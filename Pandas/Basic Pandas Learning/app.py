import pandas as pd

df = pd.read_excel("SampleSuperstore.xls")

print(df)
import pandas as pd

df = pd.read_excel("SampleSuperstore.xls")
df.to_excel("SampleSuperstore.xlsx", index=False)