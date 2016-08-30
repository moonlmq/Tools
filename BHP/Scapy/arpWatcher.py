from scapy.all import sniff.ARP
from signal import signal.SIGINT
import sys

ip_mac = {}

def watchArp(pkt):
	if pkt[ARP].op == 2:
		print pkt[ARP].hwsrc +" "+ pkt[ARP].psrc

	# Device is new. Remember it
	if ip_mac.get(pkt[ARP].psrc) == None:
		print "Found new device " + pkt[ARP].hwsrc + " "+\
		pkt[ARP].psrc

	# Device is known but has a different IP
	elif ip_mac.get(pkt[ARP].psrc) and ip_mac[pkt[ARP].psrc] != pkt[ARP].hwsrc:
		print pkt[ARP].hwsrc + " has got new ip " + pkt[ARP].psrc +\
		" (old "+ip_mac[pkt[ARP].psrc]+")"
		ip_mac[pkt[ARP].psrc] = pkt[ARP].hwsrc

sniff(prn=watchArp,filter="arp",iface="eth0",store=0)