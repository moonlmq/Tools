import socket
import os
import struct
from ctypes import *

# host to listen on
host = "127.0.0.1"

# IP header
class IP(Structure):
	_fields_ = [
	("ihl",			c_ubyte, 4),
	("version",		c_ubyte, 4),
	("tos",			c_ubyte),
	("len",			c_ushort),
	("id",			c_ushort),
	("offset",		c_ushort),
	("ttl",			c_ubyte),
	("protocal_num",c_ubyte),
	("sum",			c_ushort),
	("src",			c_ulong),
	("dst",			c_ulong)]

	def __new__(self, socket_buffer=None):
		return self.from_buffer_copy(socket_buffer)

	def __init__(self,socket_buffer=None):

		#map protocol constants to their names
		self.protocol_map = {1:"ICMP", 6:"TCP", 17:"UDP"}

		#human readable IP addresses
		self.src_address = socket.inet_ntoa(struct.pack("<L",self.src))
		self.dst_address = socket.inet_ntoa(struct.pack("<L",self.dst))

		# human readable protocol
		try:
			self.protocol = self.protocol_map[self.protocal_num]
		except:
			self.protocol = str(self.protocal_num)


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

	try:
		while True:
			# read in packet
			raw_buffer = sniffer.recvfrom(65565)[0]
			ip_content =raw_buffer[0:20]

			# create an IP header from the first 20 bytes of the buffer
			ip_header = IP(ip_content)

			#print out the protocol that was detected and the hosts
			print "Protocol: %s %s -> %s" %(ip_header.protocol, ip_header.src_address\
				, ip_header.dst_address)
	except KeyboardInterrupt:
		#if using Windows, trun off promiscuous mode
		if os.name == "nt":
			sniffer.ioctl(socket.SIO_RCVALL,socket.RCVALL_OFF)


if __name__ == '__main__':
	main()
