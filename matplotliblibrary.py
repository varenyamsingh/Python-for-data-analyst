#Matplotlib is a low level graph plotting library in python that serves as a visualization utility.

import matplotlib.pyplot as plt

y = [65, 78, 87, 98, 56]
x = ["Part1", "Part2", "Part3", "Part4", "Part5"]
color = ["red", "green", "blue", "purple", "grey"]
plt.bar(x, y, color = color, edgecolor = "yellow")
plt.xlabel("All Parts", fontsize = 15)
plt.ylabel("Popuarity", fontsize = 15)
plt.title("Harry Potter", fontsize = 10)
plt.show() # it will pop up the graph from the above data



