#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pygame
import time
import random
from setting import *
from dice import *
from select_character import *
from select_player_number import *
from Grid import * #初始化格子（棋盘）数据
pygame.init()

play_pool = []  #玩家池
list_player_picture = {1:player1_picture,2:player2_picture,3:player3_picture,4:player4_picture}
list_grid_pool=[] #格子池

class Grid (object):
	def __init__(self,grid_data):
		self.function=grid_data[0]#功能（移动1，地皮2，抽奖3，交税4，停留5）
		self.move=grid_data[1]#移动步数或者监狱停留回合数
		self.price=grid_data[2]#地皮价格
		self.level=grid_data[3]#地皮上房屋等级
		self.host=grid_data[4]#地皮拥有者
		self.tax=grid_data[5]#税
		self.luck=grid_data[6]#备用


class Role (object):  #角色数据模板
	def __init__ (self,x,y,name,loction,character,money,stop):
		self.x = x
		self.y = y
		self.name = name  #玩家名字
		self.loction = loction  #玩家所在格子数
		self.character = character  #玩家选择的角色
		self.money = money	#玩家资金
		self.stop = stop  #监狱开关
		#self.skill = skill  #玩家技能（根据所选角色不同而能力不同）开发中

def loction_changer_move (screen,turn_key,list_player_picture,play_pool,list_grid_pool,a,b,dice_number):  #实现位移（一步一移）动画
	list = {1:(190,40),2:(325,35),3:(435,35),4:(530,35),5:(630,35),6:(730,35),7:(830,35),8:(945,40),
			9:(985,135),10:(985,270),11:(985,365),12:(985,475),13:(940,550),14:(850,550),15:(760,550),
			16:(650,550),17:(540,550),18:(435,550),19:(330,550),20:(225,550),21:(120,485),22:(120,390),
			23:(120,230),24:(120,115)}#初始化位置数据
	for t in range (a,b):
		x,y = list[t]
		screen.blit (background,(0,0))
		dice_number_display (screen,dice_number)
		display_play_data (screen,play_pool)
		screen.blit (list_player_picture[play_pool[turn_key].character],
					 (x + turn_key * 10,y + turn_key * 20))
		for p in play_pool:
			if p != play_pool[turn_key]:
				screen.blit (list_player_picture[p.character],(p.x,p.y))
		display_player_name_dice (screen,play_pool,x,y,turn_key)
		display_host_name (screen,list_grid_pool)
		pygame.display.update ()
		time.sleep (0.1)
	return (x,y)

def loction_changer (screen,turn_key,list_player_picture,play_pool,list_grid_pool):  #改变玩家位置并实现位移动画
	money=play_pool[turn_key].money
	dice_gif (screen)  #骰子动画
	dice_number = random.randint (1,6)  #随机得到一个数字
	dice_number_display (screen,dice_number)  #显示骰子
	#time.sleep (0.1)
	last_loction = play_pool[turn_key].loction  #记录上一次位置
	play_pool[turn_key].loction = play_pool[turn_key].loction + dice_number  #玩家位置（格子）
	if play_pool[turn_key].loction > 24:  #判断是否过起点
		play_pool[turn_key].loction = play_pool[turn_key].loction - 24

	if last_loction < play_pool[turn_key].loction:  #判断连续两次位置是否跨一圈
		(x,y)=loction_changer_move (screen,turn_key,list_player_picture,play_pool,list_grid_pool,last_loction,play_pool[turn_key].loction + 1,dice_number)
	elif last_loction > play_pool[turn_key].loction:
		money=money+2000
		(x,y) =loction_changer_move (screen,turn_key,list_player_picture,play_pool,list_grid_pool,last_loction,25,dice_number)
		(x,y) =loction_changer_move (screen,turn_key,list_player_picture,play_pool,list_grid_pool,1,play_pool[turn_key].loction + 1,dice_number)

	play_pool[turn_key].x=x+turn_key*10
	play_pool[turn_key].y=y+turn_key*20
	play_pool[turn_key].money=money
	return (play_pool,dice_number)



