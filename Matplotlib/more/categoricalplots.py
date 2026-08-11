import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df= sns.load_dataset("tips")
print(df)

#countplot
sns.countplot(x= df["sex"], hue=df["smoker"])
plt.show() 

#barplot
sns.barplot(x= df["sex"], y = df["tip"])
plt.show()

sns.barplot(x= df["sex"], y = df["tip"], estimator= np.sum)
plt.show()

#boxplot
sns.boxplot(x= df["tip"], y= df["day"], data=df, palette="rainbow")
plt.show()

#vilonplot
sns.violinplot(x=df["tip"],y=df["day"], palette= "rainbow")
plt.show()

#stripplot
sns.stripplot(x= df["tip"], y= df["day"], data= df, palette="rainbow")
plt.show()

#swarmplot
sns.swarmplot(x= df["tip"], y= df["day"], data= df, palette="rainbow")
plt.show()

#vilonplot+swarmpplot
sns.violinplot(x=df["tip"],y=df["day"], palette= "rainbow")
sns.swarmplot(x=df["tip"],y=df["day"])
plt.show()