import pandas as pd

data = {
    "Name": ["Bob", "Devid", "Jonney", "Priya", "Laura"],
    "Age":[22,20,30,40,None],
    "Salary": [None,3000,2000,4000,5000],
    "Performance Score":[88,33,59,None,92]
}
df = pd.DataFrame(data)
print(df.fillna(0, inplace= True))