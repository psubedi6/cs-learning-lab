import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def clean_data(df):

    df = df.copy()

    # Convert Date column to datetime
    df["Date"] = pd.to_datetime(df["Date"])

    # Remove duplicate rows
    df = df.drop_duplicates()

    return df