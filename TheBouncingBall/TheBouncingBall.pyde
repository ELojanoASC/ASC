from time import *
from random import *

x = 200
y = 200
vX = 2
vY = 2

def setup():
    size(400,400)
    background(255)



def draw():
    sleep(0.01)
    global x
    global y
    global vX
    global vY
    background(255)
    fill(255,0,0)
    ellipse(x, y, 50, 50)
    sleep(0.01)
    x = x + vX
    y = y + vY
    if x == 380:
        vX = -2
    if x == 20:
        vX = 2
    if y == 380:
        vY = -2
    if y == 20:
        vY == 2