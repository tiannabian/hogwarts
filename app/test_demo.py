#coding: utf-8
#author = hewangtong
#date = 2020/7/26
import time
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


class TestWeChat():

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

  def test_daka(self):
      """
      1、打开企业微信app
      2、点击“工作台”
      3、点击“打卡”
      4、点击“外出打卡”
      5、使用文本信息“次打卡”，点击
      6、判断打卡是否成功
      :return:
      """
      self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
      self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("打卡").instance(0))').click()
      self.driver.find_element_by_id("com.tencent.wework:id/gw8").click()
      self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()
      result = self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/n7").text
      assert '打卡成功' in result










