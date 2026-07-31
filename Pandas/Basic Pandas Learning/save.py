import pandas as pd

data = {
    "Name":["Bob", "Jack", "Tina"],
    "Age":[30,42,52],
    "City":["Toronto","Hamilton", "Barrie"]
}
df = pd.DataFrame(data)
print(df.to_string(index=False))
df.to_csv("output.csv", index = False)
df.to_excel("output.xlsx", index = False)
