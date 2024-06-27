import os
import sys
import torch
import torch.nn.functional as F
from transformers import AutoModel, AutoTokenizer
from pinecone import Pinecone
from dotenv import load_dotenv
from src.exception import CustomException
from .common import read_yml
from pathlib import Path

import warnings
warnings.filterwarnings('ignore')

load_dotenv()
PC_KEY = os.getenv("PINECONE_KEY")
PC_INDEX = os.getenv("PINECONE_INDEX")

pc_client = Pinecone(api_key=PC_KEY)


params = read_yml(Path('config\params.yml'))


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
embedding_model = params['embedding_model']['model']
tokenizer = AutoTokenizer.from_pretrained(embedding_model)
model = AutoModel.from_pretrained(embedding_model, trust_remote_code=True).to(device)


def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0]
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


def get_embedding(sentence:str):
    assert isinstance(sentence, str), "Sentence should be a string"

    try:
        encoded_sentence = tokenizer(sentence, padding=True, truncation=True, return_tensors='pt', max_length=params['embedding_model']['params']['max_length'])
        encoded_sentence = {key: value.to(device) for key, value in encoded_sentence.items()}

        with torch.no_grad():
            model_output = model(**encoded_sentence)
        embedding = mean_pooling(model_output, encoded_sentence['attention_mask'])
        embedding = F.normalize(embedding, p=params['embedding_model']['params']['p'], dim=params['embedding_model']['params']['dim'])
        embedding = embedding.cpu()

        return embedding
    except Exception as e:
        raise CustomException(e, sys)




