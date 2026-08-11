import seaborn as sns
import pandas as pd
import cufflinks as cf
from plotly.offline import iplot

tips = sns.load_dataset("tips")
print(tips)

group = tips.groupby("day")["tip"].mean().iplot(kind= "bar")