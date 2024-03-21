  """Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import pandas as pd

from catchment import models

class CSVDataSource:
    def __init__(self, data_dir):
        self.data_dir = data_dir

    def load_catchment_data(self):
        data_file_paths = glob.glob(os.path.join(self.data_dir, 'rain_data_2015*.csv'))
        if len(data_file_paths) == 0:
            raise ValueError('No CSV files found in the data directory')
        data = map(models.read_variable_from_csv, data_file_paths)
        return data

class JSONDataSource:
    def __init__(self, data_dir):
        self.data_dir = data_dir
    
    def load_catchment_data(self):
        data_file_paths = glob.glob(os.path.join(self.data_dir, 'rain_data_2015*.json'))
        if len(data_file_paths) == 0:
            raise ValueError('No JSON files found in the data directory')
            data = map(models.read_variable_from_json, data_file_paths)
            return data
        
    def analyse_data(data_source):
    """Calculate the standard deviation by day between datasets.

    Args: 
        data_source : any object with a load_catchment_data method that returns 
                      some data
    """
        data = data_source.load_catchment_data()
        daily_standard_deviation = compute_standard_deviation_by_day(data)
        return daily_standard_deviation

    def compute_standard_deviation_by_day(data):
    """
    Calculate the standard deviation by day for a given list of datasets
    Args:
        data : data for which the standard deviations are to be calculated
    Returns:
        daily_standard_deviation : pandas Dataframe of standard deviations
    """
        daily_std_list = map(models.daily_std, data)
        daily_standard_deviation = pd.concat(daily_std_list)
        return daily_standard_deviation