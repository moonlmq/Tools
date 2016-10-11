# -*- coding: utf-8 -*- 
import os
class getDir(object):
	def getDirs1(self,rootDir): 
		list_dirs = os.walk(rootDir) 
		for root, dirs, files in list_dirs: 
			for d in dirs: 
				print os.path.join(root, d)      
			for f in files: 
				print os.path.join(root, f)
		return list_dirs 

	def getDirs2(self,rootDir):
		list_dirs = os.listdir(rootDir) 
		for lists in list_dirs: 
			path = os.path.join(rootDir, lists) 
			print path 
			if os.path.isdir(path): 
				Test2(path) 
		return list_dirs