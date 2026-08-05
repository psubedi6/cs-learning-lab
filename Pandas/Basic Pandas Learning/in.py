import pandas as pd

df = pd.read_csv("artist.csv")
print("Displaying the info of dataset")
print(df.info())
print(df.describe())