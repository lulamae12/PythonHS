import random,os
import pygame as pg
from colors import *

currentSong = []

appRunning = True
screenSize = (400,600)#widow width and height
path = os.getcwd()#get dir for songs

print("The current directory is : %s" % path)
print("Songs:",os.listdir("Songs"))

pg.init()

pg.display.set_caption("mp3 test")#load caption
screen = pg.display.set_mode(screenSize)#set size
class MP3():
    def __init__(self):
        self.speed = .5
    def controls(self):
        key = pg.key.get_pressed()
        if key[pg.K_RIGHT]:#Next Song
            print("PRESSED: NEXT")
        if key[pg.K_LEFT]:#last Song
            print("PRESSED: LAST")



#main loop
def main():
    while appRunning: #main loop
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
                appRunning == False
        mp3.controls()
mp3 = MP3()

main()
