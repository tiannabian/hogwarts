#coding: utf-8
#author = hewangtong
#date = 2020/7/18
import time

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


class TestDW():

  def setup(self):
    desire_caps = {
      "platformName": "android",
      "deviceName": "127.0.0.1:7555",
      "appPackage": "com.xueqiu.android",
      "appActivity": ".view.WelcomeActivityAlias",
        "noReset": "true",
      "unicodeKeyBoard" : "true",
      "resetKeyBoard" : "true"
    }
    self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desire_caps)
    self.driver.implicitly_wait(10)

  def teardown(self):
    #self.driver.quit()
    pass

  def test_search(self):
    print("搜索测试用例")
    """
    1、打开雪球APP
    2、点击搜索输入框
    3、向搜索输入框里面输入“阿里巴巴”
    4、在搜索结果里面选择“阿里巴巴”，然后进行点击
    5、获取这只阿里巴巴的股价，并判断，这只股价的价格>200
    """
    el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
    self.driver.implicitly_wait(10)
    el2 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
    el3 = self.driver.find_element_by_xpath(
      "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]")
    el3.click()
    current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
    assert current_price >200

  def test_dwpytest(self):
    """
    1、打开雪球APP首页
    2、点击首页的搜索输入框
    3、判断搜索输入框是否可见，并查看搜索框name属性值
    4、打印搜索框这个元素的左上角坐标和它的宽高
    5、向搜索输入框里面输入“alibaba”
    6、判断“阿里巴巴”是否可见
    7、如果可见，打印“搜索成功”点击，如果不可见，打印“搜索失败”
    """
    el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
    self.driver.implicitly_wait(10)
    search_enabled = el1.is_enabled()
    print(el1.text)
    print(el1.location)
    print(el1.size)
    if search_enabled == True:
      el1.click()
      self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
      self.driver.implicitly_wait(5)
      alibaba_element = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
      element_display = alibaba_element.get_attribute("displayed")
      if element_display == 'true':
        print("搜索成功")
      else:
        print("搜索失败")

  def test_touchaction(self):
    action = TouchAction(self.driver)
    window_rect = self.driver.get_window_rect()
    width = window_rect['width']
    height = window_rect['height']
    x1 = int(width/2)
    y_start = int(height*4/5)
    y_end = int(height*1/5)
    action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).release().perform()

  def test_touchaction_aunlock(self):
    print("解锁操作")
    action = TouchAction(self.driver)
    action.press(x=243,y=395).wait(200).move_to(x=721,y=378).wait(200).move_to(x=1190,y=364).wait(200).move_to(x=1202,y=859).wait(200).move_to(x=1195,y=1339).wait(200).release().perform()


  def test_get_current(self):
    el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
    self.driver.implicitly_wait(10)
    el2 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
    el3 = self.driver.find_element_by_xpath(
      "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]")
    el3.click()
    current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
    print(type(current_price))
    print(current_price)
    assert current_price>200

  def test_myinfo(self):
    """
    1、打开雪球APP，进入到个人中心信息页面
    2、点击登录，进入到登陆页面
    3、输入用户名密码
    4、点击登录
    :return:
    """
    self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
    self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("登录雪球")').click()
    self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys("12345")
    self.driver.find_element_by_android_uiautomator(
      'new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys("12345")
    time.sleep(2)
    self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()

  def test_scroll_find_element(self):
    self.driver.find_element_by_android_uiautomator('new UiSelector().text("关注")').click()
    self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("似水年华").instance(0))').click()
    time.sleep(5)


  @pytest.mark.parametrize("searchkey, type, expect_price",[
    ('alibaba','BABA','180'),
    ('xiaomi','01810','10')
  ])
  def test_search_01(self, searchkey, type, expect_price):
    """
    1、打开雪球APP
    2、点击搜索框
    3、输入搜索词‘alibaba’or‘xiaomi’
    4、点击一个搜索结果
    5、判断股票价格
    :return:
    """
    self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
    self.driver.implicitly_wait(5)
    self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(searchkey)
    self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/name").click()
    price_element = self.driver.find_element(MobileBy.XPATH, f"//*[@text={type}]/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
    print(price_element)
    current_price = float(price_element)
    assert current_price>float(expect_price)

















# if __name__ == '__main__':
#     pytest.main()



# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '6.0'
# desired_caps['deviceName'] = ''
# desired_caps['appPackage'] = ''
# desired_caps['appActivity'] = ''
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# driver.quit()









