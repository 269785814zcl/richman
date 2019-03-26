#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pygame
import time
import random
from setting import *
from dice import *
from main_richman import display_player_name_dice
pygame.init()

list_grid_pool=[]#格子池

class Grid (object):
	def __init__(self,grid_data):
		self.function=grid_data[0]#功能（移动1，地皮2，抽奖3，交税4，停留5）
		self.move=grid_data[1]#移动步数或者监狱停留回合数
		self.price=grid_data[2]#地皮价格
		self.level=grid_data[3]#地皮上房屋等级
		self.host=grid_data[4]#地皮拥有者
		self.tax=grid_data[5]#税
		self.luck=grid_data[6]#备用

list_grid_data={'1':[0,0,0,0,-1,0,0],'2':[2,0,8000,0,-1,0,0],'3':[0,0,0,0,-1,0,0],'4':[3,0,0,0,-1,0,0],'5':[2,0,3000,0,-1,0,0],
				'6':[2,0,2000,0,-1,0,0],'7':[0,0,0,0,-1,0,0],'8':[2,0,3000,0,-1,0,0],'9':[5,1,0,0,-1,0,0],'10':[2,0,5000,0,-1,0,0],
				'11':[3,0,0,0,-1,0,0],'12':[1,2,0,0,-1,0,0],'13':[0,0,0,0,-1,0,0],'14':[0,0,0,0,-1,0,0],'15':[2,0,6000,0,-1,0,0],
				'16':[4,0,0,0,-1,500,0],'17':[3,0,0,0,-1,0,0],'18':[2,0,8000,0,-1,0,0],'19':[2,0,2000,0,-1,0,0],'20':[1,-3,0,0,-1,0,0],
				'21':[3,0,0,0,-1,0,0],'22':[2,0,4000,0,-1,0,0],'23':[2,0,6000,0,-1,0,0],'24':[2,0,2000,0,-1,0,0]}
for i in range(1,25):#初始化格子数据
	list_grid_pool.append(Grid(list_grid_data['%d'%i]))
	print('%d'%list_grid_pool[i-1].move)

def window_control():
	k = 0
	x,y = pygame.mouse.get_pos ()
	for event in pygame.event.get ():
		if event.type == pygame.QUIT:
			exit ()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			print ('x=',x)  # 显示鼠标点击位置
			print ('y=',y)
			if x >= 530 and x <= 640 and y >= 420 and y <= 460:
				k = 1
			elif x>=680 and x<=790 and y>=420 and y<=460:
				k=-1
			else:
				k = 0
		elif event.type== pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				k = 1
	return k

def display_host_name(screen,list_grid_pool):
	list = {1:(190,40),2:(320,165),3:(435,35),4:(530,35),5:(635,165),6:(735,165),7:(830,35),8:(925,165),
			9:(985,135),10:(1005,395),11:(985,365),12:(985,475),13:(940,550),14:(850,550),15:(750,680),
			16:(650,550),17:(540,550),18:(435,680),19:(325,680),20:(225,550),21:(120,485),22:(130,510),
			23:(135,405),24:(135,250)}  #初始化位置数据
	text_font = pygame.font.Font ('C:\Windows\Fonts\simhei.ttf',10)
	for t in range(0,24):
		if list_grid_pool[t].host!=-1:
			text = '玩家' + '%d' % (list_grid_pool[t].host+1) +'-'+'%d'%list_grid_pool[t].level
			text_fmt = text_font.render (text,True,(255-list_grid_pool[t].host*85,list_grid_pool[t].host*85,list_grid_pool[t].host*85))
			screen.blit (text_fmt,(list[t+1]))

def font_x (text):  #文字字体
	text_font = pygame.font.Font ('C:\Windows\Fonts\simhei.ttf',30)
	text_fmt = text_font.render (text,True,(0,0,0))
	return text_fmt

def display_price(screen,number):#显示价格
	text='价格：' + '%d' %number
	text_fmt=font_x(text)
	screen.blit(text_fmt,(550,280))

def display_play_data(screen,play_pool):#显示玩家数据
	number=1
	for t in play_pool:
		text='玩家'+'%d'%number +  ':' + '%d'%play_pool[number-1].money
		text_fmt=font_x(text)
		screen.blit(text_fmt,(250,370+number*30))
		number=number+1

