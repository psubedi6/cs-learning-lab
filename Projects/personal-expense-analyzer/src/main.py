import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from basic_statistics import basic_statistics
from category import spending_by_category, spending_percentage
from clean_data import clean_data
from data_quality_report import data_quality_report
from load_data import load_data
from transaction_analysis import large_transactions, top_transactions
from visualization.matplotlib_visualization import (
    spending_by_transaction_type,
    top_spending_categories,
    transaction_type_percentage,
    transaction_by_month,
    spending_by_month,
    average_spending_by_category,
    transaction_amount_distribution,
    transaction_amount_outliers,
)
from visualization.seaborn_visualization import(
    spending_by_account,
    amount_distribution_by_transaction_type,
    top_transaction_descriptions,
    category_frequency_vs_spending,
    category_frequency_vs_average_amount,
    category_spending_comparison,
    monthly_spending_heatmap
)

def main():
    file_path = "personal_transactions_dashboard_ready.csv"

    #we call the func load_data and pass the parameter file_path which will load the csv file as a copy and we store it in df.
    df = load_data(file_path)

    #calling the clean_data func from clean_data.py which returns the clean dataset
    df= clean_data(df)

    #calling data visuals
    #matplotlib
    spending_by_transaction_type(df)
    top_spending_categories(df)
    transaction_type_percentage(df)
    transaction_by_month(df)
    spending_by_month(df)
    average_spending_by_category(df)
    transaction_amount_distribution(df)
    transaction_amount_outliers(df)

    #seaborn
    amount_distribution_by_transaction_type(df)
    top_transaction_descriptions(df)
    category_frequency_vs_spending(df)
    spending_by_account(df)
    category_frequency_vs_average_amount(df)
    category_spending_comparison(df)
    monthly_spending_heatmap(df)


    #General info
    print("\n" + "=" * 50)
    print("DATASET PREVIEW")
    print("=" * 50)

    print(f"\nFirst 5 rows{df.head()}")
    print(f"\nLast 5 rows: {df.tail()}")

    #data quality general info as well 
    data_quality_report(df)

    #Statistics
    basic_statistics(df)

    #categories percentage, on what spent.....
    print("\n" + "=" * 50)
    print("SPENDING BY TRANSACTION TYPE")
    print("=" * 50)
    print(spending_by_category(df))

    print(f"\nSpending percentage: \n{spending_percentage(df).round(2)}")


    #largest transactions above $2000
    print("\n" + "=" * 50)
    print("TRANSACTIONS ABOVE $2,000")
    print("=" * 50)
    print(large_transactions(df))

    #top 5 largest transactions
    print("\n" + "=" * 50)
    print("TOP 5 LARGEST TRANSACTIONS")
    print("=" * 50)
    print(top_transactions(df))

if __name__== "__main__":
    main()