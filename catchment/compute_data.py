"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import pandas as pd

from catchment import models, views

class CSVDataSource:
    def __init__(self, data_dir):
        self.data_dir = data_dir

    def load_catchment_data(self):
        data_file_paths = glob.glob(os.path.join(self.data_dir, 'rain_data_2015*.csv'))
        if len(data_file_paths) == 0:
            raise ValueError('No CSV files found in the data directory')
        data = map(models.read_variable_from_csv, data_file_paths)
        return list(data)
    
class JSONDataSource:
    def __init__(self, data_dir):
        self.data_dir = data_dir

    def load_catchment_data(self):
        data_file_paths = glob.glob(os.path.join(self.data_dir, 'rain_data_2015*.json'))
        if len(data_file_paths) == 0:
            raise ValueError('No JSON files found in the data directory')
        data = map(models.read_variable_from_json, data_file_paths)
        return list(data)


def analyse_data(data_source):
    data = data_source.load_catchment_data()
    return compute_standard_deviation_by_day(data)

def load_catchment_data(data_dir):
    data_file_paths = glob.glob(os.path.join(data_dir, 'rain_data_2015*.csv'))
    if len(data_file_paths) == 0:
        raise ValueError('No CSV files found in the data directory')
    data = map(models.read_variable_from_csv, data_file_paths)
    return list(data)

def daily_std(data):
    return data.groupby(data.index.date).std()

def compute_standard_deviation_by_day(data):
    daily_std_list = map(daily_std, data)      
    daily_standard_deviation = pd.concat(daily_std_list)
    return daily_standard_deviation