def key_control_select ():  #游戏操作——获取按键操作
	k = 0
	x,y = pygame.mouse.get_pos ()
	for event in pygame.event.get ():
		if event.type == pygame.QUIT:
			exit ()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			print ('x=',x)  # 显示鼠标点击位置
			print ('y=',y)
			if x >= 5 and x <= 180 and y >= 185 and y <= 800:
				k = 1
			elif True:
				k = 0
	return k


def key_control_play ():  #开始游戏——获取按键操作
	k = 0
	x,y = pygame.mouse.get_pos ()
	for event in pygame.event.get ():
		if event.type == pygame.QUIT:
			exit ()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			print ('x=',x)  # 显示鼠标点击位置
			print ('y=',y)
			if x >= 300 and x <= 375 and y >= 250 and y <= 330:
				k = 1
			elif True:
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

def end(screen,play_pool,play_number):
	for t in play_pool:  #退出判断
		if t.money > 50000:
			while True:
				clock = pygame.time.Clock ()
				clock.tick (30)
				screen.blit (background_end,(0,0))  # 显示背景
				text_font = pygame.font.Font ('C:\Windows\Fonts\simhei.ttf',30)
				text = '游戏结束'
				text_fmt = text_font.render (text,True,(0,0,0))
				screen.blit (text_fmt,(300,100))
				for t in range (1,play_number + 1):
					text = '玩家' + '%d' % t + ':' + '%d' % play_pool[t - 1].money
					text_fmt = text_font.render (text,True,(0,0,0))
					screen.blit (text_fmt,(300,100 + t * 50))
				pygame.display.update ()
				for event in pygame.event.get ():
					if event.type == pygame.QUIT:
						exit ()
def font_x (text):  #文字字体
	text_font = pygame.font.Font ('C:\Windows\Fonts\simhei.ttf',30)
	text_fmt = text_font.render (text,True,(0,0,0))
	return text_fmt

def display_play_turnkey(screen,turn_key):#显示回合
	t=turn_key+1
	text='玩家'+'%d'%t+'回合'
	text_fmt=font_x(text)
	screen.blit(text_fmt,(250,340))

def display_play_data(screen,play_pool):#显示玩家数据
	number=1
	for t in play_pool:
		text='玩家'+'%d'%number +  ':' + '%d'%play_pool[number-1].money
		text_fmt=font_x(text)
		screen.blit(text_fmt,(250,370+number*30))
		number=number+1

def display_player_name(screen,play_pool):#显示玩家名字
	text_font = pygame.font.Font ('C:\Windows\Fonts\simhei.ttf',15)
	t=0
	for i in play_pool:
		text = text_font.render (i.name,True,(255-t*85,t*85,t*85))
		t=t+1
		screen.blit(text,(i.x-5,i.y-20))

def display_player_name_dice(screen,play_pool,x,y,turn_key):#显示玩家名字
	text_font = pygame.font.Font ('C:\Windows\Fonts\simhei.ttf',15)
	t=0
	for i in play_pool:
		if i!=play_pool[turn_key]:
			text = text_font.render (i.name,True,(255-t*85,t*85,t*85))
			screen.blit(text,(i.x-5,i.y-20))
		else:
			text = text_font.render (play_pool[turn_key].name,True,(255-t*85,t*85,t*85))
			screen.blit (text,(x - 5+turn_key * 10,y - 20+turn_key*20))
		t = t + 1
	display_play_turnkey (screen,turn_key)

