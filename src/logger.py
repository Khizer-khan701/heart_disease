import os
import logging
import datetime
from src.exception import CustomException
import sys

LOG_FILE=f"{datetime.datetime.now().strftime("%d_%M_%Y_%H_%M_%S")}.log"
file_path=os.path.join(os.getcwd(),"Logs")
os.makedirs(file_path,exist_ok=True)
LOG_FILE_PATH=os.path.join(file_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(name)s %(lineno)d - %(levelname)s - %(message)s",
    level=logging.INFO
)



