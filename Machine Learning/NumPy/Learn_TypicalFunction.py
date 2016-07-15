# -*- coding:utf-8 -*-

################
#专用函数
################

import numpy as np

print u"排序"
#sort函数返回排序后的数组
#lexsort函数根据键值的字典序进行排序
#argsort函数返回输入数组排序后的下标
#ndarray类的sort方法可对数组进行原地排序
#msort函数沿着第一个轴排序
#sort_complex对复数按照先实部后虚部进行排序

import datetime
def datestr2num(s):
	return datetime.datetime.strptime(s,"%d-%m-%Y").toordinal()

dates,closes = np.loadtxt('AAPL.csv',delimiter=',',usecols=(1,6),\
	converters={1:datestr2num},unpack=True)
indices =np.lexsort((dates,closes))

print "Indices",indices
print ["%s %s" % (datetime.date.fromordinal(int(dates[i])),closes[i]) for i in indices]

print u"复数"
#设置随机种子
np.random.seed(42)
complex_numbers = np.random.random(5) + 1j*np.random.random(5)
print "Complex numbers\n",complex_numbers
print "Sorted\n",np.sort_complex(complex_numbers)

print u"搜索"
#argmax返回数组中最大值对应的下标
a= np.array([2,4,8])
print "argmax",np.argmax(a)
#nanargmax提供相同功能，但忽略NaN值
#argmin和nanargmin功能类似，只是换成最小值
#argwhere根据条件搜索非零元素，并分组返回对应下标
#searchsorted可以为指定的插入值寻找维持数组排序的索引位置
#这个位置可以保持数组有序性
a =np.arange(5)
indices = np.searchsorted(a,[-2,7])
print "Indices",indices
print "The full array", np.insert(a,indices,[-2,7])
print u"抽取元素"
#extract返回满足指定条件的数组元素
print "argwhere",np.argwhere(a<=4)
a=np.arange(7)
condition = (a%2)==0
print "Even numbers",np.extract(condition,a)
#使用nonzero函数抽取数组中的非零元素
print "Non zero",np.nonzero(a)

print u"金融函数"
# fv函数计算所谓的终值（future value），即基于一些假设给出的某个金融资产在未来某一
# 时间点的价值。
# pv函数计算现值（present value），即金融资产当前的价值。
# npv函数返回的是净现值（net present value），即按折现率计算的净现金流之和。
# pmt函数根据本金和利率计算每期需支付的金额。
# irr函数计算内部收益率（internal rate of return）。内部收益率是是净现值为0时的有效利
# 率，不考虑通胀因素。
# mirr函数计算修正后内部收益率（modified internal rate of return），是内部收益率的改进
# 版本。
# nper函数计算定期付款的期数。
# rate函数计算利率（rate of interest）。
print u"终值"
#fv函数参数为利率，参数，每期支付金额，现值
print "Future value",np.fv(0.03/4, 5*4,-10,1000)
print u"现值"
#pv函数参数为利率，参数，每期支付金额，终值
print "Present value",np.pv(0.03/4,5*4,-10,1376.09633204)
#npv参数为利率和一个表示现金流的数组.
cashflows = np.random.randint(100,size=5)
cashflows = np.insert(cashflows,0,-100)
print "Cashflows",cashflows
print "Net present value",np.npv(0.03,cashflows)
print u"内部收益率"
print "Internal rate of return",np.irr([-100, 38, 48,90 ,17,36])

print u"分期付款"
#pmt输入为利率和期数,总价，输出每期钱数
print "Payment",np.pmt(0.10/12,12*30,100000)
#nper参数为贷款利率，固定的月供和贷款额，输出付款期数
print "Number of payments", np.nper(0.10/12,-100,9000)
#rate参数为付款期数，每期付款资金，现值和终值计算利率
print "Interest rate",12*np.rate(167,-100,9000,0)

print u"窗函数"
#bartlett函数可以计算巴特利特窗
window = np.bartlett(42)
print "bartlett",window
#blackman函数返回布莱克曼窗。该函数唯一的参数为输出点的数量。如果数量
#为0或小于0，则返回一个空数组。
window = np.blackman(10)
print "blackman",window
# hamming函数返回汉明窗。该函数唯一的参数为输出点的数量。如果数量为0或
# 小于0，则返回一个空数组。
window = np.hamming(42)
print "hamming",window
# kaiser函数返回凯泽窗。该函数的第一个参
# 数为输出点的数量。如果数量为0或小于0，则返回一个空数组。第二个参数为β值。
window = np.kaiser(42,14)
print "kaiser",window
# 以i0 表示第一类修正的零阶贝塞尔函数。
x= np.linspace(0,4,100)
vals = np.i0(x)
print "i0",vals
val = np.sinc(x)
print "sinc",val