from dataclasses import dataclass
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()


@dataclass
class DataIngestionConfig:
    ingestion_dir: Path
    cluster_db: str
    prod_collection: str
    category_collection: str
    
    
@dataclass
class VectorStoreConfig:
    pc_index: str
    params: Path
    
    
@dataclass
class InferenceAPIConfig:
    cluster_db: str
    prod_collection: str
    pc_index: str