import sys
import pygame
from bullet import Bullet

def fire_bullet(bullets,screen,rocket):
    """发射子弹"""
    if len(bullets) < 4:
        new_bullet=Bullet(screen,rocket)
        bullets.add(new_bullet)
    

def check_keydown(event,rocket,screen,bullets):
    """响应按键"""
    if event.key==pygame.K_RIGHT:
        rocket.moving_right=True
    elif event.key==pygame.K_LEFT:
        rocket.moving_left=True
    elif event.key==pygame.K_DOWN:
        rocket.moving_down=True
    elif event.key==pygame.K_UP:
        rocket.moving_up=True
    elif event.key==pygame.K_SPACE:
        fire_bullet(bullets,screen,rocket)
        

def check_keyup(event,rocket):
    """响应松开"""
    if event.key==pygame.K_RIGHT:
        rocket.moving_right=False
    elif event.key==pygame.K_LEFT:
        rocket.moving_left=False
    elif event.key==pygame.K_DOWN:
        rocket.moving_down=False
    elif event.key==pygame.K_UP:
        rocket.moving_up=False

def check_events(rocket,screen,bullets):
    """响应鼠标和按键"""
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown(event,rocket,screen,bullets)
        elif event.type==pygame.KEYUP:
            check_keyup(event,rocket)

def update(screen,rocket,bg_color,bullets):
    screen.fill(bg_color)
    #绘制子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    rocket.blitme()
    pygame.display.flip()

def bullet_update(bullets,screen):
    """更新子弹位置,并删除已消失的子弹"""
    bullets.update()
    screen_rect=screen.get_rect()
    #删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.x >= screen_rect.right:
            bullets.remove(bullet)
    
    
        
