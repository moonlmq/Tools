import socket
import threading

############
#TCP client
############
tcptarget_host ="hostsite"
tcptarget_port = 80

#new a socket object
#AF_INET means typical IPv4 address or host, SOCK_STREAM
#means it's a TCP client
tcpclient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Connect to the server
tcpclient.connect((tcptarget_host,tcptarget_port))

#Send some data
tcpclient.send("aaaaa")

#receivve some data
tcpresponse = tcpclient.recv(4096)
print tcpresponse

############
#UDP client
############
udptarget_host= "hostsite"
udptarget_port= 80

#new a socket object
udpclient = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#send some data
udpclient.sendto("aaaaa",(udptarget_host,udptarget_port))

#receive some data
data, addr = client.revfrom(4096)
print data


###################
#TCP server
###################
bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))
server.listen(5)

print "[*] Listening on %s:%d" %(bind_ip,bind_port)

#client handle thread
def handle_client(client_socket):

	#print the data received from client
	request = client_socket.recv(1024)

	print "[*] Received: %s" % request

	#return a data packet
	client_socket.send("ACK!")
	client_socket.close()

while True:
	client,addr = server.accept()
	print "[*] Accepted connection from: %s:%d" % (addr[0],addr[1])

	client_handler = threading.Thread(target=handle_client,args=(client,))
	client_handler.start()