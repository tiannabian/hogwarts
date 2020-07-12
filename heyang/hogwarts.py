#coding: utf-8
#author = hewangtong
#date = 2020/6/27

#coding: utf-8
#author = hewangtong
#date = 2020/7/8
import HTMLTestRunnerNew
import unittest
from HTMLTestRunnerNew import HTMLTestRunner

#
# class TestStringMethods(unittest.TestCase):
#
#     def test_add(self):
#         print("这是一个加法")
#
#     def test_div(self):
#         print("这是一个减法")
#
# class TestDemo(unittest.TestCase):
#
#     def test_demo_01(self):
#         print("这是第一个demo")
#
#     def test_demo_02(self):
#         print("这是第二个demo")
#
# if __name__ == '__main__':
    #方法一：执行当前所有用例
    #unittest.main()
    #方法二：执行指定的测试用例，将要执行的测试用例添加到测试套件里面，批量执行
    #创建一个测试套件，testsuite
    # suite = unittest.TestSuite()
    # suite.addTest(TestStringMethods("test_add"))
    # unittest.TextTestRunner().run(suite)
    #方法三：执行某个测试类
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(TestDemo)
    # suite = unittest.TestSuite([suite1, suite2])
    # unittest.TextTestRunner(verbosity=2).run(suite)
    #
    # suite = unittest.TestSuite()
    #
    # # 添加用例
    # loader = unittest.TestLoader
    # suite.addTest(loader.loadTestsFromTestCase())
    #
    # report_title = "1111"
    # desc = "12345"
    # report_file = './result.html'
    #
    # with open(report_file, 'wb') as report:
    #     runner = HTMLTestRunnerNew.HTMLTestRunner(stream = report, title=report_title, description=desc)
    #     runner.run(suite)
from selenium.webdriver.common.by import By

"""+——+——+——+——+——+——+——————————————
web自动化基础知识整理汇总
$x('//*[@id="1"]//h3')
$('#s_tab a:nth-child(3)')

################ActionChains：执行PC端的鼠标点击，双击，右键，拖拽等事件
actions=ActionChains(driver)
actions.move_to_element(element)
actions.click(element)
actions.perform()
用法二：鼠标移动到某个元素上
action=ActionChains(self.driver)
actions.move_to_element(element)
actions.click(element)
actions.perform()




TouchAction: 模拟PC端和移动端的点击、滑动、拖拽，多点触控等多种手势操作
—————————+——+——+——+——+——+——+——+——+——"""
from selenium import webdriver

class TestHogwarts():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")
    def teardown(self):
        self.driver.quit()

    def test_hogwarts(self):

        # self.driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys("霍格沃兹测试学院")
        # self.driver.find_element(By.ID, "kw").send_keys("霍格沃兹测试学院")
        self.driver.find_element(By.CSS_SELECTOR, "#kw").send_keys("霍格沃兹测试学院")

class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")

    def teardown(self):
        self.driver.quit()

    def test_case_click(self):
        pass






























