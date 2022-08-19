import pygame
import os, sys
import time  

pygame.init()

SIZE = (WIDTH, HEIGHT) = (600, 600)

# config the size and the title
pygame.display.set_caption("Snake")
pygame.display.set_mode(SIZE)


while 1:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #update every time
    pygame.display.update()

