# -*-coding:utf-8 -*-

#计算两个数的最大公约数

def calCommonDivisor(a,b):
	result = 0
	if (a == 0 ) or ( b == 0):
		print u"0没有公约数"
		result = None
		return result
	temp = b
	while (temp != 0):
		if (a>b):
			temp = a%b
		else :
			temp = b%a
		if temp ==1:
			print u"该两个数没有公约数"
			result = None
			return result
		if temp == 0:
			print u"最大公约数为:"+ str(min(a,b))
			return min(a,b)
		a = min(a,b)
		b = temp

calCommonDivisor(125,320)
