# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
import yaml
from sklearn.model_selection import train_test_split
import pandas as pd
from src.logger import infologger

# Log information about the script starting
infologger.info('Basic cleaning and Splitting into train test data from the whole data')

class TrainTestData:
    def __init__(self,read_path,params,write_path=None):
        # intialize the class variable with the parameters
        self.read_path=read_path
        self.write_path=write_path
        self.test_params=params['test_params']
        self.seed=params['seed']
        self.trip_duration_lowerlimit=params['trip_duration_lowerlimit']
        self.trip_duration_uplimit = params['trip_duration_uplimit']
        self.pickup_latitude_lowlimit = params['pickup_latitude_lowlimit']
        self.pickup_latitude_uplimit = params['pickup_latitude_uplimit']
        self.dropoff_latitude_lowlimit = params['dropoff_latitude_lowlimit']
        self.dropoff_latitude_uplimit = params['dropoff_latitude_uplimit']
        self.pickup_longitude_lowlimit = params['pickup_longitude_lowlimit']
        self.pickup_longitude_uplimit = params['pickup_longitude_uplimit']
        self.dropoff_longitude_lowlimit = params['dropoff_longitude_lowlimit']
        self.dropoff_longitude_uplimit = params['dropoff_longitude_uplimit']
        pass
        infologger.info(f'Call to make_dataset with  the parameter:Data read Path:{self.read_path} 
                        , Data write path: {self.write_path}, Test Percentage: {self.test_per}, and seed value: ')
    def read_data(self):
         
         '''This function reads data from input path and stores it into a dataframe'''
         try:
                # Read data from the provided CSV file
                self.df=pd.read_csv(self.read_path)

         except Exception as e:
               infologger.info(f'Reading failed with error: {e}')
         else:
            # Log if reading is successful
            infologger.info('Read performed successfully')
    def data_type_conversation(self):
         try:
              self.df['pickup_datetime']=pd.to_datetime(self.df['pickup_datetime'])
            #   converting dropoff timestamp into datetime object
              self.df['dropoff_datetime']=pd.to_datetime(self.df['dropoff_datetime'])
         except Exception as e:
              # Log if object into date conversion fails
            infologger.info(f'Date conversion of columns has failed with error : {e}')
         else:
            # Log if object into datetime conversion is successful
            infologger.info('Date conversion performed successfully')

              
              
          
         
         
             




































@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
  

    main()
