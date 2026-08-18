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
    airport_highest_delay_rate,
    most_delay_months,
    flight_delay_cause,
    higthest_delay_routes,
    airlines_cancelation_rate,
)
from analysis import (
    average_arrival_delay,
    cancellation_rate,
    early_vs_delayed
)
from visualization import(
    airlines_avg_arrival_delay,
    distribution_arrival_delay,
    delayed_vs_notDelayed
)
def main():
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

    most_delay_months(df)

    flight_delay_cause(df)

    higthest_delay_routes(df)

    airlines_cancelation_rate(df)

    average_arrival_delay(df)

    cancellation_rate(df)

    early_vs_delayed(df)




    #visualization
    airlines_avg_arrival_delay(df)
    distribution_arrival_delay(df)
    delayed_vs_notDelayed(df)

if __name__== "__main__":
    main()