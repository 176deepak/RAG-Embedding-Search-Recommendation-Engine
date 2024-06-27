from src.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.pipeline.vector_store_pipeline import VectorStorePipeline

STAGE = "DATA INGESTION"
try:
    pipeline = DataIngestionPipeline()
    ingestion_dir = pipeline.process()
except Exception as e:
    print(e)    
    
    
STAGE = "VECTOR STORE"
try:
    pipeline = VectorStorePipeline()
    pipeline.process(ingestion_dir=ingestion_dir)
except Exception as e:
    print(e)