'''def hello(): # Defining our function
    print("Hello World")
    
hello() # Calling our function this will print

# Add function by giving values
def add(x, y):
    return ("The addition of two numbers is", x+y)
    
print(add(12, 56)) # giving values for adding'''


# Factorial of any number
def fact(n):
    if n == 1:
        return 1
    else:
        return(n*fact(n-1))
    
print(fact(5)) # Calling function 
