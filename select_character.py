#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import pygame
import time
from setting import *
pygame.init ()
player_pool=[]

class Role(object):#角色数据模板
	def __init__(self,x,y,name,loction,character,money,stop):
		self.x=x
		self.y=y
		self.name=name
		self.loction=loction
		self.character=character
		self.money=money
		self.stop = stop  #监狱开关
def display_select_character(screen):
	screen.fill((255,255,255))
	screen.blit(select_character_picture,(0,0))

def key_control_select ():  #人物选择——获取按键操作
	k = 0
	x,y = pygame.mouse.get_pos ()
	for event in pygame.event.get ():
		if event.type == pygame.QUIT:
			exit ()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			print ('x=',x)  # 显示鼠标点击位置
			print ('y=',y)
			if x >= 120 and x <= 280 and y >= 140 and y <= 440:
				k = 1
			elif x >= 280 and x <= 535 and y >= 20 and y <= 435:
				k = 2
			elif x >= 540 and x <= 730 and y >= 90 and y <= 465:
				k = 3
			elif x >= 735 and x <= 890 and y >= 145 and y <= 435:
				k = 4
			elif True:
				k = 0
	return k

def select_character_move1 (screen,num):  #选择人物时的动画1，用于图片上出现对勾
	if num == 1:
		screen.blit (center,(200,140))
	elif num == 2:
		screen.blit (center,(390,50))
	elif num == 3:
		screen.blit (center,(600,90))
	elif num == 4:
		screen.blit (center,(770,140))

def select_character_move2 (screen,num1,num2):  #选择人物时动画2，在屏幕上显示第num1个人选了第num2个角色的结果
	list = {'1':player1_picture,'2':player2_picture,'3':player3_picture,'4':player4_picture}
	screen.blit (list['%d' % num2],(1100,num1 * 150))

def font_x (text):  #文字字体
	text_font = pygame.font.Font ('C:\Windows\Fonts\simhei.ttf',50)
	text_fmt = text_font.render (text,True,(0,0,0))
	return text_fmt

def nameprint (screen,n):  #在屏幕上打印游戏玩家名称
	for i in range (1,n + 1):
		text = '玩家' + '%d' % i
		screen.blit (font_x (text),(980,i * 150))

def playerarrow (screen,n):  #随着玩家选择移动的箭头
	screen.blit (arrow,(900,n * 150))

def main_select_character (screen,number_x):
	array = [[1,0],[2,0],[3,0],[4,0],[5,0]]  #若x个角色，则使用x+1行数据，
	# 最多四人则矩阵为五行两列，若想进行扩展可以把array赋值成[number_x+1][2]的数组。switch数组类似
	n_temp = 0
	switch = [[0,0],[0,0],[0,0],[0,0]]
	number = number_x
	number_save = number_x

	while True:  #人物选择循环
		display_select_character (screen)  #展示出选择角色界面
		nameprint (screen,number_save)  #显示玩家123的名字所在位置
		playerarrow (screen,n_temp + 1)  # 玩家选择时用一个箭头指示
		#默认从玩家一，开始选择
		#开关改变的时候轮换至下一个玩家

		k_play = key_control_select ()  #返回屏幕上选择的角色序号
		if k_play == 1:
			switch[0][0] = 1
		elif k_play == 2:
			switch[1][0] = 1
		elif k_play == 3:
			switch[2][0] = 1
		elif k_play == 4:
			switch[3][0] = 1
		if switch[0][0] == 1:
			select_character_move1 (screen,1)
		if switch[1][0] == 1:
			select_character_move1 (screen,2)
		if switch[2][0] == 1:
			select_character_move1 (screen,3)
		if switch[3][0] == 1:
			select_character_move1 (screen,4)

		if k_play != 0:  #主要数据变化之一，用于结束程序和判断循环次数
			i = 0
			while switch[i][0] != 1 or switch[i][1] != 0:
				i = i + 1
				if i > 3:
					break
			if i <= 3:
				array[n_temp][1] = i + 1
				switch[i][1] = 1
			if array[n_temp][1] != 0:
				number = number - 1
				n_temp = n_temp + 1
		for i in range (0,4):  #进行数组遍历，找到选择了角色的玩家并将相应的角色图片贴在玩家姓名位置
			if array[i][1]:
				select_character_move2 (screen,i + 1,array[i][1])
		pygame.display.update ()
		if number == 0:
			time.sleep (0.2)
			for i in range (0,number_x):
				role = Role (190 + 10 * i,40 + 20 * i,'玩家' + '%d' % (i + 1),1,array[i][1],10000,0)
				player_pool.append (role)
			return player_pool  #若number等于零，则说明玩家都已经选择完毕，跳出循环
		time.sleep (0.1)

if __name__=="__main__":
	screen=pygame.display.set_mode((1200,800),0,0)
	main_select_character (screen,4)
