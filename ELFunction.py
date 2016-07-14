from Myro import *
init("sim")
#Email roger@allstarcode for questions, boi

turn = 90
speed = 2
seconds = 2

penDown()

def drawE():
    turnBy(turn)
    forward(speed,seconds)
    turnBy(turn * 3)
    forward(speed,seconds)
    turnBy(turn * 2)
    forward(speed,seconds)
    turnBy(turn)
    forward(seconds / 2,seconds)
    turnBy(turn)
    forward(speed,seconds)
    turnBy(turn * 2)
    forward(speed,seconds)
    turnBy(turn)
    forward(speed,seconds - .5)
    turnBy(turn)
    forward(speed,seconds)
drawE()

penUp()

forward(speed,seconds - 1.5)

penDown()

def drawL():
    turnBy(turn)
    forward(speed,seconds + .5)
    backward(speed,seconds + .5)
    turnBy(270)
    forward(speed,seconds)
drawL()