fruits = ["Mango", "Banana", 1, 2, 34.5, "Grapes"]
a = []
'''print(fruits)
print(type(fruits))
print(fruits[2:6])
print(fruits.append("Hulk"))
print(fruits.remove("Banana"))'''

for i in range(len(fruits)):
    print(fruits[i])
    
# Swap two elements
fruits[0], fruits[2] = fruits[2], fruits[0]
print(fruits)