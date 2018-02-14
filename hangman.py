from turtle import *
import random
import sys
misses = 8
start = 0
categories = ["Animals","Devices","Food",]

def noose():
    global start
    print('would you like to play hangman?')
    play = input()
    if 'y' in play:
        print('ok! good luck!')
        start = 1
    if 'n' in play:
        start = 0
        print('ok then.')
        sys.exit()
    while start == 1:
        pu()
        goto (0,120)
        pd()
        write("Category: " + random.choice(categories), False, align="center")
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
        break
    if start == 1:
        print('1=draw')
        test = input()
        if test == '1':
            misses - 1
        
    while misses <= 7:#head
        goto(0,65)
        right(90)
        pd()
        st()
        for i in range(360):
            tracer(0)
            update()
            forward(.25)
            right(1)
        break   
    if misses <= 6:#torso
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
    if misses <= 5:#larm
        pu()
        goto(15,35)
        pd()
        for i in range(1):
            forward(20)
            right(90)
            forward(10)
            right(90)
            forward(20)
    if misses <= 4:#rarm
        pu()
        goto(-14,35)
        pd()
        for i in range(1):
            forward(20)
            left(90)
            forward(10)
            left(90)
            forward(20)
    if misses <= 3:#leg
        pu()
        goto(-13,5)
        right(90)
        pd()
        for i in range(1):
            forward(20)
            left(90)
            forward(10)
            left(90)
            forward(20)
    if misses <= 2:#rleg
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
noose()








    
