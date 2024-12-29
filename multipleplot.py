# This can be important because from this we can draw any type of graph we want to

import seaborn as sns 
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
print(data)

a = sns.FacetGrid(data, col="time", height=3, hue="sex")
a.map(sns.barplot, "day", "tip")
plt.show()



