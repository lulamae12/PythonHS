import math
import chaosSig
import time

def pytheorem():
    choice = input("Find hypotenuse or a side? h or s\n")
    if choice == "h":
        a = float(input("A?\n"))
        b = float(input("B?\n"))
        c = float(math.sqrt(a**2+b**2))
        print("The hypotenuse is "+str(c)+".")
    if choice == "s":
        a = float(input("Give the length of one leg.\n"))
        c = float(input("Give the hypotenuse.\n"))
        b = float(math.sqrt(c**2-a**2))
        print("The length of the unknown leg is "+str(b)+".")

def midpointForm():
    xOne = float(input("Give the X value of the first point.\n"))
    yOne = float(input("Give the Y value of the first point.\n"))
    xTwo = float(input("Give the X value of the second point.\n"))
    yTwo = float(input("Give the Y value of the second point.\n"))

    midx,midy = (xOne+xTwo)/2, (yOne+yTwo)/2
    print("The midpoint is ("+str(midx)+", "+str(midy)+").")

def distanceForm():
    xOne = float(input("Give the X value of the first point.\n"))
    yOne = float(input("Give the Y value of the first point.\n"))
    xTwo = float(input("Give the X value of the second point.\n"))
    yTwo = float(input("Give the Y value of the second point.\n"))

    dist = float(math.sqrt((xTwo-xOne)**2+(yTwo-yOne)**2))
    print("The distance between the two given points is "+str(dist)+" units.")

def improperToMixed():
    num = int(input("Give the numerator of the improper fraction."))
    den = int(input("Give the denominator of the improper fraction."))

    newNum = num // den
    newDen = num % den
    print("The mixed number is {} and {}/{}".format(newNum,newDen,den))

def mixedToImproper():
    wholeNum = int(input("Give the whole number."))
    num = int(input("Give the numerator of the fraction."))
    den = int(input("Give the denominator of the fraction."))

    newNum = den*wholeNum+num
    print("The improper fraction is {}/{}.".format(newNum,den))

def slopeFinder():
    xOne = float(input("Give the X value of the first point.\n"))
    yOne = float(input("Give the Y value of the first point.\n"))
    xTwo = float(input("Give the X value of the second point.\n"))
    yTwo = float(input("Give the Y value of the second point.\n"))
    
    try:
        slope = (yTwo-yOne)/(xTwo-xOne)
        print("The slope of the line that passes through the given points is {}.".format(slope))
    except ZeroDivisionError:
        print("Cannot divide by zero.  Undefined slope!")

print("Pythagorean Theorem - 1\nMidpoint Formula - 2\nDistance Formula - 3")
print("Improper to Mixed - 4\nMixed to Improper - 5\nSlope Finder - 6\n")
choice = input("Give the number assigned to the subject of your choice.\n")

if choice == "1":
    pytheorem()
elif choice == "2":
    midpointForm()
elif choice == "3":
    distanceForm()
elif choice == "4":
    improperToMixed()
elif choice == "5":
    mixedToImproper()
elif choice == "6":
    slopeFinder()
else:
    print("Your choice is not valid.  Prepare to be punsihed.")
    time.sleep(2)
    chaosSig.chaos()
