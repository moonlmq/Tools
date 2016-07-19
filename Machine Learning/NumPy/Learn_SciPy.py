#-*- coding:utf-8 -*-
import numpy as np
from scipy import io
print u"MATLAB和Octave"
#scipy.io包的函数可以在Python中加载或保存MATLAB和Octave的矩阵和数组
#loadmat函数可以加载.mat文件。savemat函数可以将数组和指定的变量名字典保存为.mat文件
a = np.arange(7)
io.savemat("a.mat",{"array":a})

print u"分析随机数"
from scipy import stats
import matplotlib.pyplot as plt
#使用scipy.stats包按正态分布生成随机数
generated = stats.norm.rvs(size=900)
#用正态分布去拟合生成的数据，得到均值和标准差
print "Mean","Std",stats.norm.fit(generated)
#偏度描述的是概率分布的偏斜程度。
print "Skewtest","pvalue",stats.skewtest(generated)
#峰度描述的是概率分布曲线的陡峭程度
print "Kurtosistest","pvalue",stats.kurtosistest(generated)
#正态性检验可以检查数据集服从正态分布程度
print "Normaltest","pvalue",stats.normaltest(generated)
#得到数据所在的区段中某一百分比处的数值
print "95 percentile",stats.scoreatpercentile(generated,95)
#从数值1出发找到对应的百分比
print "Percentile at 1",stats.percentileofscore(generated,1)
plt.hist(generated)
# plt.show()

print u"比较对数收益率"
# from matplotlib.finance import quotes_historical_yahoo
# from datetime import date
# from statsmodels.stats.stattools import jarque_bera
# def get_close(symbol):
# 	today = date.today()
# 	start = (today.year-1,today.month,today.day)
# 	quotes = quotes_historical_yahoo(symbol,start,today)
# 	quotes = np.array(quotes)
# 	return quotes.T[4]

# spy = np.diff(np.log(get_close("SPY")))
# dia = np.diff(np.log(get_close("DIA")))

# print "Mean comparison", stats.ttest_ind(spy,dia)
# print "Kolmogorov smirnov test", stats.ks_2sqmp(spy,dia)
# print "Jarque Bera test", jarque_bera(spy-dia)[1]
# plt.hist(spy,histtype="step",lw=1,label="SPY")
# plt.hist(dia,histtype="step",lw=2,label="DIA")
# plt.hist(spy-dia,histtype="step",lw=3,label="Delta")
# plt.legend()
# plt.show()


print u"检测线性趋势"
from matplotlib.finance import quotes_historical_yahoo
from datetime import date
from scipy import signal
from matplotlib.dates import DateFormatter
from matplotlib.dates import DayLocator
from matplotlib.dates import MonthLocator
import matplotlib.pyplot as plt
today = date.today()
start = (today.year-1,today.month,today.day)
quotes = quotes_historical_yahoo("DISH", start,today)
quotes = np.array(quotes)

dates = quotes.T[0]
qqq = quotes.T[4]

y = signal.detrend(qqq)

alldays = DayLocator()
months = MonthLocator()
month_formatter = DateFormatter("%b %Y")
fig = plt.figure()
ax =fig.add_subplot(111)

plt.plot(dates,qqq,'o',dates,qqq-y,'-')
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(month_formatter)
fig.autofmt_xdate()
# plt.show()

print u"滤波处理"
#调大字号
from scipy import fftpack
ax.tick_params(axis="both",which='major',labelsize='x-large')
#应用傅里叶变化得到信号的频谱
amps = np.abs(fftpack.fftshift(fftpack.rfft(y)))
#滤除噪声。如果某一频率分量大小低于最强分量的10%，则将其滤除
amps[amps <0.1 * amps.max()] =0
#将滤波后的信号变换回时域，并和去除趋势后的信号一起绘制处理
plt.plot(dates,y,'o',label ="detrended")
plt.plot(dates,-fftpack.irfft(fftpack.ifftshift(amps)),label="filtered")
fig.autofmt_xdate()
plt.legend(prop={'size':'x-large'})

ax2 = fig.add_subplot(212)
ax2.tick_params(axis='both',which='major',labelsize='x-large')
N = len(qqq)
plt.plot(np.linspace(-N/2,N/2,N),amps,label="transformed")
plt.legend(prop={'size':'x-large'})
# plt.show()

print u"拟合正弦波"
from scipy import optimize
#正弦波模型
def reisduals(p,y,x):
	A,k,theta,b = p
	err = y - A*np.sin(2*np.pi*k*x+theta)+b
	return err

#滤波后的信号变换回时域
filtered = -fftpack.irfft(fftpack.ifftshift(amps))
#尝试估计从时域到频域的变换函数
f = np.linspace(-N/2,N/2,N)
p0=[filtered.max(),f[amps.argmax()]/(2*N),0,0]
print "p0",p0
#调用leastsq函数
plsq=optimize.leastsq(reisduals,p0,args=(filtered,dates))
p = plsq[0]
print "p",p
plt.plot(dates,y,'o',label="detrended")
plt.plot(dates,filtered,label="filtered")
plt.plot(dates,p[0]*np.sin(2*np.pi*dates*p[1]+p[2])+p[3],'-',label='fit')
fig.autofmt_xdate()
plt.legend(prop={'size':'x-large'})

ax2 = fig.add_subplot(212)
plt.plot(f,amps,label="transformed")
plt.show()