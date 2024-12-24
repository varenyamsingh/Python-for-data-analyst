'''while True:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter second number: "))
    print(num1+num2)
    break'''
# To stop while true loop we need to put break statement at last

# pattern problem
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
        