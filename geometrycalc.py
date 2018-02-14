#must have geofunc.py
import sys
import math
import geofunc
def opening():
    print("please choose what formula to do.")
    print("1. Area of a Rectangle")
    print("2. Area of a Circle")
    print("3. Circumference of a Circle")
    print("4. Exit")
    userinput = input()
    if userinput == '1':
        Rectangle()
    if userinput == '2':
        CircleArea()
    if userinput == '3':
        Circumference()
    if userinput == '4':
        sys.exit()
def Rectangle():
    usrLen = float(input("Give the length: "))
    usrWidth = float(input("Give the width: "))
    area = geofunc.AreaOfRectangle(usrLen,usrWidth)

    print(f"Area is {area}")
def CircleArea():
    usrRad = float(input("Give the Radius:"))
    area = geofunc.AreaOfCircle(usrRad)
    print(f"area is {area}")
def Circumference():
    usrRad = float(input("Give the Radius:"))
    Circumference = geofunc.CircumferenceOfCircle(usrRad)
    print(f"Circumference is {Circumference}")
opening()
