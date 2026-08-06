import pandas as pd

data = {
    "Name": ["Arun", "Varun", "Karun", "Narun", "Marun"],
    "Age": [28,34,22,34,28],
    "Salary":[5000,6000,4500,5200,4800]
}

df = pd.DataFrame(data)
grouped = df.groupby(["Age", "Name"])["Salary"].sum()
print(grouped)
