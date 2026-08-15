#Which airlines have the highest delay rate?
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def highest_delay_rate(df):
    print("="*50)
    print("HIGHEST DELAY RATE:")
    print("="*50)
    print(df.groupby("op_unique_carrier")["dep_delay"].apply(lambda x: (x>0).mean()*100).sort_values(ascending= False).head(10).round(2))

#Which airlines have the highest average delay?
def highest_average_delay(df):
    print("="*50)
    print("HIGHEST AVERAGE DELAY")
    print("="*50)
    print(df.groupby("op_unique_carrier")["dep_delay"].mean().sort_values(ascending=False).head(10).round(2))

#Which airports have the highest delay rate?
def airport_highest_delay_rate(df):
    print("="*50)
    print("AIRPORT WITH HIGHEST DELAY RATE")
    print("="*50)
    print(df.groupby("origin_city_name")["dep_delay"].apply(lambda x: (x>0).mean()*100).sort_values(ascending= True).head(10))