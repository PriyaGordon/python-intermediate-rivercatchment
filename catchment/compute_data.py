"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import pandas as pd

from catchment import models


def analyse_data(data_dir):
    """Calculate the standard deviation by day between datasets.

    Gets all the measurement data from the CSV files in the data directory,
    works out the standard deviation for each day. 
    """
    data = load_catchment_data(data_dir)
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

def load_catchment_data(data_dir):
    """
    Loads data from CSV files in the specified data directory
    Args: 
        data_dir : directory in which data files are located
    Returns:
        data : read-in data
    Raises:
        ValueError : If no .csv files are found in the target directory
    """
    data_file_paths = glob.glob(os.path.join(data_dir, 'rain_data_2015*.csv'))
    if len(data_file_paths) == 0:
        raise ValueError('No CSV files found in the data directory')
    data = map(models.read_variable_from_csv, data_file_paths)
    return data
