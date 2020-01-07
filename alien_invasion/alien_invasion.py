# -*- coding:utf-8 -*-
import sys
import pygame
from setting  import Setting
from ship import Ship
import game_functions as gf
from bullet import Bullet
from  pygame.sprite import Group

def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings=Setting()
	#screen=pygame.display.set_mode((1200,800))
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	ship=Ship(ai_settings,screen)
	#子弹编组
	bullets = Group()
	
	#背景色
	#bg_color=(230,230,230)
	
	#开始游戏的主循环
	while True:
		#监视鼠标和键盘事件
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		#每次循环都重绘屏幕
		#screen.fill(ai_settings.bg_color)		
		#ship.blitme()	
		#让最近绘制的屏幕可见
		#pygame.display.flip()
		gf.update_bullets(bullets)
		gf.update_screen(ai_settings, screen, ship, bullets)

run_game()