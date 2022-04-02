from pygame import*
game = True
clock = time.Clock() 
okno = display.set_mode((1250,620))

color = (196,73,14)
aboba = Rect(30, 30, 60, 60)


while game:
    for i in event.get():  
        if i.type == QUIT: 
            game = False
    okno.fill((255,0,0))
    draw.rect(okno,color,aboba)
          
          
          
    display.update()
