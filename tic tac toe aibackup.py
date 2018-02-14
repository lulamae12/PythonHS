
import time
from turtle import *
#
#    1_2_3_
#  1|1 2 3
#  2|4 5 6
#  3|7 8 9
space1 = 'empty'
space2 = 'empty'
space3 = 'empty'
space4 = 'empty'
space5 = 'empty'
space6 = 'empty'
space7 = 'empty'
space8 = 'empty'
space9 = 'empty'
Row1H = 'empty'
Row2H = 'empty'
Row2H = 'empty'
Row1V = 'empty'
Row2V = 'empty'
Row3V = 'empty'
Row1D = 'empty'
Row2D = 'empty'
playerturn = True
def board():
    setup (width=500, height=500, startx=1000, starty=0)
    title("TIC TAC TOE")
    pu()
    goto(-100,50)
    pd()
    forward(150)
    pu()
    goto(-100,0)
    pd()
    forward(150)
    pu()
    goto(-50,100)
    right(90)
    pd()
    forward(150)
    pu()
    goto(0,100)
    pd()
    forward(150)
    ht()
board()
def intro():
    print("today we are playing hangman.")
    print("you are \"O\" and the computer is \"X\"")
    print("please click where you want to place your O")
    onscreenclick(getPos)
    mainloop()

def getPos(x,y):
    global space1
    global space2
    global space3
    global space4
    global space5
    global space6
    global space7
    global space8
    global space9
    global playerturn
    global Row1H
    global Row2H
    global Row3H
    global Row1V
    global Row2V
    global Row3V
    global Row1D
    global Row2D
    ht()
    pu()
    print("(", x, "," ,y,")")
    while playerturn is True:
        if(x >= -100 and x <= -51) and (y >= 54 and y <= 102) and (space1 != x and space1 == 'empty'): #box 1 center:
            seth(270)
            goto(-95,74)#add 20 to x to match up
            pd()
            st()
            circle(20)
            ht()
            print('1')
            if space1 != 'x':
                space1 = 'o'
            playerturn = False
        else:
            print("that space has already been used")
            playerturn = False
        if(x >= -48 and x <= -1) and (y >= 50 and y <= 102) and (space2 != x and space2 == 'empty'): #box 2
            seth(270)
            goto(-44,74)#add 20 to x to match up
            pd()
            st()
            circle(20)
            ht()
            print('2')
            if space2 != 'x':
                space2 = 'o'
            playerturn = False
        else:
            print("that space has already been used")
            playerturn = False
        if(x >= 1 and x <= 44) and (y >= 53 and y <= 102) and (space3 != x and space3 == 'empty'): #box 3
            seth(270)
            goto(4,74)#add 20 to x to match up
            pd()
            st()
            circle(20)
            ht()
            print('3')
            if space3 != 'x':
                space3 = 'o'
            playerturn = False
        if(x >= -100 and x <= -51) and (y >= 2 and y <= 50) and (space4 != x and space4 == 'empty'): #box 4 
            seth(270)
            goto(-95,25)#add 20 to x to match up
            pd()
            st()
            circle(20)
            ht()
            print('4')
            if space4 != 'x':
                space4 = 'o'
            playerturn = False
        if(x >= -48 and x <= -1) and (y >= 2 and y <= 50) and (space5 != x and space5 == 'empty'): #box 5
            seth(270)
            goto(-44,25)#add 20 to x to match up
            pd()
            st()
            circle(20)
            ht()
            print('5')
            if space5 != 'x':
                space5 = 'o'
            playerturn = False
        if(x >= 1 and x <= 44) and (y >= 2 and y <= 50) and (space6 != x and space6 == 'empty'): #box 6
            seth(270)
            goto(4,25)#add 20 to x to match up
            pd()
            st()
            circle(20)
            ht()
            print('6')
            if space6 != 'x':
                space6 = 'o'
            playerturn = False
        if(x >= -100 and x <= -51) and (y >= -46 and y <= -2) and (space7 != x): #box 7 
            seth(270)
            goto(-95,-26)#add 20 to x to match up
            pd()
            st()
            circle(20)
            ht()
            print('7')
            if space7 != 'x':
                space7 = 'o'
            playerturn = False
        if(x >= -48 and x <= -1) and (y >= -46 and y <= -2) and (space8 != x and space1 == 'empty'): #box 8
            seth(270)
            goto(-44,-26)#add 20 to x to match up
            pd()
            st()
            circle(20)
            ht()
            print('8')
            if space8 != 'x':
                space8 = 'o'
            playerturn = False
        if(x >= 1 and x <= 44) and (y >= -46 and y <= -2) and (space9 != x and space1 == 'empty'): #box 9
            seth(270)
            goto(4,-26)#add 20 to x to match up
            pd()
            st()
            circle(20)
            ht()
            print('9')
            if space9 != 'x':
                space9 = 'o'    
            playerturn = False
    else:#x's
        print('comp would play')
        if (space2 is 'o' and space3 is 'o'):#box1H
            pu()
            goto(-93,57)
            pd()
            st()
            seth(0)
            left(45)
            forward(50)
            backward(25)                
            left(90)
            forward(25)
            backward(50)
            ht()
            print('1')
            if space1 != 'o':
                space1 = 'x'
        else:
            playerturn = True
        if (space1 is 'o' and space3 is 'o'):#box2H
            pu()
            goto(-45,57)
            pd()
            st()
            seth(0)
            left(45)
            forward(50)
            backward(25)                
            left(90)
            forward(25)
            backward(50)
            ht()
            print('2')
            if space2 != 'o':
                space2 = 'x'
        else:
            playerturn = True
        if (space1 is 'o' and space2 is 'o'):#box3H
            pu()
            goto(6,57)
            pd()
            st()
            seth(0)
            left(45)
            forward(50)
            backward(25)                
            left(90)
            forward(25)
            backward(50)
            ht()
            print('3')
            if space3 != 'o':
                space3 = 'x'
        else:
            playerturn = True
        if (space5 is 'o' and space6 is 'o'):#box4H
            pu()
            goto(-93,5)
            pd()
            st()
            seth(0)
            left(45)
            forward(50)
            backward(25)                
            left(90)
            forward(25)
            backward(50)
            ht()
            print('4')
            if space4 != 'o':
                space4 = 'x'
        else:
            playerturn = True
intro()




