#rockpaperscis.py
#a rock paper scissors game
#Group: Tommy, JP, Adrian, Barton
import random
import time
playagain = 1
print('would you like to play rock paper scissors?')
yesno = input()
if 'y' in yesno: 
    print('ok lets start')
if 'n' in yesno:
    print('we\'re doing it anyway')
if 'y' not in yesno and 'n' not in yesno:
    print('please enter yes or no')
while playagain == 1:
    playerChoice = 'null'
    while 'ock' not in playerChoice  and 'aper' not in playerChoice and 'cissors' not in playerChoice:#missing first letter to allow for capitals.
        playerChoice = input('please enter your choice: ')
        if 'ock' not in playerChoice  and 'aper' not in playerChoice and 'cissors' not in playerChoice:
            print('that is not a correct answer.')
    print('rock...')
    time.sleep(.5)
    print('paper...')
    time.sleep(.5)
    print('scissors...')
    time.sleep(.5)
    print('Shoot!')

    computerchoice = random.randint(0,2)#0=rock 1=paper 2=scissors.
    if (computerchoice == 0):
        computerchoice = 'rock'
    elif (computerchoice == 1):
        computerchoice = 'paper'
    elif (computerchoice == 2):
        computerchoice = 'scissors'

    if (computerchoice == playerChoice):
        print('draw!')
    elif 'aper' in playerChoice:
        if (computerchoice == "scissors"):
            print("the computer wins! The computer had " + computerchoice )
        else:
            print("You win! The computer had " + computerchoice );
    elif 'ock' in playerChoice:
        if (computerchoice == "paper"):
            print("the computer wins! The computer had " + computerchoice )
        else:
            print("You win! The computer had " + computerchoice );
    elif "cissors" in playerChoice:
        if (computerchoice == "rock"):
            print("the computer wins! The computer had " + computerchoice )
        else:
            print("You win! the computer had " + computerchoice );
    print('would you like to play again?')
    playagain = input()
    if 'y' in playagain:
        playagain = 1

    else:
        playagain = 0
        print('ok then')
