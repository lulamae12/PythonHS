#test922.py
#TLS
#a simple calculator program
import time
import math
#defs tell how to do diffrent problems 
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
print('hello there! what is you name?')
print('Name:')
name = input()#get name
print('hello, '+name+'! i am a simple calculator program that can do')
print('addition, subtraction, multiplication and divison.')
time.sleep(.5)
choice = input('please choose an operator:')#get operator
time.sleep(1)
num1 = int(input('please choose the first number(dont spell out number):'))#get first number
time.sleep(1)
num2 = int(input('please choose the second number(dont spell out number):'))#get second number

if choice == 'addition' or '+':#add
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == 'subtraction' or '-':#subtract
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == 'multiplication' or '*' or 'x':#multiply
    print(num1, "X", num2, "=", multiply(num1, num2))
elif choice == 'division' or '/':#divide
    print(num1, "/", num2, "=", divide(num1, num2))
