import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def basic_statistics(df):

    amount = df["Amount"]

    print("\n" + "=" * 50)
    print("BASIC STATISTICS")
    print("=" * 50)

    print(f"Total Transactions: {len(df)}")
    print(f"Total amount: ${amount.sum()}")
    print(f"Average Transaction: ${df['Amount'].mean()}")
    print(f"Largest Transaction: ${amount.max()}")
    print(f"Smallest Transation: ${amount.min()}")

    print("\n Descritive Statistics: ")
    print(df.describe())