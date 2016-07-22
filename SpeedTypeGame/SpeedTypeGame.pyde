from time import sleep
from random import *

alphabet = ["a", "b", "c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] 
lettersOnScreen = []
x = 0
seperator = 5
time = 0
score = 0

def setup ():
    size(600,400)
    background(255)
    
def draw():
    global x, lettersOnScreen, randomLetter, seperator, time, score
    background(255)
    time += 1
    #Time lapse
    if time%(50-seperator*2) == 0:
        lettersOnScreen.append(makeLetter())
        time = 0

    if len(lettersOnScreen) > 0:
        if keyPressed:
            if key == lettersOnScreen[0][0]:
                score = score + 1
                lettersOnScreen.pop(0)
                print score
        
        textSize(30)
        fill(255,0,0)
        
        for i in range(len(lettersOnScreen)):
            lettersOnScreen[i][1] = lettersOnScreen[i][1] + seperator
            text(lettersOnScreen[i][0], lettersOnScreen[i][1], lettersOnScreen[i][2])   
        

def makeLetter():
    return[choice(alphabet), x, randrange(0,350)]