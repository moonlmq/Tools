# -*- coding: utf-8 -*-

import difflib
import sys

try:
	textfile1 = sys.argv[1] #第一个文件路径参数
	textfile2 = sys.argv[2] #第二个文件路径参数
except Exception,e:
	print "Error:" +str(e)
	print "Usage: FileDiff.py filename1 filename2"
	sys.exit()

def readfile(filename):
	try:
		fileHandle = open(filename,'rb')
		#读取后以行进行分隔
		text = fileHandle.read().splitlines()
		fileHandle.close()
		return text
	except IOError as error:
		print "Read file Error:" + str(error)
		sys.exit()

if textfile1 =="" or textfile2 == "":
	print "Usage: FileDiff.py filename1 filename2" #>diff.html
	sys.exit()

text1_lines = readfile(textfile1)
text2_lines = readfile(textfile2)

d = difflib.HtmlDiff()
print d.make_file(text1_lines,text2_lines) 