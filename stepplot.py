import matplotlib.pyplot as plt
x = ["day1", "day2", "day3", "day4", "day5"]
y = [10, 40, 5, 70, 75]
y1 = [15, 30, 65, 5, 35]
plt.step(x, y, color="red", label="days")
plt.step(x, y1, color="green", label="people")
plt.legend()
plt.show()