def price_change(play_pool,turn_key): #实现交过路费功能
	play_temp = list_grid_pool[play_pool[turn_key].loction - 1].host  #记录地皮主人
	print('%d'%play_temp)
	money_temp=list_grid_pool[play_pool[turn_key].loction-1].price*(list_grid_pool[play_pool[turn_key].loction-1].level+1)*0.25
	play_pool[play_temp].money=play_pool[play_temp].money + money_temp
	play_pool[turn_key].money=play_pool[turn_key].money - money_temp
	return play_pool

def luncky (screen,turn_key,play_pool,now_location,dice_number,list_player_picture,x,y):#判断抽奖结果
	list = {1:(190,40),2:(325,35),3:(435,35),4:(530,35),5:(630,35),6:(730,35),7:(830,35),8:(945,40),
			9:(985,135),10:(985,270),11:(985,365),12:(985,475),13:(940,550),14:(850,550),15:(760,550),
			16:(650,550),17:(540,550),18:(435,550),19:(330,550),20:(225,550),21:(120,485),22:(120,390),
			23:(120,230),24:(120,115)}  #初始化位置数据
	money=play_pool[turn_key].money
	now_loction=play_pool[turn_key].loction
	t_rand = random.randint (1,20)
	if t_rand <= 10:
		if t_rand <= 5:
			s_rand = random.randint (1,10)
			money = play_pool[turn_key].money - s_rand * 100
			text = '天气渐凉，不慎如病，花费' + '%d' % (s_rand * 100)
			text_fmt = font_x (text)
			screen.blit (text_fmt,(550,280))
			pygame.display.update ()
			time.sleep (1)
		elif t_rand <= 9:
			s_rand = random.randint (5,10)
			money = play_pool[turn_key].money + s_rand * 300
			text = '善哉善哉，化缘所得' + '%d' % (s_rand * 300)
			text_fmt = font_x (text)
			screen.blit (text_fmt,(550,280))
			pygame.display.update ()
			time.sleep (1)
		else:
			if play_pool[turn_key].money<0:
				money = play_pool[turn_key].money+10000
			else:
				money = play_pool[turn_key].money+5000
			text = '贵人相助'
			text_fmt = font_x (text)
			screen.blit (text_fmt,(550,280))
			pygame.display.update ()
			time.sleep (1)
	elif t_rand > 10 and t_rand <= 15:
		turn_key = turn_key - 1
		text = '白龙马我们走，再次行动'
		text_fmt = font_x (text)
		screen.blit (text_fmt,(550,280))
		pygame.display.update ()
		time.sleep (1)
	else:
		s_rand = random.randint (1,24)
		now_loction = s_rand
		text = '被妖风卷走，移动至' + '%d' % s_rand
		text_fmt = font_x (text)
		screen.blit (text_fmt,(550,280))
		pygame.display.update ()
		time.sleep (1)
		x,y = list[s_rand]
		screen.blit (background,(0,0))
		display_play_data (screen,play_pool)
		dice_number_display (screen,dice_number)
		screen.blit (list_player_picture[play_pool[turn_key].character],
					 (x + turn_key * 10,y + turn_key * 20))
		for p in play_pool:
			if p != play_pool[turn_key]:
				screen.blit (list_player_picture[p.character],(p.x,p.y))
		display_player_name_dice (screen,play_pool,x,y,turn_key)
		display_host_name (screen,list_grid_pool)
		pygame.display.update ()
		time.sleep (0.2)
	return (now_loction,money,turn_key,x,y)

