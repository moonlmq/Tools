# -*-coding:utf-8 -*-
import pygame, sys
from pygame.locals import *
import numpy as np
# pygame.surfarray.array2d(img) 该函数将像素数据存入一个二维数组
# pygame.surfarray.blit_array(screen, new_pixels) 该函数将数组中的像素呈现在屏幕上
pygame.init()
img = pygame.image.load('head.jpg')
pixels = pygame.surfarray.array2d(img)
x = pixels.shape[0]*7
y = pixels.shape[1]*7
screen = pygame.display.set_mode((x,y))
pygame.display.set_caption("Surfarray Demo")
new_pixels = np.tile(pixels,(7,7)).astype(int)

while True:
	screen.fill((255,255,255))
	pygame.surfarray.blit_array(screen,new_pixels)

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()