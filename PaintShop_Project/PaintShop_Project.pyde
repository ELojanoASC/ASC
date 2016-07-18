color = 0
def setup():
    size(500,500)
    background(255,255,255)

def draw():
    global color
    noStroke()
    # red box
    fill(255,0,0)
    rect(0,0,50,50)
   
     #blue box
    fill(0,0,255)
    rect(50,0,50,50)
   
     #yellow box
    fill(255,255,0)
    rect(100,0,50,50)

    #purple box
    fill(255,0,255)
    rect(150,0,50,50)
    
    #neon blue box
    fill(0,255,255)
    rect(200,0,50,50)
    
    #green box
    fill(0,255,0)
    rect(250,0,50,50)
    
    #black box
    fill(0,0,0)
    rect(300,0,50,50)
    
    #baby blue box
    fill(50,100,150)
    rect(350,0,50,50)
    
    #orange box
    fill(255,165,0)
    rect(400,0,50,50)
    
    #navy blue box
    fill(0,0,100)
    rect(450,0,50,50)
    
    #gray box
    fill(100,100,100)
    rect(500,0,50,50)
    

    if mouseButton == LEFT:
        if mouseY < 50: # WITHIN COLOR BOXES
            if mouseX < 50: # Red box
                color = 0
                print "You are using red."
            elif mouseX < 100: # blue box
                print "You are using blue."
                color = 1
            elif mouseX < 150: # yellow box
                print "You are using yellow."
                color = 2
            elif mouseX < 200: # purple box
                print "You are using purple."
                color = 3
            elif mouseX < 250: # neon blue box
                print "You are using neon blue."
                color = 4
            elif mouseX < 300: # green box
                print "You are using green."
                color = 5
            elif mouseX < 350: # black box
                print "You are using black."
                color = 6
            elif mouseX < 400: # baby blue box
                print "You are using baby blue."
                color = 7
            elif mouseX < 450: # orange box
                print "You are using orange."
                color = 8
            elif mouseX < 500: # navy blue box
                print "You are using navy blue."
                color = 9 
            else: # gray box
                print "You are using gray."
                color = 10
        else:
            if color == 0:
                fill(255,0,0)
            elif color == 1:
                fill(0,0,255)
            elif color == 2:
                fill(255,255,0)
            elif color == 3:
                fill(255,0,255)
            elif color == 4:
                fill(0,255,255)
            elif color == 5:
                fill(0,255,0)
            elif color == 6:
                fill(0,0,0)
            elif color == 7:
                fill(50,100,150)
            elif color == 8:
                fill(255,165,0)
            elif color == 9:
                fill(0,0,100)
            else:
                fill(100,100,100)
                
            rect(mouseX,mouseY,50,50)
                
            
            
    