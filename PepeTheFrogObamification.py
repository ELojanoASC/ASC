from Myro import *

pic = makePicture(pickAFile()) #Chooses a File

#COLORS
Obama_DarkBlue = makeColor(0,51,76)

Obama_Red = makeColor(217,26,33)

Obama_Blue = makeColor(112,150,158)

Obama_Yellow = makeColor(252,227,166)

for pixel in getPixels(pic):

    if getGray(pixel) >  180:
        setColor(pixel, Obama_Yellow)
    elif getGray(pixel) > 120:
        setColor(pixel, Obama_Blue)
    elif getGray(pixel) > 60:
        setColor(pixel, Obama_Red)
    elif getGray(pixel) < 60:
        setColor(pixel, Obama_DarkBlue)

show(pic)