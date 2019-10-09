from luhn import *

ccNumber = input("Number: ")

if verify(ccNumber):
    print("Correct")
else:
    print("incorrect")
