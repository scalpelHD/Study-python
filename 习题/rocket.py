import pygame

class Rocket():
    """创建火箭"""

    def __init__(self,screen):
        """初始化属性"""
        self.image=pygame.image.load('ship.bmp')
        self.rect=self.image.get_rect()
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False

    def blitme(self):
        """绘制图形"""
        self.screen.blit(self.image,self.rect)

    def update(self):
        """根据按键调整火箭位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx+=1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery+=1
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx-=1
        if self.moving_up and self.rect.top > 0:
            self.rect.centery-=1
            
            
            
