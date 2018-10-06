import sys
import pygame
from rocket import Rocket
import function as f
from pygame.sprite import Group

screen=pygame.display.set_mode((600,600))
rocket=Rocket(screen)
bg_color=(230,230,230)
bullets=Group()
while True:
    f.update(screen,rocket,bg_color,bullets)
    f.check_events(rocket,screen,bullets)
    rocket.update()
    f.bullet_update(bullets,screen)
    
    


