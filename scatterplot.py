import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(10, 140, 77)
y = np.random.randint(40, 100, 77)
# print(len(x), len(y))
plt.scatter(x,y)
plt.show()