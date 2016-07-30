# -*- coding:utf-8 -*-

##############
#质量控制
##############
import numpy as np
import unittest

print u"断言函数"
# assert_almost_equal 如果两个数字的近似程度没有达到指定精度，就抛出异常
# assert_approx_equal 如果两个数字的近似程度没有达到指定有效数字，就抛出异常
# assert_array_almost_equal 如果两个数组中元素的近似程度没有达到指定精度，就抛出异常
# assert_array_equal 如果两个数组对象不相同，就抛出异常
# assert_array_less 两个数组必须形状一致，并且第一个数组的元素严格小于第二个数组的元素，否则
# 就抛出异常
# assert_equal 如果两个对象不相同，就抛出异常
# assert_raises 若用填写的参数调用函数没有抛出指定的异常，则测试不通过
# assert_warns 若没有抛出指定的警告，则测试不通过
# assert_string_equal 断言两个字符串变量完全相同
# assert_allclose 如果两个对象的近似程度超出了指定的容差限，就抛出异常

#小数点后7位
print "Decimal 6 with assert_almost_equal", np.testing.assert_almost_equal(0.123456789,0.123456780,decimal=7)
#后8位
print "Decimal 7 with assert_almost_equal",  np.testing.assert_almost_equal(0.123456789,0.123456780,decimal=8)


print "Significance 8 with assert_approx_equal", np.testing.assert_approx_equal(0.123456789,0.123456780,significant=8)
print "Significance 9 with assert_approx_equal", np.testing.assert_approx_equal(0.123456789,0.123456780,significant=9)

print u"数组近似相等"
#如果两个数组中元素的近似程度没有达到指定的精度要求，
#assert_array_almost_equal函数将抛出异常。
print "Decimal 8",np.testing.assert_array_almost_equal([0,0.123456789],[0,0.123456780],decimal=8)
print "Decimal 9",np.testing.assert_array_almost_equal([0,0.123456789],[0,0.123456780],decimal=9)	

print u"比较数组"
# 比较数组也可以使用assert_allclose函数。该函数有参数atol（absolute tolerance，
# 绝对容差限）和rtol（relative tolerance，相对容差限）。对于两个数组a和b，将测试是否满足以
# 下等式：
# |a - b| <= (atol + rtol * |b|)
print "Pass",np.testing.assert_allclose([0,0.123456789,np.nan],[0,0.123456780,np.nan],rtol=1e-7,atol=0)
print "Fail",np.testing.assert_array_equal([0,0.123456789,np.nan],[0,0.123456780,np.nan])

print u"数组排序"
#assert_array_less函数比较两个有严格顺序的数组
print "Pass", np.testing.assert_array_less([0, 0.123456789, np.nan], [1, 0.23456780,np.nan])
print "Fail", np.testing.assert_array_less([0, 0.123456789, np.nan], [0, 0.123456780,np.nan])

print u"比较对象"
#要比较两个元组。我们可以用assert_equal函数来完成
print "Equal?", np.testing.assert_equal((1, 2), (1, 3))

print u"字符串比较"
# assert_string_equal函数断言两个字符串变量完全相同
print "Pass", np.testing.assert_string_equal("NumPy", "NumPy")
print "Fail", np.testing.assert_string_equal("NumPy", "Numpy")

print u"浮点数比较"
#使用finfo函数确定机器精度
eps = np.finfo(float).eps
print "EPS", eps
# 使用assert_array_almost_equal_nulp函数比较两个近似相等的浮点数1.0和1.0
# + eps（epsilon），然后对1.0 + 2 * eps做同样的比较：
print "1",
np.testing.assert_array_almost_equal_nulp(1.0, 1.0 + eps)
print "2",
np.testing.assert_array_almost_equal_nulp(1.0, 1.0 + 2 * eps)
# 使用assert_array_max_ulp函数和适当的maxulp参数值：
print "1", np.testing.assert_array_max_ulp(1.0, 1.0 + eps)
print "2", np.testing.assert_array_max_ulp(1.0, 1 + 2 * eps, maxulp=2)

print u"编写单元测试"
#为一个简单的阶乘函数编写测试代码，检查所谓的程序主逻辑以及非法输入的情况
def factorial(n):
	if n==0:
		return 1

	if n<0:
		raise ValueError,"Unexpected negative value"
	return np.arange(1,n+1).cumprod()

class FactorialTest(unittest.TestCase):
	def test_factorial(self):
		#计算3的阶乘
		self.assertEqual(6,factorial(3)[-1])
		np.testing.assert_equal(np.array([1,2,6]),factorial(3))
	def test_zero(self):
		self.assertEqual(1,factorial(0))
	def test_negative(self):
		self.assertRaises(IndexError,factorial(-10))

if __name__ =='__main__':
	unittest.main()

print u"nose和测试装饰器"
# numpy.testing.decorators.deprecated 在运行测试时过滤掉过期警告
# numpy.testing.decorators.knownfailureif 根据条件抛出KnownFailureTest异常
# numpy.testing.decorators.setastest 将函数标记为测试函数或非测试函数
# numpy.testing.decorators. skipif 根据条件抛出SkipTest异常
# numpy.testing.decorators.slow 将测试函数标记为“运行缓慢”

from numpy.testing.decorators import setastest
from numpy.testing.decorators import skipif
from numpy.testing.decorators import knownfailureif
from numpy.testing import decorate_methods
#将一个函数用于测试，另一个不用于测试
@setastest(False)
def test_false():
	pass
@setastest(True)
def test_true():
	pass
#以使用skipif装饰器跳过测试。这里，我们使用一个条件使得该测试总是被跳过
@skipif(True)
def test_skip():
	pass
#添加一个空函数用于测试，并使用knownfailureif装饰器使得该测试总是不通过
@knownfailureif(True)
def test_alwaysfail():
	pass
#定义一些可以被nose执行的函数和对应的测试类：
class TestClass():
	def test_true2(self):
		pass

class TestClass2():
	def test_false2(self):
		pass
#将上一步的第二个函数在测试中禁用：
decorate_methods(TestClass2,setastest(False),'test_false2')
#测试执行命令：nosetests -v decorator_setastest.py

print u"文档字符串"
def factorial(n):
"""
Test for the factorial of 3 that should pass.
>>> factorial(3)
6
Test for the factorial of 0 that should fail.
>>> factorial(0)
1
"""
return np.arange(1, n+1).cumprod()[-1]
#执行命令
# >>>from numpy.testing import rundocs
# >>>rundocs('docstringtest.py')