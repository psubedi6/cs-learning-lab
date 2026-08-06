import pandas as pd

df_region1 = pd.DataFrame({
    "CustomerID": [1,2],
    "Name": ["David", "Alice"]
})

df_region2 = pd.DataFrame({
    "CustomerID": [3,4,5],
    "Name": ["Rome", "Joy","Prince"]
})

df_concate = pd.concat([df_region1, df_region2], axis=1,  ignore_index=True )
print(df_concate)