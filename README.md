from pygame import*
game = True
clock = time.Clock() 
okno = display.set_mode((1250,620)) 
while game:
    for i in event.get():  
        if i.type == QUIT: 
            game = False






display.update()
