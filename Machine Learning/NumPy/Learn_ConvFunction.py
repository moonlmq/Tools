# -*- coding:utf-8 -*-
########################
#便捷函数
########################

import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

bhp = np.loadtxt('BHP.csv',delimiter=',',usecols=(6,),unpack=True)
bhp_returns = np.diff(bhp) / bhp[:-1]
vale = np.loadtxt('VALE.csv',delimiter=',',usecols=(6,),unpack=True)
vale_returns = np.diff(vale) / vale[:-1]

#协方差
print u"计算协方差"
covariance = np.cov(bhp_returns,vale_returns)
print "Convariance", covariance
#diagonal函数和trace函数可以给出矩阵的对角线元素和矩阵的迹
print "Covariance diagonal", covariance.diagonal()
print "Covariance trace", covariance.trace()
#corrcoef可以计算相关系数
print "Correlation coefficient",np.corrcoef(bhp_returns,vale_returns)

#多项式拟合
print u"多项式拟合"
#polyfit函数可以用多项式去拟合一系列数据点，无论这些数据点是否来自
#连续函数都适用
t = np.arange(len(bhp))
poly = np.polyfit(t,bhp-vale,5)
print "Polynomial fit", poly
#使用roots函数可以找到拟合的多项式函数什么时候到达0值,即解出多项式的根
print "Roots",np.roots(poly)
#polyder函数可以对多项式函数求导
der = np.polyder(poly)
print "Derivative",der
#polyval可以计算多项式函数的值
vals = np.polyval(poly,t)
print "polyval",vals
#使用argmax和argmin找出最大值点和最小值点
print "argmax",np.argmax(vals)
print "argmin",np.argmin(vals)

#波动
print u"波动"
c,v = np.loadtxt('BHP.csv',delimiter=',',usecols=(6,7),unpack=True)
change = np.diff(c)
print "Change",change
#sign函数可以返回数组中每个元素的正负符号
signs = np.sign(change)
print "Signs",signs
#piecewise函数可以分段给定取值
pieces = np.piecewise(change,[change<0, change>0],[-1,1])
print "Pieces",pieces
print "Arrays equal?", np.array_equal(signs,pieces)


#避免使用循环
print u"避免使用循环"
o,h,l,c = np.loadtxt('BHP.csv',delimiter=',',usecols=(3,4,5,6),unpack=True)
#vectorize函数相当于python的map函数
def calc_profit(open,high,low,close):
	buy = open*(90)

	if low < buy<high:
		return (close-buy)/buy
	else:
		return 0

func = np.vectorize(calc_profit)
profits = func(o,h,l,c)
print "Profits",profits

#hanning函数是一个加权余弦的窗函数
print u"使用hanning函数平滑数据"
N =10
weights= np.hanning(N)
print "Weights",weights