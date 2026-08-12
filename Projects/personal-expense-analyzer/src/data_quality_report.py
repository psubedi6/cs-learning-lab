import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def data_quality_report(df):
    print("\n" + "=" * 50)
    print("DATA QUALITY REPORT")
    print("\n" + "=" * 50)

    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    print(f"\nColumns: {df.columns.tolist()}")

    print(f"\nData Types: {df.dtypes}")

    print(f"\nMissing Values: {df.isna().sum()}")

    print(f"\nDuplicate Rows: {df.duplicated().sum()}")
