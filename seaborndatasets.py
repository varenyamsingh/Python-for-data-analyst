import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")#tips is a default seaborn data taken from seaborn library from internet
print(data)
sns.barplot(data=data, x='day', y="tip")
plt.plot()
plt.show()


