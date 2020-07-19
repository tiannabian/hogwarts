#coding: utf-8
#author = hewangtong
#date = 2020/7/18
import pytest
from appium import webdriver

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
    self.driver.quit()

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









# if __name__ == '__main__':
#     pytest.main()



# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '6.0'
# desired_caps['deviceName'] = ''
# desired_caps['appPackage'] = ''
# desired_caps['appActivity'] = ''
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# driver.quit()









