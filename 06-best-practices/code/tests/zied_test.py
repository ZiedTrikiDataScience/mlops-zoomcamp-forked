import json
import logging

import boto3
import pandas as pd

# Configure the logger
logger = logging.getLogger('my_logger')

handler = logging.FileHandler('zied_app_log.log')  
#handler  = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s [%(levelname)s] : %(message)s')

handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)  

# Load the DataFrame
df = pd.read_parquet("./data/green_tripdata_2022-01.parquet")
logger.info("Dataframe Loaded Successefuly")





def test_zied():
    """
    Docstring just to test
    """
    assert -1 == -1 * 1
