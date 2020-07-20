#coding: utf-8
#author = hewangtong
#date = 2020/7/19#
import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Register:
    """
    注册页面PO
    """
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def register(self):
        """
        输入内容
        点击下拉框
        :return:
        """
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#corp_name").send_keys("test12345")
        self.driver.find_element(By.CSS_SELECTOR, "#manager_name").send_keys("wertyyu")
        return True
