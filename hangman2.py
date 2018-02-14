from turtle import *
import random
import sys
from time import *
misses = 7
start = 0
categories = ["Animals","Devices","Food",]
#credit to mack for helping me with this
clear()
clear()
def noose():
    for i in range(1):
        pu()
        goto(-20,90)
        pd()
        forward(120)
        right(90)
        forward(25)
        right(90)
        forward(120)
        right(90)
        forward(25)
        pu()
        goto(90,65)
        right(180)
        pd()
        forward(120)
        right(90)
        forward(25)
        right(90)
        forward(120)
        ht()
        pu()       

def head():
    goto(0,65)
    right(90)
    pd()
    st()
    for i in range(360):
        tracer(0)
        update()
        forward(.25)
        right(1)
def torso():
    tracer(1)
    pu()
    goto(15,35)
    right(90)
    pd()
    for i in range(1):
        forward(30)
        right(90)
        forward(28)
        right(90)
        forward(30)
        right(90)
        forward(28)
def Larm():
    pu()
    goto(15,35)
    pd()
    for i in range(1):
        forward(20)
        right(90)
        forward(10)
        right(90)
        forward(20)
def Rarm():#rarm
    pu()
    goto(-14,35)
    pd()
    for i in range(1):
        
        forward(20)
        left(90)
        forward(10)
        left(90)
        forward(20)
def Lleg():#leg
    pu()
    goto(-13,5)
    left(270)
    pd()
    for i in range(1):
        forward(20)
        left(90)
        forward(10)
        left(90)
        forward(20)
def Rleg():#rleg
    pu()
    goto(15,5)
    pd()
    right(180)
    for i in range(1):
        forward(20)
        right(90)
        forward(10)
        right(90)
        forward(20)
    pu()
    ht()


def game():

    progress = [head,torso,Larm,Rarm,Lleg,Rleg]
    categories = ["Animals","Devices","Food"]
    print('hello what ia your name?')
    name = input()
    print('hi there,'+ name +' today we are playing hangman')
    noose()

    word = '0' 
    miss = 0
    category = random.choice(categories)
    
    print("your category is:" + category)
    guessedLetter = []
    

    if category is "Devices":
        word = 'IPHONE'
    
    if category is "Animals":
        word = 'HORSE'

    if category is "Food":
        word = 'APPLE'
    
    spaces = ["_"]*len(word)
    wordArray = list(word)

    print("The word starts with: {}".format(wordArray[0]))
    while spaces.count("_") != 0 and miss < 6:
        print("Category: {}".format(category))
        print(" ".join(spaces))
        print("Letters Guessed: {}".format(", ".join(guessedLetter)))

        guess = str.upper(input("Make a guess: "))
        if guess.isalpha() is False or len(guess) != 1:
            print("Invalid guess.  Give a single letter only")
            continue
        if guess in guessedLetter:
            print("Already guessed")
            progress[miss]()
            miss = miss + 1
            sleep(.5)  
        elif guess in wordArray:
            print("{} is in the word".format(guess))
            for i in range(len(wordArray)):
                if guess == wordArray[i]:
                    spaces[i] = guess
                    if spaces.count("_") == 0:
                        win = True
                        break
        elif guess not in wordArray:
            print("{} is not in the word".format(guess))
            miss = miss + 1
            progress[miss]()
        if guess not in guessedLetter:
            guessedLetter.append(guess)
    if miss == 6:
        print('game over')
        
        

game()  




























