import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    """管理发射子弹"""
    def __init__(self,screen,rocket):
        """在火箭所在位置创建子弹"""
        super().__init__()
        self.screen=screen
        #创建子弹
        self.rect=pygame.Rect(0,0,15,5)
        self.rect.centery=rocket.rect.centery
        self.rect.right=rocket.rect.right
        self.color=60,60,60
        self.speed_factor=1

    def update(self):
        """向右移动子弹"""
        self.rect.x+=self.speed_factor

    def draw_bullet(self):
        """在屏幕绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)