def main ():
	screen = pygame.display.set_mode ((1200,800),0,0)
	pygame.display.set_caption ("大富翁")  # 设置标题
	turn_key = 0  #回合控制开关，表示几号玩家
	turn_number = 1  #回合数
	dice_number = 0  #骰子数
	#play_number = 0  #玩家数量
	list_grid_pool=[]
	list_grid_data = {'1':[0,0,0,0,-1,0,0],'2':[2,0,8000,0,-1,0,0],'3':[0,0,0,0,-1,0,0],'4':[3,0,0,0,-1,0,0],
					  '5':[2,0,3000,0,-1,0,0],
					  '6':[2,0,2000,0,-1,0,0],'7':[0,0,0,0,-1,0,0],'8':[2,0,3000,0,-1,0,0],'9':[5,1,0,0,-1,0,0],
					  '10':[2,0,5000,0,-1,0,0],
					  '11':[3,0,0,0,-1,0,0],'12':[1,2,0,0,-1,0,0],'13':[0,0,0,0,-1,0,0],'14':[0,0,0,0,-1,0,0],
					  '15':[2,0,6000,0,-1,0,0],
					  '16':[4,0,0,0,-1,500,0],'17':[3,0,0,0,-1,0,0],'18':[2,0,8000,0,-1,0,0],'19':[2,0,2000,0,-1,0,0],
					  '20':[1,-3,0,0,-1,0,0],
					  '21':[3,0,0,0,-1,0,0],'22':[2,0,4000,0,-1,0,0],'23':[2,0,6000,0,-1,0,0],'24':[2,0,2000,0,-1,0,0]}
	for i in range (1,25):  #初始化格子数据
		list_grid_pool.append (Grid (list_grid_data['%d' % i]))

	#背景音乐
	pygame.mixer.music.play (-1)

	#玩家数量选择
	play_number = select_player_number (screen)#已被封装

	#玩家人物选择
	play_pool = main_select_character (screen,play_number)#已被封装

	while True:  #开始游戏循环

		while True:  # 操作循环
			clock = pygame.time.Clock ()
			clock.tick (30)
			screen.blit (background,(0,0))  # 显示背景
			display_play_turnkey (screen,turn_key)
			for i in range (0,play_number):
				screen.blit (list_player_picture[play_pool[i].character], (play_pool[i].x,play_pool[i].y))  #显示玩家人物
			display_play_data(screen,play_pool)
			display_player_name (screen,play_pool)
			display_host_name (screen,list_grid_pool)
			k_play = key_control_play ()  #检查键盘

			if k_play == 1:
				k_play = 0
				(play_pool,dice_number) = loction_changer (screen,turn_key,list_player_picture,play_pool,list_grid_pool)  #改变玩家位置
				first_location=play_pool[turn_key].loction
				first_turn_key=turn_key
				(play_pool,list_grid_pool,turn_key)=character_grid (screen,turn_key,dice_number,play_pool,list_player_picture) #判断位置所在的功能
				while (1):
					if first_turn_key>turn_key:
						turn_key=turn_key+1
						(play_pool,dice_number) = loction_changer (screen,turn_key,list_player_picture,play_pool,
																   list_grid_pool)  #改变玩家位置
					if first_location!=play_pool[turn_key].loction:
						first_location = play_pool[turn_key].loction
						(play_pool,list_grid_pool,turn_key) = character_grid (screen,turn_key,dice_number,play_pool,
																				list_player_picture)  #判断位置所在的功能
					else:
						break
					time.sleep(0.01)
				t = turn_key + 1
				e = 1#记录接下来有几人在监狱
				if play_pool[(t) % play_number].stop == 1:
					play_pool[(t) % play_number].stop = 0
					e = e + 1
					while True:
						t = t + 1
						if play_pool[(t) % play_number].stop == 1:
							play_pool[(t) % play_number].stop = 0
							e = e + 1
						else:
							break
					turn_key = (turn_key + e) % play_number  #回合记录器
				else:
					turn_key = turn_key + 1  # 回合记录器

			dice_number_display (screen,dice_number)  #显示骰子
			pygame.display.update ()

			end(screen,play_pool,play_number)#判断游戏结束

			if turn_key == play_number:  #回合结束判断
				turn_number = turn_number + 1
				turn_key = 0
				break

if __name__ == '__main__':
	main ()
