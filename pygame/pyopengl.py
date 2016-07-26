# -*-coding:utf-8 -*-
# pygame.display.set_mode((w,h),
# pygame.OPENGL|pygame.DOUBLEBUF)
# 该函数将显示模式设置为指定的宽度、高度和OpenGL对
# 应的显示类型
# glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) 该函数使用掩码清空缓冲区。在本例中，我们清空的是颜
# 色和深度缓冲区
# glu0rtho2D(0, w, 0, h) 该函数根据上、下、左、右的裁切平面坐标定义一个2D
# 的正交投影矩阵
# glColor3f(1.0, 0, 0) 该函数根据三个浮点数表示的RGB颜色来设置当前的绘
# 图颜色。在本例中为红色
# glBegin(GL_P0INTS) 该函数限定一组或多组图元的定点定义
# glVertex2fv(point) 该函数根据一个顶点产生一个点
# glEnd() 该函数结束以glBegin开始的代码段
# glFlush() 该函数强制刷新缓冲区，执行绘图命令
import pygame
from pygame.locals import *
import numpy as np

from OpenGL.GL import *
from OpenGL.GLU import *

def display_openGL(w,h):
	pygame.display.set_mode((w,h),pygame.OPENGL|pygame.DOUBLEBUF)

	glClearColor(0.0,0.0,0.0,1.0)
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

	glu0rtho2D(0,w,0,h)

def main():
	pygame.init()
	pygame.display.setcaption('OpenGL Demo')
	DIM = 400
	display_openGL(DIM,DIM)
	glColor3f(1.0,0,0)
	vertices = np.array([[0,0],[DIM/2,DIM],[DIM,0]])
	NPOINTS = 9000
	indices = np.random.random_integers(0,2,NPOINTS)
	point = [175.0,150.0]

	for i in xrange(NPOINTS):
		glBegin(GL_POINTS)
		point = (point+vertices[indices[i]])/2.0
		glVertex2fv(point)
		glEnd()

	glFlush()
	pygame.display.flip()

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				return

if __name__ == '__main__':
	main()