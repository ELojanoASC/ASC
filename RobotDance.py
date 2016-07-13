#Robot Dance
from Myro import *
init("sim")

i = 0 #Start Counter
while i < 2:
    motors(-4,4,2)
    turnBy(360)
    forward(2,.25)
    backward(2,.25)