import pandas as pd

data = {
    "Name": ["Bob", "Calab", "Jonney", "Priya", "Laura"],
    "Age":[22,20,30,40,50],
    "Salary": [1000,3000,2000,4000,5000],
    "Performance Score":[88,33,59,68,92]
}
df = pd.DataFrame(data)
print("Sample DataFrame")
print(df)

print(df["Name"])
print(df[["Name","Age"]])
print(df[df["Salary"]> 2000])
print(df[(df["Salary"]> 2000) & (df["Age"]>20)])
print(df[(df["Salary"]> 2000) | (df["Age"]>20)])