import time
import board
import neopixel
import adafruit_lis3dh
import touchio
import audioio
import math
import busio

postiveMovementThreshold = 72
negativeMovementThreshold = 72

Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0)
Lime = (0,255,0)
Blue = (0,0,255)
Yellow = (255,255,0)
Cyan = (0,255,255)
Magenta = (255,0,255)
Silver = (192,192,192)
Gray = (128,128,128)
Maroon = (128,0,0)
Olive = (128,128,0)
Green = (0,128,0)
Purple = (128,0,128)
Teal = (0,128,128)
Navy = (0,0,128)












pixel_pin = board.EXTERNAL_NEOPIXEL

# The number of NeoPixels
num_pixels = 30


ORDER = neopixel.GRB
RightTouch = touchio.TouchIn(board.A2)
LeftTouch = touchio.TouchIn(board.A2)       # Rightmost capacitive touch pad
Audio = audioio.AudioOut(board.A0)
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False,
                           pixel_order=ORDER)

"""ACCELEROMETER"""
I2C = busio.I2C(board.SCL, board.SDA)
try:
    ACCEL = adafruit_lis3dh.LIS3DH_I2C(I2C, address=0x18) # Production board
except:
    ACCEL = adafruit_lis3dh.LIS3DH_I2C(I2C, address=0x19) # Beta hardware
ACCEL.range = adafruit_lis3dh.RANGE_4_G



def StaticColor(color):
    for i in range(num_pixels):
        pixel[i] = color
    pixels.show()

def LightWhenMoved(idle,movement):
    if accelerationSquared > postiveMovementThreshold:
        for i in range(num_pixels):
            pixel[i] = movement
        pixels.show()
    else:
        for i in range(num_pixels):
            pixel[i] = idle
        pixels.show()



def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos*3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos*3)
        g = 0
        b = int(pos*3)
    else:
        pos -= 170
        r = 0
        g = int(pos*3)
        b = int(255 - pos*3)
    return (r, g, b) if ORDER == neopixel.RGB or ORDER == neopixel.GRB else (r, g, b, 0)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)


while True:
    accelerationX, accelerationY, accelerationZ = ACCEL.acceleration # Read accelerometer
    accelerationSquared = accelerationX * accelerationX + accelerationY * accelerationY
    pixels.show()


    rainbow_cycle(0.001)    # rainbow cycle with 1ms delay per step
