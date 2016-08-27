# -*-coding:utf-8-*-
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
resp = requests.get("http://www.tuicool.com/articles/nEjiEv")

print (resp.status_code)
print
print (resp.text)