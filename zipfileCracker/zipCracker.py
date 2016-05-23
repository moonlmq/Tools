# -*- coding :utf-8 -*-

##############################
#this script is use for unzip a cript zip file
##############################
import zipfile
import optparse
from threading import Thread

#unzipfile
def extracFile(zFile, password):
	try:
		zFile.extractall(pwd=password)
		print password
		print '[+] Found Password '+ password +'\n'
	except:
		pass

def main():
	parser = optparse.OptionParser("usage%prog -f <zipfile> -d <dictionary>")
	parser.add_option('-f', dest ='zname', type='string', help = 'specify zip file')
	parser.add_option('-d', dest = 'dname', type = 'string', help = 'specify dictionary file')
	(options, args) = parser.parse_args()
	if (options.zname == None) | (options.dname == None):
		print parser.usage
		exit(0)
	else:
		zname = options.zname
		dname = options.dname

	zFile = zipfile.ZipFile(zname)
	passFile = open(dname)
	for line in passFile.readlines():
		password = line.strip('\n')
		t = Thread(target = extracFile, args=(zFile, password))
		t.start()
		extracFile(zFile,password)

if __name__ == '__main__':
	main()

