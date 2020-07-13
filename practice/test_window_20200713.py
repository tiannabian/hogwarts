#coding: utf-8
#author = hewangtong
#date = 2020/7/13

import time
import allure
import pytest
from selenium import webdriver
class TestWindow():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_window(self):
        self.driver.find_element_by_partial_link_text('登录').click()
        print(self.driver.current_window_handle)
        self.driver.find_element_by_partial_link_text("立即注册").click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)

        window = self.driver.window_handles
        self.driver.switch_to.window(window[-1])
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("username")



        time.sleep(3)