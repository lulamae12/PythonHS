import math
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
#main menu
print("please choose a category")
print("1. Basic math")
print("2. Algebra")
print ("3. Pythagreon therom")
print ("please choose a category")
category = int(input("choice: "))
if choice == '1': #basic math
    print("please choose your function")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("please choose a number.")
    num1 = int(input("first number: "))
    num2 = int(input("second number: "))
    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
#if choice == '3':
#    print please
