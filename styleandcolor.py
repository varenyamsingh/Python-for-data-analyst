import seaborn as sns 
import matplotlib.pyplot as plt

data = sns.load_dataset("exercise")
sns.set_style('whitegrid')#background
sns.barplot(x="time", y="pulse", data=data)
plt.show()




