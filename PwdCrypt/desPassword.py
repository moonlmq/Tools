#-*- coding:utf-8 -*-

#####################################
#this script is use for decription the password from a txt 
#which use for dictionary
#####################################
import crypt

#description the password
def  getPassword(cryptPass):
	salt = cryptPass[0:2]
	dictFile = open('dictionary.txt','r')
	for word in dictFile.readlines():
		word = word.strip('\n')
		print word
		cryptWord = crypt.crypt(word,salt)
		print "cryptWord is "+cryptWord
		if  cryptWord ==cryptPass.strip('\n'):
			print "Found Password : "+ word + "\n"
			return
	print "Not found!\n"
	return

#open the file begin the description
def main():
	passFile =  open('passwords.txt','r')
	for line in passFile.readlines():
		if ":" in line:
			user =  line.split(':')[0]
			cryptPass = line.split(':')[1].strip(' ')
			print "cryptPass is "+cryptPass
			print "Cracking Password For : "+user
			getPassword(cryptPass)

if  __name__  =="__main__":
	main()


		


