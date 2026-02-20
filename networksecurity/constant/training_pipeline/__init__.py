import os      
import sys
import pandas as pd
import numpy as np

# common variable for the training pipeline
TARGET_COLUMN = "Result"
PIPELINE_NAME: str = "NetworkSecurity"
ARTIFACT_DIR: str = "artifact"
FILE_NAME: str = "phisingData.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"





"""
    DATA_INGESTION REALTER COFING START WITH DATA_INGESTION_VARIABLES
"""


DATA_INGESTION_COLLECTION_NAME: str  ="NetworkData"
DATA_INGESTION_DATABASE_NAME: str ="ETL"
DATA_INGESTION_DIR_NAME: str ="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.2
