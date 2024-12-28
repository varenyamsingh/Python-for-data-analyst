import matplotlib.pyplot as plt

x = ["day1", "day2", "day3", "day4"]
y = [130, 150, 174, 320]
y1 = [233, 344, 211, 122]
plt.plot(x, y, marker = "o", ls = "--", color = "red", label = "week1")
plt.plot(x, y1, marker = "o", ls = "--", color = "purple", label = "week2")
plt.legend()
plt.show()