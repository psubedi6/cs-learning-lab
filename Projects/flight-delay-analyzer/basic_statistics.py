import numpy as np
import pandas as pd
def basic_statistics(df):
    #basic stats of the data 
    print(f"Statistical summary of columns are:\n{df.describe(include="all")}")

    print("The delay in departure more than 30 mins")
    print(df[df["dep_delay"] > 30])