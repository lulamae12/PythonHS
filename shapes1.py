from turtle import *
print("please choose your shape.")
print("1. Square")
print("2. Circle")
print("3. Figure 8")
usrchoice = input("Choice:")
if usrchoice is "1":
    for i in range(4):
        forward(25)
        right(90)
    onclick()
