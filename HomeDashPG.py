from phue import Bridge
from ips import *
import pygame as pg

bridge = Bridge(hueBridge)
lights = [1,2,3,4,5,6]
pg.init()
pg.display.set_caption("Home Dash: Beta")
screen = pg.display.set_mode((1500,900))
pg.display.update()
clock = pg.time.Clock()
clock.tick(60)

def IsLightOn():
    for light in lights:
        lightOn = bridge.get_light(light, "on")
        if lightOn == True:
            print("Light ",light, " is on.")
        else:
            print("Light ",light, " is off.")
def changeBrightness(light, brightness):
    if brightness > 254:
        brightness = 254
    bridge.set_light(light, 'bri', brightness)





class Background():
    def __init__(self):
        self.floorPlan = pg.image.load("floorplan001.png")
        self.floorPlan = pg.transform.scale(self.floorPlan, (1500, 900))
        self.floorPlanRect = self.floorPlan.get_rect()
        screen.blit(self.floorPlan, self.floorPlanRect)
        pg.display.update()
class Light():
    def __init__(self):
        self.light = pg.image.load("bulbOff.png")

        self.light = pg.transform.scale(self.light, (32, 32))
        self.lightRect = self.light.get_rect()
        pg.display.update()

    def lightPostion(self, x, y):
        screen.blit(self.light,(x,y))
        self.lightRect = self.light.get_rect()
        self.lightX = x
        self.lightY = y

        self.lightRect = self.light.get_rect().move(x,y)
        pg.display.update()

    def isClicked(self, x,y):
        self.lightX = x
        self.lightY = y
        self.imageType = 0# 0 is off 1 is on
        self.lightRect = self.light.get_rect().move(self.lightX, self.lightY)
        if pg.mouse.get_pressed()[0] and self.lightRect.collidepoint(pg.mouse.get_pos()) and not False:
            self.light = pg.image.load("bulbOn.png")
            print("Clicked")
            pg.display.update()
            if self.imageType == 0:
                self.light = pg.image.load("bulbOn.png")
                pg.display.update()
                self.imageType == 1
            if self.imageType == 1:
                self.light = pg.image.load("bulbOff.png")
                pg.display.update()
                self.imageType == 0
                def chang




def lightGroup():
    light1 = Light()
    light2 = Light()
    light3 = Light()
    light4 = Light()
    light5 = Light()
    light6 = Light()

    light1.lightPostion(900,90)
    light2.lightPostion(900,560)
    light3.lightPostion(900,350)
    light4.lightPostion(900,260)
    light5.lightPostion(900,460)
    light6.lightPostion(900,660)





light1 = Light()
#startup
bridge.connect()
bridge.get_api()

screen.fill((0,0,255))
pg.display.flip()
Background()
lightGroup()
gameRunning = True
while gameRunning: #main loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
            gameRunning == False
        light1.isClicked(900,90)
        print(pg.mouse.get_pos())
        if pg.mouse.get_pressed()[0] and light1.lightRect.collidepoint(pg.mouse.get_pos()) and not False:
             = pg.image.load("bulbOn.png")
            print("Clicked")
        pg.display.update()


    #lightbr = input("num: ")
    #changeBrightness(1,int(lightbr))
