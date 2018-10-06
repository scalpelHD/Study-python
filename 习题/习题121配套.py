import pygame
from pygame.sprite import Group
from pygame.sprite import Sprite

class Pictrue(Sprite):
    def __init__(self,screen):
        """初始化图片和位置"""
        super().__init__()
        self.screen=screen
        self.image=pygame.image.load('logo.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.x=self.screen_rect.left
        self.rect.y=self.screen_rect.top
    def update(self):
        """更新屏幕"""
        if self.rect.y < self.screen_rect.height and self.rect.x < self.screen_rect.width:
            self.rect.y+=1
            self.rect.x+=1
            
        

    def blitme(self):
        """在指定位置绘制图片"""
        self.screen.blit(self.image,self.rect)

def get_number_pics(screen,pic):
    """计算每行可容纳多少图片"""
    screen_rect=screen.get_rect()
    pic_numbers=int(screen_rect.width/pic.rect.width)
    return pic_numbers
def get_number_rows(screen,pic):
    """计算可容纳多少行"""
    screen_rect=screen.get_rect()
    number_rows=int(screen_rect.height/pic.rect.height)
    return number_rows
def create_pics(screen,pictrues):
    """绘制图片"""
    pic=Pictrue(screen)
    rows=get_number_rows(screen,pic)
    lines=get_number_pics(screen,pic)
    for line in range(lines):
        pic=Pictrue(screen)
        pic.rect.x=pic.rect.width*line
        pic.rect.y=pic.rect.height
        pictrues.add(pic)

    


        
        


            
