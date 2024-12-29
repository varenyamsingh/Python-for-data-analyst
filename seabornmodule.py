import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {"Days":[1, 2, 3, 4],
        "People":[60, 30, 40, 25]}

df = pd.DataFrame(data)
print(df)

sns.lineplot(data=data, x="Days", y="People")
plt.show()




