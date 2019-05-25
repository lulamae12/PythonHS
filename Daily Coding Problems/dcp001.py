"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17."""




def listSum(numberList,numToGet):
    for i in range(len(numberList)-1):
        remaining = int(numToGet) - numberList[i]
        if remaining in numberList:
            print(numberList[i]," + ",remaining," = ",numToGet)
            return True
    print("no match found")


listSum(numberList = [10,15,3,7],numToGet = input("number :"))
