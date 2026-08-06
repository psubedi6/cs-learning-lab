import pandas as pd

data = {
    "Name": ["David", "Alice", "Mathew", "Rick", "Nitto"],
    "Age": [22,45,23,53,87],
    "Salary": [4000, 5000, 3500, 6700, 8000]
}

df = pd.DataFrame(data)
print(df)

df.sort_values(by = "Name", ascending= False, inplace= True)

print("Sorting age by descending")
print(df)