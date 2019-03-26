#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import pygame
import time
from setting import *


pygame.init ()

def key_control_number():#玩家数量——获取按键操作
	k=0
	x,y = pygame.mouse.get_pos ()
	if x >= 55 and x <= 380 and y >= 120 and y <= 170:
		k = 11
	elif x >= 55 and x <= 380 and y >= 200 and y <= 250:
		k = 12
	elif x >= 55 and x <= 380 and y >= 280 and y <= 330:
		k = 13
	elif x >= 55 and x <= 380 and y >= 360 and y <= 410:
		k = 14
	for event in pygame.event.get ():
		if event.type == pygame.QUIT:
			exit ()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			print ('x=',x)  # 显示鼠标点击位置
			print ('y=',y)
			if x >= 55 and x <= 380 and y >= 120 and y <= 170:
				k = 21
			elif x >= 55 and x <= 380 and y >= 200 and y <= 250:
				k = 22
			elif x >= 55 and x <= 380 and y >= 280 and y <= 330:
				k = 23
			elif x >= 55 and x <= 380 and y >= 360 and y <= 410:
				k = 24
			elif True:
				k = 0
	return k


def select_player_number(screen):
	play_number = 0  #玩家数量
	fps = 0  #记录画面数
	k_number = 0
	while True:  #选择玩家数量循环
		fps = fps + 1
		text_font = pygame.font.Font ('C:\Windows\Fonts\simhei.ttf',30)
		text_number = text_font.render ("游戏开始请选择玩家数量",True,(140,40,255))
		text_number1 = text_font.render ("·······一个玩家",True,(0,0,255))
		text_number2 = text_font.render ("·······两个玩家",True,(0,0,255))
		text_number3 = text_font.render ("·······三个玩家",True,(0,0,255))
		text_number4 = text_font.render ("·······四个玩家",True,(0,0,255))
		screen.blit (select_player_number_picture,(0,0))
		screen.blit (text_number,(50,50))
		if k_number == 0 or k_number > 10:  #实现鼠标移到选项上选项进行闪烁
			if k_number != 11 or fps <= 5:
				screen.blit (text_number1,(50,130))
			if k_number != 12 or fps <= 5:
				screen.blit (text_number2,(50,210))
			if k_number != 13 or fps <= 5:
				screen.blit (text_number3,(50,290))
			if k_number != 14 or fps <= 5:
				screen.blit (text_number4,(50,370))
		if k_number > 20:
			if k_number == 21:
				play_number = 1
			elif k_number == 22:
				play_number = 2
			elif k_number == 23:
				play_number = 3
			elif k_number == 24:
				play_number = 4
			return play_number  #跳出选择数量循环

		if fps == 7:
			fps = 0

		pygame.display.update ()
		k_number = key_control_number ()
		time.sleep (0.05)

if __name__=="__main__":
	screen=pygame.display.set_mode((1200,800),0,0)
	select_player_number (screen)