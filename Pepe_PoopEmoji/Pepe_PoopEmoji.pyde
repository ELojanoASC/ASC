from random import choice
def setup():
    size(500, 500)
    background(255, 255, 255)
    global pepe
    global poop
    pepe = requestImage("Pepe.jpg")
    poop = requestImage("poop.png") 
def draw():
    image(pepe, mouseY, mouseX, 100, 100)
    image(poop, mouseX, mouseY, -50, 80)
    
             