#coding: utf-8
#author = hewangtong
#date = 2020/6/27

#coding: utf-8
#author = hewangtong
#date = 2020/7/8
import HTMLTestRunnerNew
import unittest
from HTMLTestRunnerNew import HTMLTestRunner


class TestStringMethods(unittest.TestCase):

    def test_add(self):
        print("这是一个加法")

    def test_div(self):
        print("这是一个减法")

class TestDemo(unittest.TestCase):

    def test_demo_01(self):
        print("这是第一个demo")

    def test_demo_02(self):
        print("这是第二个demo")

if __name__ == '__main__':
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

    suite = unittest.TestSuite()

    # 添加用例
    loader = unittest.TestLoader
    suite.addTest(loader.loadTestsFromTestCase())

    report_title = "1111"
    desc = "12345"
    report_file = './result.html'

    with open(report_file, 'wb') as report:
        runner = HTMLTestRunnerNew.HTMLTestRunner(stream = report, title=report_title, description=desc)
        runner.run(suite)




