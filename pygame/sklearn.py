#-*-coding:utf-8-*-
# sklearn.cluster.AffinityPropagation().fit(S) 该函数创建AffinityPropagation对象并根据关联矩阵
# 进行聚类
# pygame.draw.polygon(screen, (255, 0,0), polygon
# points[i])
# 该函数根据指定的Surface对象、颜色（在本例中为红色）
# 和数据点列表绘制多边形
import numpy as np
import sklearn.cluster
import pygame, sys
import pygame.locals import *
#在400 × 400像素的方块内随机生成30个坐标点
positions = np.random.randint(0,400,size=(30,2))
# 使用欧氏距离（Euclidean distance）来初始化关联矩阵
positions_norms = np.sum(positions ** 2,axis = 1)
S = - positions_norms[:,np.newaxis] - positions_norms[np.newaxis,:]+\
2*np.dot(positions,positions.T)
# 结果提供给AffinityPropagation类。该类将为每一个数据点标记合适的
# 聚类编号。
aff_pro = sklearn.cluster.AffinityPropagation().fit(S)
labels = aff_pro.labels_
polygon_points = []

for i in xrange(max(labels)+1):
	polygon_points.append([])

for i in xrange(len(labels)):
	polygon_points[labels[i]].append(positions[i])
pygame.init()
screen = pygame.display.set_mode((400,400))

while True:
	for i in xrange(len(polygon_points)):
		pygame.draw.polygon(screen,(255,0,0),polygon_points[i])

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()