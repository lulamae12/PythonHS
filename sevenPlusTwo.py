import math
def calc(num1, num2 ):
    sum = num1 + num2
    sum = sum/3
    print(math.ceil(sum))



while True:
    firstNum = int(input("num 1: "))
    secondNum = int(input("num 2: "))

    calc(firstNum,secondNum)
