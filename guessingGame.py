import random,os,time
from sys import exit
cls = lambda: os.system('cls')

PURPLE = '\033[95m'
BLUE = '\033[94m'
MAGENTA = "\033[35m"
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
ORANGE = "\033[91m"
ENDC = '\033[0m'
rainbowList = [RED,ORANGE,YELLOW,GREEN,BLUE,MAGENTA,PURPLE]

print(ENDC + "")
playAgain = True
try:
    while True:
        for color in rainbowList:
            print(color + "")
            time.sleep(.1)
            cls()
            print("╔════════════════════════════════════════════════════════════════════════════════════════════════════╗ ")
            print("║  ______ _     _ _______ _______ _______ _____ __   _  ______       ______ _______ _______ _______  ║ ")
            print("║ |  ____ |     | |______ |______ |______   |   | \\  | |  ____      |  ____ |_____| |  |  | |______  ║ ")
            print("║ |_____| |_____| |______ ______| ______| __|__ |  \\_| |_____|      |_____| |     | |  |  | |______  ║ ")
            print("║                                                                                                    ║ ")
            print("║                                                                                                    ║ ")
            print("║                                A Way too elaborate guessing game by Tommy Smith.                   ║ ")
            print("║                                                                                                    ║ ")
            print("╚════════════════════════════════════════[Press 'Ctrl + c' to play]══════════════════════════════════╝ ")

except(KeyboardInterrupt):
    cls()
while playAgain:



    randomNum = random.randint(0,10)
    print(GREEN + "")
    print("please guess a number from  0 - 10.")
    while True:
        try:
            print(ENDC + "")
            print(YELLOW + "")
            guess = input("guess: ")
            print(ENDC + "")
            if int(guess) >= 0 and int(guess) <= 10:
                break
            else:
                print(RED + "")
                print("That is invalid! Try again!")
        except(ValueError):
            print(RED + "")
            print("That is invalid! Try again!")
    cls()
    time.sleep(1)
    print(GREEN + "")
    print("Guess: ",guess,"\n")
    print("rolling.")
    time.sleep(.5)
    print("rolling..")
    time.sleep(.5)
    print("rolling...")
    time.sleep(.5)
    if guess == randomNum:
        print("congrats you geussed it!")
    else:
        print("\nsorry! you lost. the number was: ",randomNum)
    print(ENDC + "")
    print(YELLOW + "")
    playAgainQues = input("\nplay again? (y,N): ")
    while True:
        print(ENDC + "")
        print(GREEN + "")
        if playAgainQues == "y":
            break
        elif playAgainQues == "n":
            print("Thanks for playing!")
            print(ENDC + "")
            exit()
        else:
            print(RED + "")
            print("That is an invalid choice!")
