from src.config import configuration
from src.components.vector_store import VectorStore


class VectorStorePipeline:
    def __init__(self) -> None:
        pass
    
    
    def process(self, ingestion_dir):
        config = configuration.ConfigurationManager()
        vector_store_config = config.get_vector_store_config()
        vector_store = VectorStore(vector_store_config)
        vector_store.initiate_vector_upsertion(ingestion_dir)
    