#IF YOU DO NOT HAVE MACK'S CHAOS MODULE, A CERTAIN PART OF THIS PROGRAM WILL ERROR OUT!
import time
from chaosSig import chaos

def joke():
    print("What did Ubuntu say to macOS and Windows?")
    setupRe = input()
    print("Let's all put aside our differences and live together in Unity!")

def opinion():
    opinion = input("Did you like my joke? y or n")

    if opinion == "y":
        if name == "Mack":
            print("I'm not in any way criticizing your ways, my Great Creator, but laughing at your own joke is pretty narcissistic and is generally frowned upon by society...")
        else:
            print("Great! You've escaped my Great Creator's chaotic wrath...this time... \n¯\_(ツ)_/¯")
        
    if opinion == "n":
        if name != "Mack":
            print("You and my Great Creator do not share the same sense of humor.  I am a computer, therefore I have no reasoning skills, therefor you must be PUNISHED!")
            time.sleep(5)
            chaos()
        if name == "Mack":
            print("You do not share a sense of humor with yourself, then.  I am a computer, therefore I have no reasonability, therefore you must be PUNISHED!")
            time.sleep(5)
            print("...but since you're the Great Creator and chaos is disabled under your name, I guess I'll just let you off on a warning.")

name = input("What is your name?\n")
if name == "Mack":
    print("--Chaos has been disabled, my Great Creator.--")

readyCheck = input("Greetings, "+name+".  Are you ready for me to put your sides into orbit? y or n")

if readyCheck == "y":
    print("Okay, here we go.")
    joke()
    opinion()

if readyCheck == "n":
    print("Okay, here's a five-second breather for you to use to prepare yourself in.")
    time.sleep(5)
    print("And we're off!")
    joke()
    opinion()
