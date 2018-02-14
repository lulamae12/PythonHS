#rnggame.py
# a guess the number game by tommy smith
import random
randNum = random.randint(1,20)
def openingQuestion():
    print("hello, what is your name?")
    name = input()
    print("hello, " + name + " I am thinking of anumber between 1 and 20. You have 5 guesses left.")  
def Guesses():
    guess = 5
    while guess != 0:
        print("what number am I thinking of?")
        numGuess = int(input())
        if numGuess == randNum:
            print("thats correct!")
        if numGuess != randNum:
            if numGuess > randNum:
                print('the number is less than that')
            if numGuess < randNum:
                print('the number is greater than that')
            guess = guess - 1
            print("guesses left:" + str(guess))
    if guess == 0:
        print("sorry, you are out of guesses. The number I was thinking of was " + str(randNum))
openingQuestion()
Guesses()
