#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import pygame
import time
from setting import *
def dice_gif(screen):#骰子动画
	list=[dice1,dice2,dice3,dice4,dice5,dice6,dice7,dice8]
	for x in range(0,1):
		for t in list:
			screen.blit(t,(290,250))
			pygame.display.update()
			time.sleep(0.08)


def dice_number_display(screen,dice_number):
	list={'0':dice_1,'1':dice_1,'2':dice_2,'3':dice_3,'4':dice_4,'5':dice_5,'6':dice_6}
	screen.blit (list['%d'%dice_number],(290,250))
	pygame.display.update()
