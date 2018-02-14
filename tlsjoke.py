#tlsjoke.py
#a simple joke program by tommy smith
from graphics import *
import time
import sys
print('hello, please enter your name:')
name = input()
if 'hack' in name:
    print('deploying hack countermeasures')
    time.sleep(10)
    
    import heck
    heck()
def getAnswer():
    JokeAnswer = input()
    if 'stick' in JokeAnswer:
            print ("you got it!")
    elif JokeAnswer != 'a stick':
            print ("its a s\ tick!")
def answer():
    print("want to hear a joke? yes or no?")
    answer = input()
    if answer == 'yes':
        print ("ok, here is the joke")
        print ("what is brown and sticky?")
    if answer == 'no':
        print ("ok then.")
        sys.exit()
def endquestion():
    print("did you like the joke?")
    endquestion = input()
    if 'yes' in endquestion:
        print("im glad you liked it!")
        sys.exit()
    if 'no' in endquestion:
        print("ok then. maybe next time.")
        sys.exit()

answer()
getAnswer()
endquestion()























if name is 'bob':
    print('hi')
