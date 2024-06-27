from src.entity import InferenceAPIConfig
from src.utils.vector_store_utils import get_embedding, pc_client
from src.utils.data_ingestion_utils import *
from src.utils.inference_utils import extract_ids

class InferenceEps:
    def __init__(self, config:InferenceAPIConfig):
        self.config = config
        self.pc_index=pc_client.Index(self.config.pc_index)
    
    
    def get_vector_ebd(self, query:str) -> list[float]:
        try:
            ebd = get_embedding(query)
            ebd = ebd.flatten().tolist()
            return ebd
        except:
            return 500
    
    
    def vector_search(self, vector):
        try:
            records = self.pc_index.query(
                vector=vector,
                top_k=100,
            )['matches']
        
            ids = extract_ids(records)
            query = {
                'objectID': { 
                    '$in': ids 
                }
            }
        
            records = dataloader(
                db=self.config.cluster_db, 
                collection=self.config.prod_collection, 
                query=query, 
                proj={"_id":0}
            )        
        
            data = [record for record in records]

            return data
        except:
            return 500