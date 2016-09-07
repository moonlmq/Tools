#-*-coding:utf-8
from scapy.all import *
#指定目标主机的MAC和IP地址，添加两个VLAN标识
packet = Ether(dst="c0:d3:de:ad:be:ef")/Dot1Q(vlan=1)/Dot1Q(vlan=2)/IP(dst="192.168.13.3")/ICMP()

sendp(packet)

