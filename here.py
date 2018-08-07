from graphics import *

def main():
    win1=GraphWin("Menu",1000,1000)
    r1=Rectangle(Point(150,850),Point(250,800))
    r1.draw(win1)
    r1.setFill("cyan")
    tex1=Text(Point(200,830),"HalfSize")
    tex1.draw(win1)
    r2=Rectangle(Point(350,850),Point(450,800))
    r2.draw(win1)
    r2.setFill("blue")
    tex2=Text(Point(400,830),"Quarter")
    tex2.draw(win1)
    r3=Rectangle(Point(550,850),Point(650,800))
    r3.draw(win1)
    r3.setFill("pink")
    tex3=Text(Point(600,830),"Bounce")
    tex3.draw(win1)
    r4=Rectangle(Point(700,850),Point(800,800))
    r4.draw(win1)
    r4.setFill("red")
    text4=Text(Point(750,830),"Restart")
    text4.draw(win1)
    pix=Image(Point(500,500),"jeff.ppm")
    height=pix.getHeight()
    width=pix.getWidth()

    pix.draw(win1)
    winny=win1.getMouse()

    #quarter mirror work
    #ricky =first pixel
    blanky=Image(Point(500,500),193,193)
    pix = pix.zoom(int(.25))
    for i in range(width):
        for z in range(height):
            ricky=pix.getPixel(x,y)
            x = x + 1
            y = y + 1
            r=ricky[0]
            g=ricky[1]
            b=ricky[2]
            color=color_rgb(r,g,b)
            blanky.setPixel(193,0,color)

    pix.undraw()
    blanky.draw(win1)

    pix.draw(win1)







#undraw first pic
#set new pic
#create new image()etc
#.clone











main()
