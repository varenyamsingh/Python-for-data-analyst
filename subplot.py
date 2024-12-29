import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [23, 43, 42, 54, 65]
a = [6, 7, 8, 9, 10]
b = [33, 53, 62, 24, 55]
plt.subplot(1, 2, 1)# row, colunm, chartnumber
plt.plot(x, y, a, b)
# plt.savefig("chart.png") # this will save our chart as a image format in out desktop
plt.show()




