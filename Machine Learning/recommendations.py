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

#利用所有他人评价值的加权平均，为某人提供建议
def getRecommendations(prefs,person,similarity=sim_pearson):
	totals={}
	simSums={}
	for other in prefs:
		if other == person : continue
		sim = similarity(prefs,person,other)



		#忽略评价值为零或小于零的情况
		if sim<=0: continue
		for item in prefs[other]:

			#只对还未曾看过的的影片进行评价
			if item not in prefs[person] or prefs[person][item]==0:
				#相似度*评价值
				totals.setdefault(item,0)
				totals[item]+=prefs[other][item]*sim
				#相似度之和
				simSums.setdefault(item,0)
				simSums[item]+=sim

	#建立一个归一化的列表
	rankings = [(total/simSums[item],item) for item, total in totals.items()]

	#返回经过排序的列表
	rankings.sort()
	rankings.reverse()
	return rankings

#将物品与人员对调
def transformPrefs(prefs):
	result={}
	for person in prefs:
		for item in prefs[person]:
			result.setdefault(item,{})

			result[item][person]=prefs[person][item]
	return result


##########################
#基于物品的过滤
##########################
def calculateSimilarItems(prefs,n=10):
	#建立字典，以给出与这些物品最为相近的所有其他物品
	result={}

	#以物品为中心对偏好矩阵实施倒置处理
	itemPrefs=transformPrefs(prefs)
	c=0
	for item in itemPrefs:
		#针对大数据集更新状态变量
		c+=1
		if c%100==0: print "%d / %d" % (c,len(itemPrefs))
		#寻找最为相近的物品
		scores= topMatches(itemPrefs,item,n=n,similarity=sim_distance)
		result[item]=scores
	return result


def getRecommendedItems(prefs,itemMatch,user):
	userRatings=prefs[user]
	scores={}
	totalSim={}

	#循环遍历由当前用户评分的物品
	for (item,rating) in userRatings.items():

		#循环遍历与当前物品相近的物品
		for (similarity,item2) in itemMatch[item]:

			#如果该用户已经对当前物品做过评价，则将其忽略
			if item2 in userRatings : continue

			#评价值与相似度的加权之和
			scores.setdefault(item2,0)
			scores[item2]+=similarity*rating

			#全部相似度之和
			totalSim.setdefault(item2,0)
			totalSim[item2]+=similarity

		#将每个合计值除以加权和，求出平均值
		rankings=[(score/totalSim[item],item) for item,score in scores.items()]

		#按最高值到最低值的顺序，返回评分结果
		rankings.sort()
		rankings.reverse()
		return rankings