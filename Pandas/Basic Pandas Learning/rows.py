import pandas as pd

df = pd.read_csv("artist.csv")

print("display first 10 rows")
print(df.head(10))

print("Display 10 last rows")
print(df.tail(10))