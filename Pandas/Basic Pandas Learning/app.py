import pandas as pd

df = pd.read_csv("artist.csv")

print(df)
import pandas as pd

df = pd.read_csv("artist.csv")
df.to_csv("output.csv", index=False)