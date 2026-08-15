import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from load_data import load_data
from clean_data import clean_data
from category import category
from basic_statistics import basic_statistics
from data_understanding import data_understanding
from general_analysis import (
    highest_delay_rate,
    highest_average_delay,
    airport_highest_delay_rate
)

file_path= "data/flight_data_2024_sample.csv"
df = load_data(file_path)

#understanding basic things about data
#presenting the clean data
clean_data(df)

#looking for categorical data
category(df)

basic_statistics(df)

data_understanding(df)

highest_delay_rate(df)

highest_average_delay(df)

airport_highest_delay_rate(df)