#!/usr/env python
# simple chat bot
# author: ari

from datetime import date
import time
import numpy as np

feelings = [ 'good', 'okay', 'terrific', 'terrible']
get_feeling = lambda x: "I'm feeling %s, thank you for asking" % x
get_editor = "my favorite text editor is vim of course!"

def get_time():
    today = date.today()
    unixtime = time.time()
    return "Today is %s for humans. For me, it's %s " % (str(today), unixtime)

def get_feel():
    choice = np.random.randint(len(feelings))
    return get_feeling(feelings[choice])


while True:
    print "hello, I'm chat bot ask me something"
    query = raw_input()

    if query == "How are you?":
        print get_feel()
    elif query == "What is the date?":
        print get_time()
    elif query == "What is your favorite text editor?":
        print get_editor
    elif query in ["q", "quit"]:
        print "goodbye it was great speaking with you today."
        break
    else:
        print "sorry, but I do not understand %s." % query


