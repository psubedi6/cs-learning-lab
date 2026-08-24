import pandas as pd

df = pd.read_csv("data/retailpulse.csv")

#First 5 row
print(df.head())

#Rows and Columns
print(df.shape)

#Columns names
print(df.columns)

#data types of data
print(df.info())

#How many unique invoices are there?
print(df["Invoice"].nunique())

#How many unique products (StockCode) are there?
print(df["StockCode"].nunique())

#How many unique customers (Customer ID) are there?
print(df["Customer ID"].nunique())

#How many unique countries are there?
print(df["Country"].nunique())

