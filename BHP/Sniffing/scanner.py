import threading
import time
from netaddr import IPNetwork, IPAddress
from ICMP import ICMP
import os
from sniffer_ip_header_decode import IP
import socket
from ctypes import *

#host to listen on
host = "192.168.253.4"

# subnet to target
subnet = "192.168.253.0/24"

#magic string to check ICMP responses 
magic_message = 'abcdefghigklmnopq'

#this sprays out the UDP datagrams
def udp_sender(subnet, magic_message):
	time.sleep(5)
	sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	for ip in IPNetwork(subnet):
		try:
			sender.sendto(magic_message,("%s" % ip,65212))
		except:
			pass






def main():
	if os.name == "nt":
		socket_protocol = socket.IPPROTO_IP
	else:
		socket_protocol = socket.IPPROTO_ICMP

	sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)

	sniffer.bind((host, 0))
	sniffer.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)

	if os.name == "nt":
		sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
	#start sending packets
	t = threading.Thread(target = udp_sender, args = (subnet, magic_message))
	t.start()

	try:
		while True:
			# read in packet
			raw_buffer = sniffer.recvfrom(65565)[0]
			ip_content =raw_buffer[0:20]

			# create an IP header from the first 20 bytes of the buffer
			ip_header = IP(ip_content)

			#print out the protocol that was detected and the hosts
			# print "Protocol: %s %s -> %s" %(ip_header.protocol, ip_header.src_address\
			# 	, ip_header.dst_address)

			#decode ICMP
			if ip_header.protocol == "ICMP":
				# calculate where ICMP packet starts
				offset = ip_header.ihl*4

				buf = raw_buffer[offset:offset+sizeof(ICMP)]

				# create ICMP structure
				icmp_header = ICMP(buf)

				# print "ICMP -> Type: %d Code: %d" % (icmp_header.type, icmp_header.code)

				#check for the TYPE 3 and CODE
				if icmp_header.code == 3 and icmp_header.type == 3:

					#make sure host is in target subnet
					if IPAddress(ip_header.src_address) in IPNetwork(subnet):
						#make sure it has magic message
						print "get the response from",ip_header.src_address
						if raw_buffer[len(raw_buffer) - len(magic_message):] ==\
						magic_message:
							print "Host Up: %s" % ip_header.src_address



	except KeyboardInterrupt:
		#if using Windows, trun off promiscuous mode
		if os.name == "nt":
			sniffer.ioctl(socket.SIO_RCVALL,socket.RCVALL_OFF)


if __name__ == '__main__':
	main()