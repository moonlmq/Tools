# -*- coding: utf-8 -*-
import smtplib
import string

HOST = "smtp.qq.com"  #定义smtp主机
SUBJECT = "Test email from python" #定义邮箱主题
TO = "" #定义邮件收件人
FROM = "" #定义邮件发件人
text = "hello, nice to meet you" #内容

#组装sendmail方法的邮件主体内容，各段以"\r\n"进行分隔
BODY = string.join((
	"From: %s" % FROM,
	"To: %s" % TO,
	"Subject: %s" % SUBJECT,
	"",
	text),"\r\n")

server = smtplib.SMTP() #创建一个SMTP对象
server.connect(HOST,"25") #通过connect 方法连接smtp主机
server.starttls() #启动安全传输模式
server.login("","") #邮箱账号登录校验
server.sendmail(FROM,[TO],BODY) #邮件发送
server.quit() #断开smtp连接