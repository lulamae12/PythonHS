from math import factorial
def grid():
    rights = 2
    ups = 1
    totalrightandups = rights + ups
    n = rights
    r = ups
    c = n/r
    print("total rights and ups:",int(totalrightandups))
    lineTotal = (factorial(totalrightandups) / factorial(n) / factorial(r))

    print("line/path total:",int(lineTotal))
    #print(factorial(n) / (factorial(r) * factorial(n - r)))
grid()
