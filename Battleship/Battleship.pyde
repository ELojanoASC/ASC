def setup():
    size(500,500)
    background(255)

board = [[1,1,1,1,1],
         [1,1,1,1,1],
         [1,1,1,1,1],
         [1,1,1,1,1],
         [1,1,1,1,1]]

board[0][3] = 0 # SHIP

print board
def draw():
    
    counter = 0
    x = 0
    y = 0
    
    for row in board:
        for column in row:
            if column == 1:
                fill(255)
                rect(x,y,100,100)
                x += 100 # column = column + 100 +=, -=
            elif column == 0:
                fill(255,0,0)
                rect(x,y,100,100)
        x = 0
        y = y + 100
    
    
    # while counter < 5:
    
    #     for i in range(len(board)):
    #         if (board[0],[1][i] == 1):
    #             rect(i*100, y, 100,100)
    #         # elif board[0][i] == "empty":
    #         #     fill(255)
    #         #     rect(i * 100, y, 100, 100)
    #     y = y + 100
    #     counter = counter + 1
    
    
"""        
    if mousePressed == True:
        if mouseY < 100 and mouseX < 100:
            if board[0][0] == 1:
                board[0][0] = "empty"
                print board
        else:
            print "you are using blue."
"""
            
                