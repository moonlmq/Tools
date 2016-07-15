# -*- coding:utf-8 -*-

#################################
#Numpy模块
#################################
import numpy as np

print u"线性代数"
#numpy.linalg中的inv函数可以计算逆矩阵
print u"逆矩阵"
A = np.mat("0 1 2; 1 0 3; 4 -3 8")
print "A",A
inverse = np.linalg.inv(A)
print "inverse of A", inverse
print "Check", A*inverse

print u"求解线性方程组"
A = np.mat("1 -2 1;0 2 -8;-4 5 9")
print "A\n",A
b = np.array([0, 8, -9])
print "b\n",b
#调用solve函数求解线性方程组
x = np.linalg.solve(A,b)
print "Solution",x
#使用dot函数检查求得解是否正确
print "Check wiith dot",np.dot(A,x)

print u"特征值和特征向量"
#特征值即方程Ax=ax的根，是一个标量。其中，A是一个二维矩阵，x
#是一个一维向量。特征向量是关于特征值的向量。
#numpy.linalg模块中，eigvals函数可以计算矩阵特征值，而eig函数
#可以返回一个包含特征值和对应的特征向量和元祖
A =np.mat("3 -2;1 0")
print "A\n",A
#调用eigval函数求解特征值
print "Eigenvalues",np.linalg.eigvals(A)
#使用eig函数求解特征值和特征向量。函数返回一个元祖，按列排放着
#特征值和对应的特征向量，其中第一列为特征值，第二列为特征向量
eigenvalues,eigenvectors = np.linalg.eig(A)
print "First tuple of eig", eigenvalues
print "Second tuple of eig\n",eigenvectors
#dot函数验证
for i in range(len(eigenvalues)):
	print "Left",np.dot(A,eigenvectors[:,i])
	print "Right",eigenvalues[i]*eigenvectors[:,i]


print u"奇异值分解"
#SVD是一种因子分解运算，将一个矩阵分解为3个矩阵的乘积。
A = np.mat("4 11 14;8 7 -2")
print "A\n", A
#svd函数可以对矩阵进行奇异值分解，返回U,Sigma和V，其中
#U和V是正交矩阵，Sigma包含输入矩阵的奇异值
U,Sigma,V = np.linalg.svd(A,full_matrices=False)
print "U"
print U
print "Sigma"
print Sigma
print "V"
print V
print "Product\n", U*np.diag(Sigma)*V

print u"广义逆矩阵"
A = np.mat("4 11 14; 8 7 -2")
print "A\n",A
#使用pinv计算广义逆矩阵
pseudoinv = np.linalg.pinv(A)
print "Pseudo inverse\n", pseudoinv
print "Check", A*pseudoinv

print u"行列式"
A = np.mat("3 4;5 6")
print "A\n", A
#使用det函数计算行列式
print "Determinant", np.linalg.det(A)

print u"傅里叶变换"
x = np.linspace(0, 2*np.pi, 30)
wave = np.cos(x)
#fft函数对余弦信号进行傅里叶变换
transformed = np.fft.fft(wave)
#应用ifft函数还原
print np.all(np.abs(np.fft.ifft(transformed)-wave) < 10** -9)

print u"移频"
#使用fftshift进行操作
shifted = np.fft.fftshift(transformed)
#ifftshift逆操作
print np.all((np.fft.ifftshift(shifted)- transformed)< 10** -9)

print u"随机数"
#numpy中random模块binomoal函数模拟随机游走
cash =np.zeros(10000)
cash[0] = 1000
#每轮抛9个硬币，如果少于5枚正面朝上损失一份，否则赢得一份
outcome = np.random.binomial(9,0.5,size=len(cash))
for i in range(1, len(cash)):
	if outcome[i] < 5:
		cash[i] = cash[i-1]-1
	elif outcome[i] <10:
		cash[i] = cash[i-1]+1
	else:
		raise AssertionError("Unexpected outcome "+ outcome)

print u"超几何分布"
#numpy中random模块hypergeometric可以实现
points = np.zeros(100)
#第一个参数为普通参数数量，第二个参数为问题参数数量，第三个参数为
#每次采样数量
outcome = np.random.hypergeometric(25,1,3,size=len(points))
print outcome

print u"连续分布"
#normal函数模拟正态分布
print "normal",np.random.normal(size= 10)
#lognormal模拟自然对数服从正态分布的任意随机变量的概率分布
print "lognormal",np.random.lognormal(size=10)