def character_grid(screen,turn_key,dice_number,play_pool,list_player_picture):#实现每一格的效果
	list = {1:(190,40),2:(325,35),3:(435,35),4:(530,35),5:(630,35),6:(730,35),7:(830,35),8:(945,40),
			9:(985,135),10:(985,270),11:(985,365),12:(985,475),13:(940,550),14:(850,550),15:(760,550),
			16:(650,550),17:(540,550),18:(435,550),19:(330,550),20:(225,550),21:(120,485),22:(120,390),
			23:(120,230),24:(120,115)}  #初始化位置数据
	x,y=list[play_pool[turn_key].loction]
	now_turn_key=turn_key
	now_loction=play_pool[turn_key].loction
	money=play_pool[turn_key].money
	if list_grid_pool[play_pool[turn_key].loction-1].function==1:#移动效果
		now_loction=play_pool[turn_key].loction + list_grid_pool[play_pool[turn_key].loction-1].move
		if list_grid_pool[play_pool[turn_key].loction-1].move>0:#向前移动效果
			for t in range(play_pool[turn_key].loction+1,now_loction+1):
				x,y = list[t]
				screen.blit (background,(0,0))
				display_play_data (screen,play_pool)
				dice_number_display (screen,dice_number)
				screen.blit (list_player_picture[play_pool[turn_key].character],
							 (x + turn_key * 10,y + turn_key * 20))
				for p in play_pool:
					if p !=play_pool[turn_key]:
						screen.blit (list_player_picture[p.character],(p.x,p.y))
				display_player_name_dice (screen,play_pool,x,y,turn_key)
				display_host_name (screen,list_grid_pool)
				pygame.display.update ()
				time.sleep (0.1)
		elif list_grid_pool[play_pool[turn_key].loction-1].move<0:#向后移动
			t=play_pool[turn_key].loction
			while t>=now_loction:
				x,y = list[t]
				screen.blit (background,(0,0))
				display_play_data (screen,play_pool)
				dice_number_display (screen,dice_number)
				screen.blit (list_player_picture[play_pool[turn_key].character],(x + turn_key * 10,y + turn_key * 20))
				t=t-1
				for p in play_pool:
					if p != play_pool[turn_key]:
						screen.blit (list_player_picture[p.character],(p.x,p.y))
				display_player_name_dice (screen,play_pool,x,y,turn_key)
				display_host_name (screen,list_grid_pool)
				pygame.display.update ()
				time.sleep (0.1)
	elif list_grid_pool[play_pool[turn_key].loction-1].function==2:#地皮
		if list_grid_pool[play_pool[turn_key].loction-1].host==-1:#购买地皮
			if money < list_grid_pool[play_pool[turn_key].loction - 1].price:
				text_money_unenough = font_x ("资金不足")
				screen.blit (text_money_unenough,(500,250))
				pygame.display.update ()
				time.sleep (0.5)
				return(play_pool,list_grid_pool,turn_key)
			screen.blit(land_window,(500,250))
			display_price(screen,list_grid_pool[play_pool[turn_key].loction-1].price)
			pygame.display.update()
			k_window=0
			while True:
				k_window=window_control()
				time.sleep(0.1)
				if k_window==1:
					money=money-list_grid_pool[play_pool[turn_key].loction-1].price
					list_grid_pool[play_pool[turn_key].loction-1].host=turn_key #host=turn_key 即 玩家一为0，玩家二为1...
				if k_window!=0:
					play_temp=list_grid_pool[play_pool[turn_key].loction-1].host  #记录地皮主人
					break
		elif list_grid_pool[play_pool[turn_key].loction-1].host!=-1:#交过路费
			if list_grid_pool[play_pool[turn_key].loction-1].host!=turn_key:
				play_pool=price_change(play_pool,turn_key)
				return(play_pool,list_grid_pool,turn_key)
			elif list_grid_pool[play_pool[turn_key].loction-1].level<3:#升级地皮
				if money < list_grid_pool[play_pool[turn_key].loction - 1].price/4:#判断资金是否够升级
					text_money_unenough = font_x ("升级资金不足")
					screen.blit (text_money_unenough,(500,250))
					pygame.display.update ()
					time.sleep (1)
					return (play_pool,list_grid_pool,turn_key)
				screen.blit (land_window_level,(500,250))
				display_price (screen,list_grid_pool[play_pool[turn_key].loction - 1].price/4)
				pygame.display.update ()
				k_window = 0
				while True:
					k_window = window_control ()
					time.sleep (0.1)
					if k_window == 1:
						list_grid_pool[play_pool[turn_key].loction - 1].level =  list_grid_pool[play_pool[turn_key].loction - 1].level+1
						money=money-list_grid_pool[play_pool[turn_key].loction - 1].price/4
						break

	elif list_grid_pool[play_pool[turn_key].loction-1].function==4:#交税
		money=money-list_grid_pool[play_pool[turn_key].loction-1].tax
	elif list_grid_pool[play_pool[turn_key].loction - 1].function == 3:  #抽奖
		(now_loction,money,now_turn_key,x,y)=luncky(screen,turn_key,play_pool,now_loction,dice_number,list_player_picture,x,y)
	elif list_grid_pool[play_pool[turn_key].loction-1].function==5: #到监狱
		play_pool[turn_key].stop=1
		text = '被妖怪捉走了'
		text_fmt = font_x (text)
		screen.blit (text_fmt,(550,280))
		pygame.display.update ()
		time.sleep (1)

	play_pool[turn_key].x=x+turn_key*10
	play_pool[turn_key].y=y+turn_key*20
	play_pool[turn_key].money=money
	play_pool[turn_key].loction=now_loction
	turn_key = now_turn_key
	return (play_pool,list_grid_pool,turn_key)#返回玩家池及格子池
