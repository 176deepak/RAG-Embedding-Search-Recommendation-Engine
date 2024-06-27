import os
import yaml
import sys
from src.exception import CustomException
from src.logger import logging

def make_dirs(dirs:list[str]):
    try:
        for dir in dirs:
            os.makedirs(dir, exist_ok=True)
        logging.info(f"{dirs} directory created.")
    except Exception as e:
        logging.info(f"{e}")
        raise CustomException(e, sys)

        
def make_files(files:list[str]):
    try:
        for file in files:
            with open(file, 'w') as f:
                f.close()    
        logging.info(f"{files} files created.")
    except Exception as e:
        logging.info(f"{e}")
        raise CustomException(e, sys)
    

def read_yml(filepath:str):
    try:
        with open(filepath, 'r') as file:
            filedata = yaml.safe_load(file)
            file.close()
        logging.info(f"{filepath} reading done.")    
        return filedata
    except Exception as e:
        logging.info(f"{e}")
        raise CustomException(e, sys)
