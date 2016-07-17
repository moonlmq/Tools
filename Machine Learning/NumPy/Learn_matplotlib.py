# - *-coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

#以自然数序列作为多项式的系数，使用poly1d函数创建多项式
func = np.poly1d(np.array([1,2,3,4]).astype(float))
x = np.linspace(-10,10,30)
y = func(x)
plt.plot(x,y)
#添加x,y轴标签
plt.xlabel('x')
plt.ylabel('y(x)')
plt.show()