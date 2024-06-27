import os
import pandas as pd
from src.entity import DataIngestionConfig
from src.utils.data_ingestion_utils import *


class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config
        
        
    def ingest_data(self):
        records = dataloader(db=self.config.cluster_db, collection=self.config.category_collection, proj={'_id':0, 'category':1})
        categories = list(records)
        
        
        for category in categories:
            category = category['category']
            records = dataloader(db=self.config.cluster_db, collection=self.config.prod_collection, query={'category':f"{category}"}, proj={'objectID':1, 'title':1, "category":1})
            
            pd.DataFrame(records).to_csv(os.path.join(self.config.ingestion_dir, f"{category}.csv"), index=False)
        
        return self.config.ingestion_dir