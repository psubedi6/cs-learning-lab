import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

flights = sns.load_dataset("flights")
tips = sns.load_dataset("tips")

#heatmap
tips_corr = tips[["total_bill", "tip", "size"]]
print(tips_corr.corr())

sns.heatmap(tips_corr.corr(), annot= True)
plt.show()

#clustermap
sns.clustermap(tips_corr.corr())
plt.show()

#pivottable
pvtflight= flights.pivot_table(values="passengers", index="month", columns="year")
print(pvtflight)

sns.clustermap(pvtflight.corr())
plt.show()