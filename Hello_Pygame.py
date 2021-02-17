import pygame
import sys
from colors import *
from icecream import ic

pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('HELLO PyGAME!')

x = 50
y = 50

w = 100
h = 50

speed = 5

run = True

while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        ic(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
    if keys[pygame.K_RIGHT] and (x < 800 - w -5):
        x += speed
    if keys[pygame.K_UP] and y > 5:
        y -= speed
    if keys[pygame.K_DOWN] and (y < 600 - h - 5):
        y += speed

    window.fill(BLACK)
    pygame.draw.rect(window, BLUE, (x, y, w, h))
    pygame.display.update()