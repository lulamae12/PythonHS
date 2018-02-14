#python program
# problem #2
#must be run in python3
import sys
List = [2,4,6,8,10]
def forloop():
    forlooplist = []
    for l in List:
        forlooplist.append(l)
    forlooplistsum = sum(List)
    return(forlooplistsum)
def whileloop():
    whilelooplist = []
    while len(whilelooplist)!= len(List):
        for l in List:
            whilelooplist.append(l)
    whilelooplistsum = sum(whilelooplist)
    return(whilelooplistsum)
def Output():
    print(f"this is the list of numbers to add: {List}")
    print(f"this is the sum found by the for loop: {forloop()}")
    print(f"this is the sum found by the while loop: {whileloop()}")
    sys.exit()
Output()
