# -*-coding:utf-8 -*-
# mpl.use("Agg") 该函数指定使用非交互式后端
# plt.figure(figsize=[3, 3]) 该函数创建一个大小为3 × 3平方英寸的图像
# agg.FigureCanvasAgg(fig) 该函数在非交互模式下创建一个画布
# canvas.draw() 该函数在画布上进行绘制
# canvas.get_renderer() 该函数获取画布的渲染器


import pygame, sys
from pygame.locals import *
import numpy as np
import matplotlib as mpl
#use函数必须在引入matplotlib主模块后并引入其他matplotlib模块前立即调用
mpl.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg

fig = plt.figure(figsize=[3,3])
ax = fig.add_subplot(111)
canvas = agg.FigureCanvasAgg(fig)

def plot(data):
	ax.plot(data)
	canvas.draw()
	renderer = canvas.get_renderer()
	raw_data = renderer.tostring_rgb()
	size = canvas.get_width_height()

	return pygame.image.fromstring(raw_data,size,"RGB")


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((400,400))

pygame.display.set_caption('Animating Objects')
img = pygame.image.load('head.jpg')

steps = np.linspace(20,360,40).astype(int)
print "steps",steps
right = np.zeros((2,len(steps)))
print "right",right
down = np.zeros((2,len(steps)))
left = np.zeros((2,len(steps)))
up = np.zeros((2,len(steps)))
#[::-1]可以获得倒序的数组元素
right[0] = steps
print "right[0]",right[0]
right[1] = 20
print "right",right

down[0] = 360
down[1] = steps

left[0] = steps[::-1]
left[1] = 360

up[0] = 20
up[1] = steps[::-1]

pos = np.concatenate((right.T, down.T, left.T, up.T))
print "pos",pos
i = 0

while True:
	#清屏
	screen.fill((255,255,255))

	if i >=len(pos):
		i=0

	screen.blit(img,pos[i])
	i += 1

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
	clock.tick(30)










