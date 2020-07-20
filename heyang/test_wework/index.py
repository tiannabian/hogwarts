#coding: utf-8
#author = hewangtong
#date = 2020/7/19
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from heyang.test_wework.add_member import AddMember
from heyang.test_wework.base_page import BasePage


class Index(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    def goto_add_member(self):
        """
        添加成员
        :return:
        """
        def add_member_condition(x):
            """
            改写显示等待条件
            :param x:
            :return:
            """
            element = len(self.finds(By.ID, "username"))
            if element <= 0:
                self.find(By.CSS_SELECTOR, ".js_has_member>div:nth-child(1)>a:nth-child(2)").click()
            #如果username不存在，就会触发until中的死循环
            return element > 0

        #self.find(By.CSS_SELECTOR, ".index_service_cnt_item_title").click()
        self.find(By.CSS_SELECTOR, "#menu_contacts").click()
        self.wait_for_condition(add_member_condition)

        return AddMember(self._driver)

    def goto_import_address(self):
        """
        导入通讯录
        :return:
        """
        self._driver.find_elements_by_xpath("//span[@class='index_service_cnt_item_title']")[1].click()

    def goto_join_member(self):
        """
        成员加入
        :return:
        """