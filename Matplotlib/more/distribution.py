import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
print(df)
print(df["size"].unique())

#histplot
plt.subplot(1,2,1)
sns.histplot(df["total_bill"], bins=20, kde =True)

plt.subplot(1,2,2)
sns.histplot(df["tip"], bins=20, kde =True)
plt.show() 


#jointplot
sns.jointplot(x = "total_bill", y="tip", data= df, kind="scatter")
plt.show() 

#pairplot
sns.pairplot(df, hue= "size",palette= "rainbow")
plt.show()

#rugplot
sns.rugplot(df)
plt.show()