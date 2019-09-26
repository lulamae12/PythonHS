from phue import Bridge
from ips import *
from tkinter import *
bridge = Bridge(hueBridge)
lights = [1,2,3,4,5,6]

def IsLightOn():
    for light in lights:
        lightOn = bridge.get_light(lights, "on")
        if lightOn == True:
            print("Light ",light, " is on.\n")
        else:
            print("Light ",light, " is on.\n")
def changeBrightness(light, brightness):
    if brightness > 254:
        brightness = 254
    bridge.set_light(light, 'bri', brightness)


class HomeDash:
    def __init__(self, master):
        self.master = master

        master.title("HomeDash")
        window = Canvas(master, width=200, height=60)
        window.pack()
        canvas_height=200
        canvas_width=200
        y = int(canvas_height / 2)

        self.label = Label(master, text="Light control")
        self.label.pack()

        self.greet_button = Button(master, text="Turn on lights", command=self.popup)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def turnOn(self):
        changeBrightness(1,255)

root = Tk()
my_gui = HomeDash(root)
root.mainloop()









#startup
#bridge.connect()
#bridge.get_api()
#IsLightOn()
main()
window.cb()
