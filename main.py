# This files covers the basics of python

print("""Hello
 World""") #this is single line comment in python

print("Hello \n World")

"""this is multiple
line comments"""

#variables
a = "Hello World"
print(a)

# Datatypes and user Inputs
#datatypes=str, int, float, list, tuple, range, dictionary, set, frozenset, bool, bytes, bytearray, memoryview
#user Inputs:- name = input("Enter name") \n print(name)
'''name = input("Enter Your Name: ")
print("Your name is "+name)'''

'''a = int(input()) #we cannot use float value in integer
b = float(input())
sum=(a+b)
print(sum)'''

#evaluate finction gives result of any equation
'''exp = eval(input("Enter expression: "))
print(exp)'''

#typecasting
name = "123"
age = 23
age1 = 23.5
print(type(name))
print(type(age))
print(type(age1))
print(type(age+age1))

a = int(name)#here we convert name str to int
print(a)
print(type(a))

