import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def spending_by_category(df):
    return(df.groupby("Transaction Type")["Amount"].sum().sort_values(ascending = False))

def spending_percentage(df):
    category_total = spending_by_category(df)
    return(category_total / df["Amount"].sum() * 100)