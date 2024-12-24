# write a program to display a person's name, age and address in different lines
'''name = "Tony"
age = 23
address = "Delhi"
print(name)
print(age)
print(address)'''


# Swap two variables
'''a = 23
b = 25
# 1st method for swapping using temporary variable
temp = a 
a = b
b = temp 
print(a, b) 
# 2nd method for swapping using arithmetic operators
a, b = b, a 
print(a, b)'''


# Convert float to int
'''num = 23.3
num = int(num)
print(type(num))'''


# take input as int and then convert it to float
'''num = int(input("Enter a number: "))
num = float(num)
print(num)
print(type(num))'''


# Sum of all even numbers upto 50
'''sum = 0
for i in range(1, 51):
    if i % 2 == 0:
        sum += i
print("sum of all even numbers upto 50 is: ", sum)'''


# Write first 20 numbers and their squared numbers
'''for i in range(1, 21):
    print(i, i*i)'''
    
    
# Find sum of first 10 odd numbers
sum = 0
for i in range(1, 11):
    if i % 2 != 0:
        sum += i
print(sum)




