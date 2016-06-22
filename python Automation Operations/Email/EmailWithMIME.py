# -*- coding: utf-8 -*-
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

HOST = "smtp.gmail.com" #定义smtp主机
SUBJECT = u"官网业务服务质量周报" #邮件主题
TO = "" #收件人
FROM = "" #发件人

def addimg(src,imgid): #添加图片函数，参数1：图片路径，参数2：图片id
	fp = open(src,'rb')
	msgImage = MIMEImage(fp.read()) #创建MIMEImage对象，读取图片内容作为参数
	fp.close() #关闭文件
	msgImage.add_header('Content-ID',imgid) #指定图片Content-ID，<img>标签src用到
	return msgImage #返回msgImage对象

msg = MIMEMultipart('related') #采用related定义内嵌资源的邮件体

#创建一个MIMEText对象，HTML元素包括文字与图片<img>
msgtext = MIMEText("<font color=red>官网业务周平均延时图表：<br><img src=\"cid:weekly\"
	border = \"1\"><br>详细内容见附件.</font>","html","utf-8")
msg.attach(msgtext)
msg.attach(addimg("img/weekly.png","weekly"))


#创建一个MIMEText对象，附件week_report.xlsx文档
attach = MIMEText(open("doc/week_report.xlsx","rb"),read(),"base64","utf-8")
attach["Content-Type"] = "application/octet-stream" #指定文件格式类型
#指定Content-Disposition值为attachment则出现下载保存对话框，保存的默认文件名使用filename指定
#由于qqmail使用gb18030页面编码，为保证中文名不出现乱码，对文件名进行编码转换
attach["Content-Disposition"] = "attachment; filename =\" 业务服务质量周报.xlsx\"".
decode("utf-8").encode("gb18030")

msg.attach(attach)  #附件附件内容
msg['Subject'] =SUBJECT
msg['From'] =FROM
msg['To'] =TO
try:
	server = smtplib.SMTP()
	server.connect(HOST,"25")
	server.starttls()
	server.login("","")
	server.sendmail(FROM,TO,msg.as_string)
	server.quit()
	print "邮件发送成功"
except Exception, e:
	print "失败："+str(e)