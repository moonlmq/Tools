from scapy.all import *

i = 5
while(i):
	#产生随机MAC地址与IP
	print RandMAC()
	print RandIP()
	#产生固定网段IP
	print RandIP("192.168.1.*")
	i = i-1