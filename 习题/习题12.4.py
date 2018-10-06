import pygame
import sys

pygame.init()
screen=pygame.display.set_mode((600,600))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            print(event.key)
