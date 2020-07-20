#coding: utf-8
#author = hewangtong
#date = 2020/7/19
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from heyang.test_wework_login.register import Register


class Login:
    """
    登录页面PO
    """
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def scan(self):
        """
        扫描二维码
        :return:
        """
        pass

    def goto_register(self):
        """
        1、点击企业注册
        2、进去到注册PO
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR, ".login_registerBar_link").click()
        return  Register(self.driver)