# Square Lab
from Myro import * #ImportAllFunction
init("sim") #StartSimulator

x = 2 #Speed
y = 2 #seconds

d = 90 #Degrees
z = "deg" #Measurement

i = 0 #StartCounter
penDown() # Put pen down

while i < 4:
    forward(x,y)
    turnBy(d,z)
    i = i + 1
    