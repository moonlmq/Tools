# -*- coding: utf-8 -*-
from math import sqrt

#一个涉及影评者及其对几部电影评分情况的字典
critics ={'Lisa Rose':{'Lady in the Water':2.5,'Snakes on a Plane':3.5,
'Just My Luck':3.0, 'Superman Return':3.5, 'You,Me and Dupree': 2.5,
'The Night Listener': 3.0},
'Kobe Byrant':{'Lady in the Water':3.0,'Snakes on a Plane':3.5,
'Just My Luck':1.5, 'Superman Return':5.0, 'You,Me and Dupree': 3.5,
'The Night Listener': 3.0},
'Allen Iverson':{'Lady in the Water':2.5,'Snakes on a Plane':3.0,
'Superman Return':3.5, 'You,Me and Dupree': 2.5,'The Night Listener': 4.0},
'Jack Rose':{'Snakes on a Plane':3.5,
'Just My Luck':3.0, 'Superman Return':4.0, 'The Night Listener': 4.5},
'Andraw Jone':{'Lady in the Water':3.0,'Snakes on a Plane':4.0,
'Just My Luck':2.0, 'Superman Return':3.0, 'You,Me and Dupree': 2.0,
'The Night Listener': 3.0},
'Stanson Curry':{'Lady in the Water':3.0,'Snakes on a Plane':4.0,
'Superman Return':5.0, 'You,Me and Dupree': 1.0,'The Night Listener': 3.0},
'Toby':{'Snakes on a Plane':4.5,'Superman Return':4.0, 'You,Me and Dupree': 1.0}}

################################
#欧几里得相似度
################################

#返回一个有关person1与person2的基于距离的相似度评价
def sim_distance(prefs,person1,person2):
	#得到shared_items的列表
	si = {}
	for item in prefs[person1]:
		if item in prefs[person2]:
			si[item] = 1

	#如果两者没有共同之处，则返回0
	if len(si) == 0 :return 0

	#计算所有差值的平方和
	sum_of_squares = sum([pow(prefs[person1][item]-prefs[person2][item],2)
		for item in prefs[person1] if item in prefs[person2]])
	return 1/(1+sqrt(sum_of_squares))



#################################
#皮尔逊相关度评价
#################################

#返回p1和p2的皮尔逊相关系数
def sim_pearson(prefs,p1,p2):
	# 得到双方都曾评价过的物品列表
	si={}
	for item in prefs[p1]:
		if item in prefs[p2]: si[item]=1

	n =len(si)
	
	#如果没有共同之处则返回1
	if n == 0 : return 1

	#对所有偏好求和
	sum1 = sum([prefs[p1][it] for it in si])
	sum2 = sum([prefs[p2][it] for it in si])

	#求平方和
	sum1Sq = sum([pow(prefs[p1][it],2) for it in si])
	sum2Sq = sum([pow(prefs[p2][it],2) for it in si])

	#求乘积之和
	pSum = sum(prefs[p1][it]*prefs[p2][it] for it in si)

	#计算皮尔逊评价值
	num = pSum-(sum1*sum2/n)
	den = sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
	if den == 0 : return 0

	r=num/den

	return r


#从反映偏好的字典中返回最匹配者
#返回结果的个数和相似度函数均为可选参数
def topMatches(prefs,person,n=5,similarity=sim_pearson):
	score = [(similarity(prefs,person,other),other)
		for other in prefs if other != person]

	#对列表进行排序，评价值最高者排在最前面
	score.sort()
	score.reverse()
	return score[0:]