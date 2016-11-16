#-*- coding:utf-8 -*-
from VideoCapture import Device  
cam = Device()  
cam.setResolution(320,240)   #设置显示分辨率  
cam.saveSnapshot('demo.jpg') #抓取并保存图片