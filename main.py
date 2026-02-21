from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exceptions import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
import sys 
from networksecurity.entity.config_entity import TrainingPipelineConfig



if __name__=="__main__":
    try:
        trainingPipelineConfig=TrainingPipelineConfig()
        data_ingestion_config=DataIngestionConfig(trainingPipelineConfig)
        data_ingestion=DataIngestion(data_ingestion_config=data_ingestion_config)
        dataframe=data_ingestion.export_collection_as_dataframe()
        print(dataframe.head())
        
        data_ingestion.export_data_into_feature_store(dataframe=dataframe)
        
        train_set, test_set = data_ingestion.split_data_as_train_test(dataframe=dataframe)
        print(train_set.shape,test_set.shape)
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)