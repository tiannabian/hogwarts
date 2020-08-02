#coding: utf-8
#author = hewangtong
#date = 2020/7/26
from appium import webdriver

from app.page.mainpage import MainPage


class App:

    def start(self):
        """启动APP"""
        desire_caps = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.tencent.wework",
            "appActivity": "com.tencent.wework.launch.WwMainActivity",
            "noReset": "true",
            "unicodeKeyBoard": "true",
            "resetKeyBoard": "true"
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desire_caps)
        self.driver.implicitly_wait(10)
        return self


    def restart(self):
        """重启APP"""


    def stop(self):
        """停止APP"""


    def goto_main(self):
        """进入首页"""


        return MainPage()