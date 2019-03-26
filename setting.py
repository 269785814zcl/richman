#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pygame
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

pygame.init()  # 游戏初始化
pygame.mixer.init()  # 混音器初始化
pygame.mixer.music.load(os.path.join(BASE_DIR, "richman/material/xiyouji.wav"))
pygame.mixer.music.set_volume(0.2)

background = pygame.image.load ("material/background3.jpg")#开始游戏背景

background_end = pygame.image.load ("material/background_end.jpg")#结束游戏背景

player1_picture= pygame.image.load ("material/player1_1.png")#玩家
player2_picture = pygame.image.load ("material/player2_1.png")
player3_picture = pygame.image.load ("material/player3_1.png")
player4_picture = pygame.image.load ("material/player4_1.png")

center=pygame.image.load ("material/right.png")

arrow=pygame.image.load ("material/arrow.png")

dice_1 = pygame.image.load ("material/dice_1.png")#骰子
dice_2 = pygame.image.load ("material/dice_2.png")
dice_3 = pygame.image.load ("material/dice_3.png")
dice_4 = pygame.image.load ("material/dice_4.png")
dice_5 = pygame.image.load ("material/dice_5.png")
dice_6 = pygame.image.load ("material/dice_6.png")

dice1 = pygame.image.load ("material/dice1.png")
dice2 = pygame.image.load ("material/dice2.png")
dice3 = pygame.image.load ("material/dice3.png")
dice4 = pygame.image.load ("material/dice4.png")
dice5 = pygame.image.load ("material/dice5.png")
dice6 = pygame.image.load ("material/dice6.png")
dice7 = pygame.image.load ("material/dice7.png")
dice8 = pygame.image.load ("material/dice8.png")

select_character_picture=pygame.image.load("material/timg2.jpg")#选择人物

select_player_number_picture=pygame.image.load("material/select_player_number1.jpg")#选择玩家数量

land_window=pygame.image.load("material/land_window1.png")#地皮购买
land_window_level=pygame.image.load("material/land_window_level.png")#地皮升级
