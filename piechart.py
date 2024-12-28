import matplotlib.pyplot as plt
brands = ["Apple", "Nokia", "Redmi"]
x = [23, 34, 45]

explode = [0.1, 0, 0] # this will cutout the graph and highlight that part
plt.pie(x, labels=brands, explode=explode, shadow=True, autopct="%.f")
plt.show()



