#coding: utf-8
#author = hewangtong
#date = 2020/7/19
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from heyang.test_wework.base_page import BasePage


class AddMember(BasePage):
    """
    添加成员
    """
    def add_member(self):
        """
        :return:
        """
        self.find(By.CSS_SELECTOR, "#username").send_keys("qwee")
        self.find(By.CSS_SELECTOR, "#memberAdd_acctid").send_keys("12345678")
        self.find(By.CSS_SELECTOR, "#memberAdd_phone").send_keys("18810903988")
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
