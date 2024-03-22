"""Module containing mechanisms for calculating the standard deviation between datasets
related to catchment areas. It supports both CSV and JSON data sources.
"""

import glob
import os
import pandas as pd

from catchment import models

class CSVDataSource:
    """
    A data source loader that fetches catchment data from CSV files within a specified directory.
    
    Attributes:
        data_dir (str): Directory path containing the data files.
    """

    def __init__(self, data_dir):
        """
        Initialize a CSVDataSource instance with a specific data directory.
        
        Args:
            data_dir (str): Directory path where CSV data files are stored.
        """
        self.data_dir = data_dir

    def load_catchment_data(self):
        """
        Load catchment data from CSV files matching a specific pattern in the data directory.

        Returns:
            Iterable: An iterable over the datasets loaded from each CSV file.

        Raises:
            ValueError: If no CSV files are found in the specified data directory.
        """
        data_file_paths = glob.glob(os.path.join(self.data_dir, 'rain_data_2015*.csv'))
        if len(data_file_paths) == 0:
            raise ValueError('No CSV files found in the data directory')
        data = map(models.read_variable_from_csv, data_file_paths)
        return data

class JSONDataSource:
    """
    A data source loader that fetches catchment data from JSON files within a specified directory.
    
    Attributes:
        data_dir (str): Directory path containing the data files.
    """

    def __init__(self, data_dir):
        """
        Initialize a JSONDataSource instance with a specific data directory.
        
        Args:
            data_dir (str): Directory path where JSON data files are stored.
        """
        self.data_dir = data_dir
    
    def load_catchment_data(self):
        """
        Load catchment data from JSON files matching a specific pattern in the data directory.

        Returns:
            Iterable: An iterable over the datasets loaded from each JSON file.

        Raises:
            ValueError: If no JSON files are found in the specified data directory.
        """
        data_file_paths = glob.glob(os.path.join(self.data_dir, 'rain_data_2015*.json'))
        if len(data_file_paths) == 0:
            raise ValueError('No JSON files found in the data directory')
        data = map(models.read_variable_from_json, data_file_paths)
        return data


def analyse_data(data_source):
    """
    Analyze data from a specified data source by calculating the standard deviation by day.

    Args: 
        data_source (DataSource): An object that provides a load_catchment_data method returning data.

    Returns:
        pandas.DataFrame: A DataFrame containing the standard deviation calculated for each day.
    """
    data = data_source.load_catchment_data()
    daily_standard_deviation = compute_standard_deviation_by_day(data)
    return daily_standard_deviation

def compute_standard_deviation_by_day(data):
    """
    Compute the standard deviation by day for a collection of datasets.

    Args:
        data (iterable): An iterable of datasets for which to calculate daily standard deviations.

    Returns:
        pandas.DataFrame: A DataFrame representing daily standard deviations across the datasets.
    """
    daily_std_list = map(models.daily_std, data)
    daily_standard_deviation = pd.concat(daily_std_list)
    return daily_standard_deviation

