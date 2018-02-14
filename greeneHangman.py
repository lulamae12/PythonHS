from turtle import *
import random
from time import *

def gallows():
    win = Screen()
    forward(100)
    left(180)
    forward(50)
    right(90)
    forward(200)
    left(90)
    forward(100)
    left(90)
    forward(50)
    
def head():
    right(90)
    circle(25)
    up()
    left(90)
    forward(50)
    down()
    
def chest():
    forward(50)
    up()
    left(180)
    forward(25)
    left(135)
    down()
    
def armOne():
    forward(25)
    up()
    right(180)
    forward(25)
    right(90)
    down()
    
def armTwo():
    forward(25)
    up()
    right(180)
    forward(25)
    left(135)
    forward(25)
    down()
    
def legOne():
    right(45)
    forward(25)
    up()
    right(180)
    forward(25)
    right(90)
    down()
    
def legTwo():
    forward(25)
    up()
    right(180)
    forward(25)
    left(135)
    forward(100)
    write("Rest In Peace, {}.".format(name), move=False, align="left", font=("Times New Roman", 20, "normal"))

def game():
    randWord = random.choice(words)
    words.remove(randWord)
    wordArray = list(randWord)
    cat = wlist[randWord]
    steps = [head,chest,armOne,armTwo,legOne,legTwo]
    hideturtle()
    pensize(5)
    global name
    global win
    bad = 0
    win = False
    
    guessed = []
    blanks = ["_"]*len(randWord)

    print("Welcome to Hangman.  Whether you walk away with your life determines on your luck and/or thinking ability.")
    name = input("Enter your name so we know what to put on your tombstone: ")
    print("Alright, {}, let's get to it then...\n".format(name))
    gallows()

    print("The word starts with: {}".format(wordArray[0]))
    while blanks.count("_") != 0 and bad < 6:
        print("Category: {}".format(cat))
        print(" ".join(blanks))
        print("Letters Guessed: {}".format(", ".join(guessed)))

        guess = str.upper(input("Make a guess: "))
        if guess.isalpha() is False or len(guess) != 1:
            print("Invalid guess.  Give a single letter only")
            continue
        if guess in guessed:
            print("Already guessed")
            steps[bad]()
            bad = bad + 1
            sleep(.5)  
        elif guess in wordArray:
            print("{} is in the word".format(guess))
            for i in range(len(wordArray)):
                if guess == wordArray[i]:
                    blanks[i] = guess
                    if blanks.count("_") == 0:
                        win = True
                        break
        elif guess not in wordArray:
            print("{} is not in the word".format(guess))
            steps[bad]()
            bad = bad + 1
            sleep(.5)
        if guess not in guessed:
            guessed.append(guess)

    if bad == 6:
        print("\nYou breathe your final breath.  The word was {}\n".format(randWord))  
    if win == True:
        print(" ".join(blanks))
        print("Congratulations, {}, you have won\n".format(name))

wlist = {"APPLE":"Food","CAKE":"Food","PIZZA":"Food","CHICKEN":"Food"}
words = [i for i in wlist.keys()]

again = True
while again is True:
    game()
    while again != "y" and again != "n":
        again = str.lower(input("Would you like to play again? y or n: "))
    if again == "y":
        if len(words) != 0:
            reset()
            again = True
        else:
            print("There are no more words in the wordlist")
    elif again == "n" and win == False:
        print("May your eternal rest never be disrupted, {}".format(name))
    elif again == "n" and win == True:
        print("A wise decision, {}".format(name))
