# -*- coding: utf-8 -*-   
import telnetlib
import time 
'''''Telnet远程登录：Windows客户端连接Linux服务器'''  
# 配置选项  
Host = '10.26.0.17' # Telnet服务器IP  
username = 'bmu852'   # 登录用户名  
password = 'aaaabbbb'  # 登录密码  
finish = '->'      # 命令提示符（标识着上一条命令已执行完毕）  

t = 5
# 连接Telnet服务器  
tn = telnetlib.Telnet(Host)  
print "Telneting..."
# 输入登录用户名  
tn.read_until('login: ')  
tn.write(username + '\n')  
# 输入登录密码  
tn.read_until('Password: ')  
tn.write(password + '\n')
print "logining..."  
# 登录完毕后，执行ls命令  
print "wait for login"  
print "go to 0"
tn.read_until(finish)  
tn.write('digi_oduk_loopback 24,0\n')  
# ls命令执行完毕后，终止Telnet连接（或输入exit退出）  
print "0"
tn.read_until(finish)  
time.sleep(t-0.15)
tn.write('digi_oduk_loopback 24,1\n')  
# ls命令执行完毕后，终止Telnet连接（或输入exit退出）  
print "1"
tn.read_until(finish)  
tn.close() # tn.write('exit\n') 