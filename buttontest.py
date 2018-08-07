#buttontest.py
#this is written in python 3
#TLS
from graphics import *

WINDOW_WIDTH, WINDOW_HEIGHT = 200, 150 #set window height and length

win = GraphWin("button ewxample", WINDOW_WIDTH, WINDOW_HEIGHT)#load window with button example as title

def buttons():#define button
    button = Rectangle(Point(25, 55), Point(55, 85))  # points are ordered ll, ur. first point is lower left next is upper right
    button.setFill("blue") #fill button with color blue
    button.draw(win)#draw button to window
    return button#return button so it can be used in other def statements

def inside(point, rectangle):#this statement checks if mouse point is inside the button
    """check if point is inside the rectangle? """

    ll = rectangle.getP1()  # assume p1 is ll (lower left)
    ur = rectangle.getP2()  # assume p2 is ur (upper right)

    return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY() #return points and dimensions

button = buttons()#call buttons

centerPoint = Point(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)#define centerpoint of window

while True:
    clickPoint = win.getMouse()#get mouse and set it as the var clickPoint

    if clickPoint is None:  #for error handle
        pass#ignore
    elif inside(clickPoint, button):#if mouse click is inside the button, execute code in statement.
        print("button pressed")
    else:#finishes if statements
        pass

win.close()#closewindows
"""|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"""
#this is a part of code that makes a button and extecutes code when its pressed. i tried to comment it best i could. in my opinon, if you can it may be better to use a python module like tkinter(wheich is sometimes a pain but is made for this type of stuff )or pygame (which is also sometimes good for this stuff)
#but  graphics.py should be fine. i would only check those out if yopu wanna go more in depth.
#a python module that is  good for data montioring and graphing is matplotlib. it is very versatile and is well documented here:https://matplotlib.org/
#the file dogstatgraph.py on my gitghub uses matplotlib to graph if u want to look at it for refrence.
#my github repo: https://github.com/lulamae12/Python
