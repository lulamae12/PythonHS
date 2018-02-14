from graphics import *
win = GraphWin(width = 600, height = 600)
win.setCoords(0, 0, 12, 12)
cube = Rectangle(Point(2,2), Point(10,10))#back
cube2 = Rectangle(Point(1,1), Point(9,9))#front
line1 = Line(Point(10,10), Point(9,9))#upper right
line2 = Line(Point(2,2), Point(1,1))#lower left
line3 = Line(Point(10,2), Point(9,1))#lower Right
line4 = Line(Point(2,10), Point(1,9))#upper left
cube.draw(win)
cube2.draw(win)
line1.draw(win)
line2.draw(win)
line3.draw(win)
line4.draw(win)
win.getMouse()
win.close()
