import matplotlib.pyplot as plt

x = ["day1", "day2", "day3", "day4"]
y = [230, 150, 174, 300]
y1 = [253, 344, 211, 122]
y2 = [243, 124, 371, 210]
y3 = [203, 234, 123, 232]
plt.plot(x, y, marker = "o", ls = "--", color = "red", label = "week1")
plt.plot(x, y1, marker = "o", ls = "--", color = "purple", label = "week2")
plt.plot(x, y2, marker = "o", ls = "--", color = "green", label = "week3")
plt.plot(x, y3, marker = "o", ls = "--", color = "hotpink", label = "week4")
plt.legend()
plt.show()