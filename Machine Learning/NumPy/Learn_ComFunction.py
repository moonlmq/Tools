# -*- coding:utf-8 -*-
#########################
#numpy常用函数
#########################

import numpy as np
#数据存在data.csv中，设置分隔符为，。usecols为一个元组，以获取7，8字段数据
#unpack设置为True，意思是分拆储存不同列的数据，即分别将两个数组值赋值给c和v
c,v = np.loadtxt('data.csv',delimiter=',',usecols=(6,7),unpack=True)


print u"计算平均值"
print c
print v
#加权平均值
vwap = np.average(c,weights=v)
print "vwap = ",vwap
#算数平均值
print "mean = ",np.mean(c)

print
print u"最大值和最小值"
h,l =np.loadtxt('data.csv',delimiter=',',usecols=(5,6),unpack=True)
print "highest = ",np.max(h)
print "lowest = ",np.min(l)
print u"ptp函数计算极差"
print "Spread high price ",np.ptp(h)
print "Spread low price ",np.ptp(l)

print 
c = np.loadtxt('data.csv',delimiter=',',usecols=(6,),unpack=True)
print u"排序"
sorted_close = np.msort(c)
print "msort = ", sorted_close
N = len(c)
#N为奇数
print "middle = ", sorted_close[(N-1)/2]
#N为偶数
#print "average middle = ", (sorted_close[N/2]+sorted_close[(N-1)/2])/2
print u"计算中位数"
print "median = ", np.median(c)
print u"计算方差"
print "variance = ",np.var(c)
print "variance from definition = ",np.mean((c-c.mean())**2)

print u"diff函数可以返回一个由相邻元素差值构成的数组"
a=np.arange(10)
b= np.diff(a)
print "diff array is ", b
print "标准差"
print "Standard deviation = ", np.std(a)
print u"log求对数"
print "log = ", np.log(a)

print u"where函数可以根据指定条件返回所有满足条件的数组元素索引值"
posretindices = np.where(np.log(a)>1)
print "Indices with bigger than 1 is", posretindices


print u"python中整数和浮点数的除法运算机制不同，必须用浮点才能得到正确结果"
print np.sqrt(1./12.)


#日期分析
print u"分析日期数据"
from datetime import datetime
def datestr2num(s):
	return datetime.strptime(s,"%d-%m-%Y").date().weekday()
#converters是数据列和转换函数之间进行映射的字典
dates,close = np.loadtxt('data.csv',delimiter=',',usecols=(1,6),converters={1:datestr2num},unpack=True)
print "Dates =", dates

dates,open,high,low,close = \
np.loadtxt('data.csv',delimiter=',',usecols=(1,3,4,5,6),converters={1:datestr2num},unpack=True)
close = close[:4]
datess = dates[:4]
#找到第一个星期一
first_monday = np.ravel(np.where(dates == 0))[0]
print "The first Monday index is", first_monday
#找到最后个星期五
last_friday = np.ravel(np.where(dates == 4))[-2]
print "The last Monday index is", last_friday
weeks_indices = np.arange(first_monday,last_friday+1)
print "Week indice initial",weeks_indices
#apply_along_axis函数会调用另外一个由我们给出的函数，作用于每个数组元素上
# take函数根据索引值获取元素的值
#save将数据保存文件
#maximum可以挑选多个数组每个元素位置上的最大值
#savetxt("week.csv",week,delimiter=",",fmt="%s")
# a= np.arange(15)
# a = np.split(a,5)
# print a
# b= np.arange(15)
# b = np.split(b,5)
# print b
# def sumex(a,b):
# 	return "do",a,b
# c = np.apply_along_axis(sumex,1,a,b)

# print "aply_along_axis sum is",c

#移动平均线卷积是分析数学中一种重要的运算，
#定义为一个函数与经过翻转和平移的另
#一个函数的乘积的积分。
from matplotlib.pyplot import plot
from matplotlib.pyplot import show
print u"计算简单移动平均线"
N = 5
#ones函数创建一个长度为N的元素均初始化为1的数组
#然后数组除以N，即可得权重
weights=np.ones(N)/N
print "Weights",weights

c=np.loadtxt('data.csv',delimiter=',',usecols=(6,),unpack=True)
sma = np.convolve(weights,c)[N-1:-N+1]
t = np.arange(N-1,len(c))
# plot(t,c[N-1:],lw=1.0)
# plot(t,sma,lw=2.0)
# show()

# exp函数可以计算每个数组元素的指数
x = np.arange(2,5)
print x
print "exp", np.exp(x)
#linspace函数可以返回一个元素值在指定的范围内均匀分布的数组
print "Linspace",np.linspace(-1,0,4)


#fill函数可以将数组元素的值全部设置为一个指定的标量值
a= np.zeros(N)
a.fill(x[0])
print a

#线性模型
print u"线性模型"
b=x[::-1]
print "b",b
A=np.zeros((3,3),float)
print "Zeros N by N",A
for i in range(3):
	A[i,]= x[i]
print "A",A

#linalg包中的lstsq函数可以得到系数向量x，残差数组，A的秩以及A的奇异值
(x,residuals,rank,s) = np.linalg.lstsq(A,b)
print x,residuals,rank,s

#趋势线
print u"趋势线"
#绘制趋势线
h,l,c =np.loadtxt('data.csv',delimiter=',',usecols=(4,5,6),unpack=True)
pivots=(h+l+c) /3
print "Pivots",pivots
#定义一个函数用直线y=at+b来拟合数据，函数返回系数a和b
def fit_line(t,y):
	print "ones_like",np.ones_like(t)
	A=np.vstack([t,np.ones_like(t)]).T
	print A
	return np.linalg.lstsq(A,y)[0]

t = np.arange(len(c))
sa, sb =fit_line(t,pivots-(h-l))
print "sa",sa
print "sb",sb
ra, rb = fit_line(t,pivots+(h-l))
support = sa*t+sb
resistance = ra*t +rb

condition = (c>support) &(c<resistance)
print "Condition",condition
between_bands =np.where(condition)
print support[between_bands]
print c[between_bands]
print resistance[between_bands]
between_bands = len(np.ravel(between_bands))
print "Number points between bands",between_bands
print "Ratio between bands",float(between_bands)/len(c)
print "Tomorrows support",sa*(t[-1]+1)+sb
print "Tomorrows resistance",ra*(t[-1]+1)+rb

#数组的修剪和压缩
print u"数组的修剪和压缩"
#clip方法返回一个修剪过的数组，也就是将所有比给定最大值还大的元素
#全部设为给定的最大值，而所有比给定最小值还小的元素全部设为给定的
#最小值
a = np.arange(5)
print "a=",a
print "Clipped",a.clip(1,2)

#compress方法返回一个根据给定条件筛选后的数组
print "Compressed",a.compress(a>2)

#阶乘
print u"阶乘"
#prod方法可以计算数组所有元素的乘积
b=np.arange(1,9)
print "b=",b
print "Factorial",b.prod()
#cumprod可以知道所有阶乘值
print "Factorials",b.cumprod()