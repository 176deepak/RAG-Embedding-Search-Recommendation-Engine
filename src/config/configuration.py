from src.constants import *
from src.entity import *
from src.utils.common import *


class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_YAML_FILE):
        self.configurations = read_yml(config_filepath)
        make_dirs([self.configurations['artifacts_dir']])    
        
    
    def get_data_ingestion_config(self):
        make_dirs([self.configurations['data_ingestion']['ingestion_dir']])
        
        data_ingestion_config = DataIngestionConfig(
            ingestion_dir = self.configurations['data_ingestion']['ingestion_dir'],
            cluster_db=self.configurations['data_ingestion']['cluster_db'],
            prod_collection=self.configurations['data_ingestion']['prod_collection'],
            category_collection=self.configurations['data_ingestion']['category_collection']
            )
        
        return data_ingestion_config
    
    
    def get_vector_store_config(self):
        vector_store_config = VectorStoreConfig(
            pc_index=self.configurations['vector_store']['pc_index'],
            params=self.configurations['vector_store']['params']
        )
        
        return vector_store_config
    
    
    def get_inference_config(self):
        inference_config = InferenceAPIConfig(
            cluster_db=self.configurations['inference_apis']['cluster_db'],
            prod_collection = self.configurations['inference_apis']['prod_collection'],
            pc_index=self.configurations['inference_apis']['pc_index']
        )
        
        return inference_config