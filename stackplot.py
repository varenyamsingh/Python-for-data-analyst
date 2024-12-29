import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
people1 = [50, 10, 35, 20, 45]
people2 = [10, 30, 35, 40, 50]
people3 = [85, 50, 75, 90, 85]
plt.stackplot(days, people1, people2, people3, colors=["red", "magenta", "hotpink"], labels=["week1", "week2", "week3"])
plt.legend()
plt.show()