import pygame
from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    #创建Play按钮
    play_button=Button(ai_settings,screen,'Play')

    #创建一个用于储存游戏统计信息的实例,并创建记分牌
    stats=GameStats(ai_settings)
    sb=Scoreboard(ai_settings,screen,stats)

    #创建一艘飞船
    ship=Ship(ai_settings,screen)
    #创建一个用于储存子弹的编组
    bullets=Group()
    #创建一个用于储存外星人的编组
    aliens=Group()
    #创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)
    #加入混响
    pygame.init()
    pygame.mixer.init()
    #开始游戏主循环
    while True:
        #监视键盘和鼠标
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,
                        aliens,bullets)
        if stats.game_active:
            #移动飞船
            ship.update()
            #刷新子弹
            gf.update_bullets(ai_settings,screen,sb,stats,ship,aliens,bullets)
            #更新外星人
            gf.update_aliens(ai_settings,stats,screen,sb,ship,aliens,bullets)
            
        #刷新屏幕
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,
                         bullets,play_button)
        if pygame.mixer.music.get_busy():
            continue
        pygame.mixer.music.load('music/全民飞机大战-music-游戏的音乐(game_music)_爱给网_aigei_com.mp3')
        pygame.mixer.music.set_volume(0.6)
        pygame.mixer.music.play()

run_game()
