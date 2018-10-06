import sys
import pygame
from 习题121配套 import Pictrue
from 习题121配套 import create_pics
from pygame.sprite import Group
def run_pic():
    """初始化并创建对象"""
    pygame.init()
    screen=pygame.display.set_mode((1200,1200))
    bg_color=(255,255,255)
    pictrue=Pictrue(screen)
    #监视输入
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    pictrues=Group()
    #绘图
    create_pics(screen,pictrues)
    while True:
        #更新屏幕
        screen.fill(bg_color)
        #绘制
        pictrues.update()
        pictrues.draw(screen)
        #绘制屏幕
        pygame.display.flip()

run_pic()
