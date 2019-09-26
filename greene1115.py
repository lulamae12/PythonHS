import string,sys
numberList = (1,2,3,4,5,6,7,8,9,0)
userInput = input("please enter a string: ")


try:
    if userInput.find("***") != -1:
        firststar = userInput.find("*")
        laststar = firststar + 2
        firstnum = firststar - 1
        lastnum = laststar + 1
        if int(userInput[firstnum]) + int(userInput[lastnum]) == 10:
            print("true")
            sys.exit()
        else:
            print("false")
    else:
        print("false")
except (ValueError):
    print("false")
