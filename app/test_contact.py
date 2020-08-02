#coding: utf-8
#author = hewangtong
#date = 2020/7/26
import time
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


class TestContact:

  def setup(self):
    desire_caps = {
      "platformName": "android",
      "deviceName": "127.0.0.1:7555",
      "appPackage": "com.tencent.wework",
      "appActivity": "com.tencent.wework.launch.WwMainActivity",
        "noReset": "true",
      "unicodeKeyBoard" : "true",
      "resetKeyBoard" : "true"
    }
    self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desire_caps)
    self.driver.implicitly_wait(10)

  def teardown(self):
    self.driver.quit()

  def test_addcontact(self):
    """
    1、
    2、
    3、
    4、
    :return:
    """
    self.driver.find_element(MobileBy.XPATH, "//android.widget.TextView[@text='通讯录']").click()
    self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                             'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0))').click()
    self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../*[@class='android.widget.TextView']").send_keys("")
