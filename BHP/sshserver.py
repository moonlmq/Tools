import socket
import paramiko
import threading
import sys

# use the key from the Paramiko demo files
#host_key = paramiko.RSAKey(filename = 'test_rsa.key')

class Server(paramiko.ServerInterface):
	def _init_(self):
		self.event = threading.Event()

	def check_channel_request(self, kind, chanid):
		if kind == 'session':
			return paramiko.OPEN_SUCCEEDED
		return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

	def check_auth_password(self, username, password):
		if (username == 'root') and (password == 'root'):
			return paramiko.AUTH_SUCCESSFUL
		return paramiko.AUTH_FAILED


def main():
	server = sys.argv[1]
	ssh_port =int(sys.argv[2])
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
		sock.bind((server, ssh_port))
		sock.listen(100)
		print '[+] Listening for connection ...'
		client, addr = sock.accept()
	except Exception, e:
		print '[-] Listen failed: ' + str(e)
		sys.exit(1)
	print '[+] Got a connection'

	try:
		tSession = paramiko.Transport(client)
		#tSession = paramiko.add_server_key(host_key)
		server = Server()
		try:
			tSession.start_server(server = server)
		except paramiko.SSHException, X:
			print '[-] SSH negotiation failed.'
		chan = tSession.accept(20)
		print '[+] Authenticated!'
		print chan.recv(1024)
		chan.send('Welcome to ssh')
		while True:
			try:
				command = raw_input("Enter command: ").strip('\n')
				if command !='exit':
					chan.send(command)
					print chan.recv(1024) +'\n'
				else:
					chan.send('exit')
					print 'exiting'
					tSession.close()
					raise Exception('exit')
			except KeyboardInterrupt:
				tSession.close()
	except Exception, e:
		print '[-] Caught exception: '+ str(e)
		try:
			tSession.close()
		except:
			pass
		sys.exit(1)


main()