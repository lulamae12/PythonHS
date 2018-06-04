#chatbot
import random
import os
cls = lambda: os.system('cls')
cls()
def checkForGreeting(sentence, words):
    greetingKeywords = ("hello", "hi", "greetings", "hey")
    greetingResponses = ("Hi!", "Hey!", "*nods*", "Hello!")
    for word in words:
        if word in greetingKeywords:
            response = random.choice(greetingResponses)
            print(response)
def commands(words):
     for word in words:
         if '!help' in words:
             commands = open("Tarscommands","r")
             lines = commands.readlines()
             for line in lines:
                 line = line.rstrip()
                 print(line)
        elif !stock in words:
            print('stock here')
while True:
    sentence = input(">>:")
    words = sentence.split()
    checkForGreeting(sentence, words)
    commands(words)
