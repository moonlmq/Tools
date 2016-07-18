# - *-coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
#以自然数序列作为多项式的系数，使用poly1d函数创建多项式
func = np.poly1d(np.array([1,2,3,4]).astype(float))
#使用derive函数和参数m为几阶导数
func1 = func.deriv(m=1)
func2 = func.deriv(m=2)
x = np.linspace(-10,10,30)
y = func(x)
y1 = func1(x)
y2=func2(x)
#subplot可以创建子图.该函数的第一个参数是子图的行数，第二个参数是
#子图的列数，第三个参数是一个从1开始的序号。另一个方式是将这3个
#参数结合成一个字，如311，这样子图将组织成3行1列。
plt.subplot(311)
plt.plot(x,y,'r-')
plt.title("Polynomial")
plt.subplot(312)
plt.plot(x,y1,'b-')
plt.title('First Derivative')
plt.subplot(313)
plt.plot(x,y2,'go')
plt.title("Second Derivative")
plt.xlabel('x')
plt.ylabel('y')
#plot可以画出不同风格的图
# plt.plot(x,y,'ro',x,y1,'g--')
#添加x,y轴标签
# plt.xlabel('x')
# plt.ylabel('y(x)')
# plt.show()

print u"财经"
#matplotlib.finance包中函数可以从雅虎下载股票数据，并绘制成K线图
from matplotlib.dates import DateFormatter
from matplotlib.dates import DayLocator
from matplotlib.dates import MonthLocator
from matplotlib.finance import quotes_historical_yahoo
from matplotlib.finance import candlestick
import sys
from datetime import date

print u"K线图"
today = date.today()
start = (today.year -1,today.month,today.day)
#创建定位器，可以在x轴上定位月份和日期
alldays = DayLocator()
months = MonthLocator()
#创建一个日期格式化器以格式化x轴上的日期。
#该格式化器将创建一个字符串，包含间歇的月份和年份
month_formatter = DateFormatter("%b %y")
#下载数据
symbol = 'DISH'
quotes = quotes_historical_yahoo(symbol,start,today)
#创建一个matplotlib的figure对象，这是绘图组件的顶层容器
fig = plt.figure()
#增加一个子图
ax = fig.add_subplot(111)
#将x轴上的主定位器设置为月定位器，该定位器负责x轴上较粗的刻度
ax.xaxis.set_major_locator(months)
# 将x轴上的次定位器设置为日定位器。负责x轴上较细的刻度
ax.xaxis.set_minor_locator(alldays)
#将x轴上的主格式化器设置为月格式化器，负责x轴上较粗的标签
ax.xaxis.set_major_formatter(month_formatter)
#candlestick画k线图，可以指定矩形宽度
candlestick(ax,quotes)
fig.autofmt_xdate()
# plt.show()


print u"直方图"
# #hist函数可以绘制直方图
quotes = np.array(quotes)
# print quotes
close = quotes.T[4]
# print close
# plt.hist(close,np.sqrt(len(close)))
# plt.show()
print u"对数坐标图"
volume = quotes.T[5]
#plt.semilogy(dates,volume)
ret = np.diff(close)/close[:-1]
volchange = np.diff(volume)/volume[:-1]
fig = plt.figure()
ax = fig.add_subplot(111)
print u"散点图"
ax.scatter(ret,volchange,c = ret*100,s=volchange*100,alpha=0.5)
ax.set_title('Close and volume returns')
ax.grid(True)
# plt.show()

print u"着色"
fig = plt.figure()
dates = quotes.T[0]
ax = fig.add_subplot(111)
ax.plot(dates,close)
plt.fill_between(dates,close.min(),close,where=close>close.mean(),facecolor="green",alpha=0.4)
plt.fill_between(dates,close.min(),close,where=close<close.mean(),facecolor="red",alpha=0.4)
# plt.show()

print u"图例和注释"
#legend函数可以创建透明的图例，由matplotlib自动确定其摆放位置
#可以用annotate函数在图像上精确地添加注释，并有很多可选的注释和箭头风格。
fig = plt.figure()
ax = fig.add_subplot(111)

emas = []
for i in range(9,18,3):
	weights = np.exp(np.linspace(-1.,0,i))
	weights /= weights.sum()

	ema = np.convolve(weights,close)[i-1:-i+1]
	idx = (i-6)/3
	ax.plot(dates[i-1:],ema,lw=idx,label="EMA(%s)" % (i))
	data = np.column_stack((dates[i-1:],ema))
	emas.append(np.rec.fromrecords(data,names=["dates","ema"]))

first = emas[0]["ema"].flatten()
second = emas[1]["ema"].flatten()
bools = np.abs(first[-len(second):]-second)/second <0.0001
xpoints = np.compress(bools,emas[1])

for xpoint in xpoints:
	ax.annotate('x',xy=xpoint,textcoords='offset points',\
		xytext=(-50,30),arrowprops=dict(arrowstyle="->"))


leg = ax.legend(loc='best',fancybox=True)
leg.get_frame().set_alpha(0.5)

ax.plot(dates,close,lw=1.0,label="Close")
ax.xaxis.set_major_locator(months)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(month_formatter)
ax.grid(True)
fig.autofmt_xdate()
# plt.show()

print u"三维绘图"
#3D作图需要一个和三维投影相关的Axes3D对象
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
fig=plt.figure()
#使用3d关键字指定图像的三维投影
ax = fig.add_subplot(111,projection='3d')
# 使用meshgrid函数创建一个二维左边网格，用于x，y赋值
u = np.linspace(-1,1,100)
x,y = np.meshgrid(u,u)
z = x**2 + y**2
#指定行和列的步幅，以及绘制曲面所用的色彩表。
ax.plot_surface(x,y,z,rstride=4,cstride=4,cmap=cm.YlGnBu_r)
# plt.show()

print u"等高线图"
#contour函数创建一般的等高线，对于色彩填充的等高线图
#可以使用contourf绘制
fig = plt.figure()
ax = fig.add_subplot(111)
u = np.linspace(-1,1,100)
x,y = np.meshgrid(u,u)
z = x**2+y**2
ax.contourf(x,y,z)
plt.show()

print u"动画"
import matplotlib.animation as animation
fig = plt.figure()
ax = fig.add_subplot(111)
N =10
x= np.random.rand(N)
y = np.random.rand(N)
z = np .random.rand(N)
circles,triangles,dots = ax.plot(x,'ro',y,'g',z,'b.')
ax.set_ylim(0,1)
plt.axis('off')

def update(data):
	circles.set_ydata(data[0])
	triangles.set_ydata(data[1])
	return circles,triangles

def generate():
	while True: yield np.random.rand(2,N)

anim = animation.FuncAnimation(fig,update,generate,interval=150)
plt.show()