import pandas as pd

customers = pd.DataFrame({
    "CustomerID": [1,2,3],
    "Name": ["Ramesh", "Suresh", "Kalpesh"]
})

df_orders = pd.DataFrame({
    "CustomerID":[1,2,4],
    "OrderAmount":[250, 450, 320]
})

df_merged= pd.merge(customers, df_orders, on="CustomerID", how= "outer")
print(df_merged) 