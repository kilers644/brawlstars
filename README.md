from pygame import*


while game:
    for i in event.get():  
        if i.type == QUIT: 
            game = False
