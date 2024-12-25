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
'''sum = 0
for i in range(1, 11):
    if i % 2 != 0:
        sum += i
print(sum)'''


# Length of string
a = "Hello World in, python {}"
print(len(a)) 
print(a.index("o", 5, 11)) # last two numbers are index numbers
print(a.capitalize())
print(a.format(a))
# Check the occurence of any alphabet 
print(a.count("o"))
print(a.lower())
print(a.upper())
print(a.title()) # makes first word in capital
print(a.find("in")) # find any word in sentence
print(a.center(5, "*"))

# String slicing
print(a[0:5]) # prints from 0 to 5 index


# Pattern Problem
'''for i in range(1, 6):
    for j in range(1, i+1):
        print(i, end=" ")
    print()'''


# Pattern Problem
'''for i in range(1, 6):
    for j in range(6, i, -1):
        print(j, end=" ")
    print()'''


