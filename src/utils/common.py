import os
import yaml
import sys
from src.exception import CustomException

def make_dirs(dirs:list[str]):
    try:
        for dir in dirs:
            os.makedirs(dir, exist_ok=True)
    except Exception as e:
        raise CustomException(e, sys)

        
def make_files(files:list[str]):
    try:
        for file in files:
            with open(file, 'w') as f:
                f.close()    
    except Exception as e:
        raise CustomException(e, sys)
    

def read_yml(filepath:str):
    try:
        with open(filepath, 'r') as file:
            filedata = yaml.safe_load(file)
            file.close()
        return filedata
    except Exception as e:
        raise CustomException(e, sys)
