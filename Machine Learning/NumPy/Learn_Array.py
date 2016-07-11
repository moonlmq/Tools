# -*- coding:utf-8 -*-
from numpy import *
import sys

reload(sys)  
sys.setdefaultencoding('utf8')

# new a  multi-dimension array
print "new a  multi-dimension array"
m = array([arange(2),arange(2)])
print m
print m.shape

a = array([[1,2],[3,4]])
print a[0,0],a[0,1]

#######################################################################################
# bool 用一位存储的布尔类型（值为TRUE或FALSE）
# inti 由所在平台决定其精度的整数（一般为int32或int64）
# int8 整数，范围为128至127
# int16 整数，范围为32 768至32 767
# int32 整数，范围为231至231 1
# int64 整数，范围为263至263 1
# uint8 无符号整数，范围为0至255
# uint16 无符号整数，范围为0至65 535
# uint32 无符号整数，范围为0至2321
# uint64 无符号整数，范围为0至2641
# float16 半精度浮点数（16位）：其中用1位表示正负号，5位表示指数，10位表示尾数
# float32 单精度浮点数（32位）：其中用1位表示正负号，8位表示指数，23位表示尾数
# float64或float 双精度浮点数（64位）：其中用1位表示正负号，11位表示指数，52位表示尾数
# complex64 复数，分别用两个32位浮点数表示实部和虚部
# complex128或complex 复数，分别用两个64位浮点数表示实部和虚部
########################################################################################

##################
# 整数 i
# 无符号整数 u
# 单精度浮点数 f
# 双精度浮点数 d
# 布尔值 b
# 复数 D
# 字符串 S
# unicode字符串 U
# void （空） V
###################

#set data type
print ""
print "set data type"
a = arange(7,dtype=uint16)
print a
b = arange(7,dtype ='f')
print b

# 自定义数据类型
print u"自定义数据类型"
t = dtype([('name', str_, 40), ('numitems',int32),('price',float32)])
print t


# 一维索引和切片
print u"一维索引和切片"
a = arange(9)
print u"切片"
print a[3:7] #3,4,5,6
print u"以2为步长选取元素"
print a[:7:2] #0,2,4,6
print u"利用负数下标翻转数组"
print a[::-1] #8,7,6,5,4,3,2,1,0

print u"多维数组切片和索引"
b = arange(24).reshape(2,3,4)
print b.shape
print b
# (2, 3, 4)
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]

#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]
print b[0,0,0]
print b[:,0,0]
print b[0] #或者b[0,:,:] 多个冒号可以用（...）代替 b[0,...]
print u"数组切片中间隔地选定元素"
print b[0,1,::2]
print u"选取所有位于第二列的房间"
print b[0,:,1]
print u"选取第一楼最后一列所有房间"
print b[0,:,-1]
print u"反向选取第一层最后一列所有房间"
print b[0,::-1,-1]
print u"数组切片中间隔选定元素"
print b[0,::2,-1]
print u"翻转"
print b[::-1]

print u"改变数组维度"
print u"reval 完成展平操作"
print b.ravel()
print u"flatten 与reval一样，会请求分配内存，reval返回一个view"
print b.flatten()
print u"用元祖设置维度"
b.shape =(6,4)
print b
print u"转置矩阵"
print b.transpose
print u"resize与reshape一样，但会修改所操作的数组"
print b.resize((2,12))


print u"数组组合"
a = arange(9).reshape(3,3)
print a
b = 2*a
print b

print u"水平组合"
c = hstack((a,b))
print c
d = concatenate((a,b), axis =1)
print d

print u"垂直组合"
c = vstack((a,b))
print c
d = concatenate((a,b),axis = 0)
print d

print u"深度组合"
c = dstack((a,b))
print c

print u"列组合 column_stack对于一维数组按列方向进行组合，二维与hstack效果一样"
oned = arange(2)
print oned
t_oned = 2*oned
print t_oned
c = column_stack((oned,t_oned))
print c
d = column_stack((a,b))
print d

print u"行组合 row_stack对于一维数组按行方向进行组合，二维与vstack效果一样"
c = row_stack((oned,t_oned))
print c
d = row_stack((a,b))
print d

print u"分割数组"

print a
print u"水平分割"
c = hsplit(a,3)
print c
d =split(a,3,axis=1)
print d

print u"垂直分割"
c = vsplit(a,3)
print c
d = split(a,3,axis = 0)
print d

print u"深度分割"
a = arange(27).reshape(3,3,3)
print a
c = dsplit(a,3)
print c 


print u"数组属性"
b = arange(24)
print b

print u"size属性，给出数组元素总个数"
print b.size

print u"itemsize属性，给出数组中元素在内存中所占字节数"
print b.itemsize

print u"整个数组所占储存空间"
print b.nbytes

print u"T属性和transpose效果一样"
print b.resize(6,4)
print b.T
print u"一维数组T为原数组"
a=arange(3)
print a.ndim
print a.T

print u"复数的虚部用j表示"
b = array([1.j+1,2.j+3])
print b

print u"real属性给出复数数组的实部"
print b.real

print u"imag属性给出复数数组的虚部"
print b.imag

print u"如果数组包含复数元素，则类型为复数型"
print b.dtype

print u"flat属性会返回一个numpy.flatiter对象，"+\
"这是获得flatiter对象的唯一方式，这个可以让我" +\
"们像遍历一维数组一样去遍历任意多维数组"
b = arange(4).reshape(2,2)
print b
f = b.flat
print f
for item in f: print item
print u"直接获取元素"
print b.flat[2]
print b.flat[[1,3]]

print u"flat属性是一个可赋值属性，对flat赋值将导致整个数组元素被覆盖"

b.flat=7
print b
b.flat[[1,3]]=1
print b


print u"数组的转换"
print u"转换成列表"
b = array([1.j+1,2.j+3])
print b
print b.tolist()

print u"astype可以在转换数组时指定数据类型"
print b.astype(int)