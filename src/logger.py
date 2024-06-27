import os
import logging
from datetime import datetime


log_dir = os.path.join(os.getcwd(), 'LOGS')
os.makedirs(log_dir, exist_ok=True)

log_filename = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
log_filepath = os.path.join(log_dir, log_filename)


with open(log_filepath, 'w') as log:
    """Create log file"""
    pass


logging.basicConfig(
    filename=log_filepath,
    level=logging.INFO,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)