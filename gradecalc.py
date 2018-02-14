import math
import sys
gradelist = []
stop = False
def gradescale():
    print("please enter your grade")
    average = input()
    if int(average) >= 90:
        print('your grade is an A')
    if int(average) >= 80 and int(average) < 90:
        print('your grade is a B')
    if int(average) >= 70 and int(average) < 80:
        print('your grade is a C')
    if int(average) >= 61 and int(average) < 70:
        print('your grade is a D')
    if int(average) <= 60:
        print('your grade is an F')
def start():
    print("this program will take grades that you enter in and give you the average, sum and count of the numbers entered")
    print("when you are done entering numbers, simply type finish to calculate.")
    print('are you ready to start?')
    start = input()
    if 'y' in start:
        print('ok. Starting program.')
        gradeinput()
    if 'n' in start:
        print('ok. Exiting program.')
        sys.exit()
def gradeinput():
    global stop
    global gradelist
    while stop is False:
        grade = input('input your grade:')
        gradelist.append(grade)
        try:
            if "finish" in grade:
                gradelist.remove('finish')
                gradecalc()
                break
            if float(grade).is_integer():
                print('ok')
        except:
                print('please enter a valid number or make sure you are correctly spelling finished.')
                
                

def gradecalc():
    Sum = list(map(int, gradelist))
    print(Sum)
    totalgrade = sum(Sum)
    print(totalgrade)
start()

