import pygame
import sys
from icecream import ic

pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('HELLO PyGAME!')


w = 100
h = 50

x = (800 - w)//2
y = 600 - h - 5


speed = 5

game_run = True

jump = False
jumpCount = 10

while game_run:
    pygame.time.delay(10)

    # TODO: добавить хендлер событий
    for event in pygame.event.get():
        ic(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # TODO: добавить хендлер нажатий клавиш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
    if keys[pygame.K_RIGHT] and (x < 800 - w -5):
        x += speed
    if not jump:
        if keys[pygame.K_UP] and y > 5:
            y -= speed
        if keys[pygame.K_DOWN] and (y < 600 - h - 5):
            y += speed
        if keys[pygame.K_SPACE]:
            jump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 3
            else:
                y -= (jumpCount ** 2) / 3
            jumpCount -= 1
        else:
            jump = False
            jumpCount = 10

    window.fill((0, 0, 0))
    pygame.draw.rect(window, (0, 0, 255), (x, y, w, h))
    pygame.display.update()