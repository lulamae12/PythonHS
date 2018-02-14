import math
def gradecomp():
    print("please enter your grade")
    score = input()
    if int(score) >= 90:
        print('your grade is an A')
    if int(score) >= 80 and int(score) < 90:
        print('your grade is a B')
    if int(score) >= 70 and int(score) < 80:
        print('your grade is a C')
    if int(score) >= 61 and int(score) < 70:
        print('your grade is a D')
    if int(score) <= 60:
        print('your grade is an F')
gradecomp()
        
    
