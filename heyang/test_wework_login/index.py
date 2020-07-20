#coding: utf-8
#author = hewangtong
#date = 2020/7/19
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from heyang.test_wework_login.login import Login
from heyang.test_wework_login.register import Register


class Index:
    """
    首页PO
    """
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")

    def goto_register(self):
        """
        1、点击立即注册
        2、进入到注册PO
        :return:
        """
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        return Register(self.driver)


    def goto_login(self):
        """
        1、点击企业登录
        2、进入到企业登录的PO
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        return  Login(self.driver)
