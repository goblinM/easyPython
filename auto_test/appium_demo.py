#! /usr/bin/env python
#coding=utf-8
import os
import time
# from selenium import webdriver
from appium import webdriver
# from lib2to3.pgen2.driver import Driver
# from lib2to3.tests.support import driver

PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__), p))

desired_caps = {
    "platformName": "Android",  # 设备系统
    "platformVersion": "6.0.1",  # 设备系统版本
    "deviceName": "a19da881",   # 设备名称
    "appPackage": "com.easefun.polyv.cloudclassdemo",  # 应用包名
    "appActivity": "com.easefun.polyv.cloudclassdemo.login.PolyvCloudClassLoginActivity"  # Activity
}
# desired_caps['app'] = PATH('C:\\Users\\LENOVO\\Desktop\\StarZone_V2.0.0.apk')
# com.easefun.polyvsdk/com.easefun.polyvsdk.activity.PolyvMainActivity
# 如果设置的是app在电脑上的路径，则不需要配appPackage和appActivity，同理反之
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #启动app

time.sleep(5)  # 启动app时，需要一定时间进入引导页，所以必须设置等待时间，不然下面会一直报错定位不到元素
driver.find_element_by_id('com.easefun.polyv.cloudclassdemo:id/login').click()
time.sleep(5)
driver.quit()
