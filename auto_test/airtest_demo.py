# -*- encoding=utf8 -*-
"""
Author:goblinM
Date:2019-09-02
"""
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
init_device("Android")
connect_device("android:///a19da881")
install()
start_app("com.easyfun.polyv.cloudclassdemo")
touch()
swipe()
assert_exists()
keyevent()
stop_app("com.easyfun.polyv.cloudclassdemo")
clear_app("com.easyfun.polyv.cloudclassdemo")
home()
uninstall("com.easyfun.polyv.cloudclassdemo")

# class AirTestDemo:
#     def __init__(self):
#         pass
#
#     def test_init_device(self, platform, uuid, **kwargs):
#         print(init_device(platform, uuid, **kwargs))
#
#     def test_connect_device(self, uri):
#         print(connect_device(uri))
