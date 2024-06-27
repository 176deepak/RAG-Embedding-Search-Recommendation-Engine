import os
import pandas as pd
from tqdm import tqdm
from src.utils.vector_store_utils import *
from src.entity import VectorStoreConfig


class VectorStore:
    def __init__(self, config:VectorStoreConfig):
        self.config = config
        self.pc_index=pc_client.Index(self.config.pc_index)
    
    
    def initiate_vector_upsertion(self, data_ingestion_dir):
        files = os.listdir(data_ingestion_dir)
        
        for file in files:
            namespace = file.split(".csv")[0]
            
            df = pd.read_csv(os.path.join(data_ingestion_dir, file))
            df['description'] = df['title'] + ' \n ' + df['category']
            records = df.to_dict('records')
            
            print(f"Category:{namespace} vector store...")
            
            BATCH_SIZE = 64
            for i in tqdm(range(0, len(records), BATCH_SIZE)):
                try:
                    batch = records[i:i+BATCH_SIZE]
                    
                    pc_records = []
                    for product in batch:
                        product_ebd = get_embedding(product['description'])
                        pc_record = {
                            'id': product['objectID'],
                            'values': product_ebd.flatten().tolist()
                        }
                        pc_records.append(pc_record)

                    self.pc_index.upsert(vectors=pc_records, namespace=namespace)
                except Exception as e: 
                    logging.info(f"{e}")
                    raise CustomException(e, sys)
            logging.info(f"file:{file} vector inserted successfully!")            
