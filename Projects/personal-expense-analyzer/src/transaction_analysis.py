import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def large_transactions(df, threshold= 2000):
    return df[df["Amount"]> threshold].sort_values(by="Amount", ascending = False)

def top_transactions(df, n=5):
    return df.sort_values(by="Amount", ascending = False).head(n)
