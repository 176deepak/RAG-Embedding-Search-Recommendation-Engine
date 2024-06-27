from src.config import configuration
from src.components.data_ingestion import DataIngestion


class DataIngestionPipeline:
    def __init__(self):
        pass
    
    
    def process(self):
        config = configuration.ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        ingestion_dir = data_ingestion.ingest_data()
        
        return ingestion_dir
