from turtle import *
import random
import sys
misses = 7
start = 0
categories = ["Animals","Devices","Food",]

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
    
noose()

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
    right(90)
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








    
