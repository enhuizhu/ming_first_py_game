import pygame
from random import seed
from random import randint

pygame.init()

screenWidth = 600
screenHeight = 600

win = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("first game")

x=50
y=450
width=60
height=100
vel=5

run=True
isJump = False
jumpCount = 5
jumpCountOrigin = jumpCount;
jumpMinus = -jumpCount

seed(1)

while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
   
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x = x - vel
    
    if keys[pygame.K_RIGHT] and x < screenWidth - width:
        x = x + vel

    if not(isJump):
        if keys[pygame.K_UP] and y > vel:
            y = y - vel
        if (keys[pygame.K_DOWN]) and y < screenHeight - height:
            y = y + vel
        if (keys[pygame.K_SPACE]):
            isJump = True
    else:
        if jumpCount >= jumpMinus:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= jumpCount ** 2 * 0.5 * neg
            jumpCount = jumpCount - 1
        else:
            isJump = False
            jumpCount = jumpCountOrigin
    
    win.fill((0, 0, 0))
    red = randint(0, 255)
    green = randint(0, 255)
    black = randint(0, 255)
    # width = randint(1, 23)
    # height = randint(1, 23)
    pygame.draw.rect(win, (red, green, black), (x, y, width, height))
    # pygame.draw.circle(win, (red, green, black), (x, y + 40), 10)
    # pygame.draw.polygon(win, (red, green, black), [[x, y + 80], [x, y + 90], [x + 10, y + 90]])
    pygame.display.update()

pygame.quit()