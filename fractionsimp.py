import math
from fractions import gcd
def getnums():
    numerator = int(input("Pease enter your numerator:"))
    denominator = int(input("Pease enter your denominator:"))
    return (numerator, denominator)

def simplify(numerator, denominator):
    
    greatestcommondenomondeano = gcd(numerator, denominator)
    print('greatest common denominator:', greatestcommondenomondeano, '\n')
    simplifiednum = numerator / greatestcommondenomondeano

    simplifieddenom = denominator / greatestcommondenomondeano
    print(simplifiednum)
    print('-----')
    print(simplifieddenom)


nums = getnums()
numer = nums[0]
denom = nums[1]
simplify(numer, denom)
