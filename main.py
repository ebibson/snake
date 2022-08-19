import pygame
import os, sys
import time  
import random

pygame.init()

SIZE = (WIDTH, HEIGHT) = (600, 600)

# config the size and the title
pygame.display.set_caption("Snake")
screen = pygame.display.set_mode(SIZE)


colors = ['Red']


# create fruits the ywil be generated randomly
fruit = pygame.Surface((10, 10))
fruit.fill('Red')

screen.blit(fruit, (random.randint(1, 599), random.randint(1, 599)))

# create the Snake
snake = pygame.Surface((20, 20))
snake.fill('Green')

screen.blit(snake, (200, 100))

while 1:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            

   #update every time
    pygame.display.update()

