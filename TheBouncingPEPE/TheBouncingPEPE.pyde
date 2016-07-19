from time import *
from random import *

x = 200
y = 100
vX = 2
vY = 2

def setup():
    size(400,400)
    background(0)
    global pic
    pic = requestImage("SadPepe.png")

def draw():
    sleep(0.0001)
    mX = mouseX
    global mX2
    global r
    global g
    global b
    mX2 = mX + 80
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    global x
    global y
    global vX
    global vY
    global pic
    background(r,g,b)
    rect(mX, 360,100,20)
    fill(0)
    image(pic, x, y, 50, 50)
    sleep(0.0001)
    x = x + vX
    y = y + vY
    if x == 380:
        vX = -2
    if x == 20:
        vX = 2
    if y == 380:
        vY = -2
    if y == 20:
        vY = 2
    if y == 310 and x > mX and x < mX2:
        vY = -2