# fibonacci series
'''a = 0
b = 1
for i in range(2, 11):
    c = a + b
    a = b
    b = c
    print(c)'''
    

# check prime
'''num = int(input("Enter a number: "))
if num <= 1:
    print("Not a Prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")'''


# Palindrome Number
num = int(input("Enter a number: "))
temp = num
rev = 0
while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10
if rev == temp:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
    
