import pygame
from random import seed
from random import randint

pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("first game")

x=50
y=50
width=60
height=100
vel=5

run=True

seed(1)

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
   
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x = x - vel
    
    if keys[pygame.K_RIGHT]:
        x = x + vel

    if keys[pygame.K_UP]:
        y = y - vel

    if (keys[pygame.K_DOWN]):
        y = y + vel
    
    win.fill((0, 0, 0))
    red = randint(0, 255)
    green = randint(0, 255)
    black = randint(0, 255)
    width = randint(1, 23)
    height = randint(1, 23)
    pygame.draw.rect(win, (red, green, black), (x, y, width, height))
    pygame.draw.circle(win, (red, green, black), (x, y + 40), 10)
    pygame.draw.polygon(win, (red, green, black), [[x, y + 80], [x, y + 90], [x + 10, y + 90]])
    pygame.display.update()

pygame.quit()