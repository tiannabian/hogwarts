import json

import yaml
from selenium.webdriver.android.webdriver import WebDriver

from mishop_app.page.handle_black import handle_black


class BasePage:
    """基础数据PO"""
    _params = {}

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    @handle_black
    def find(self, by, locator=None):
        if locator is None:
            result = self.driver.find_element(*by)
        else:
            result = self.driver.find_element(by, locator)
        return result

    def finds(self, by, locator=None):
        if locator is None:
            return self.driver.find_elements(*by)
        else:
            return self.driver.find_elements(by, locator)

    def set_implicitly_wait(self, second):
        self.driver.implicitly_wait(second)

    def steps(self, path, name):
        with open(path, encoding="utf-8") as f:
            steps = yaml.safe_load(f)[name]
        raw = json.dumps(steps)
        for key, value in self._params.items():
            raw = raw.replace('${' + key + '}', value)
        steps = json.loads(raw)
        for step in steps:
            if "action" in step.keys():
                action = step["action"]
                if "click" == action:
                    self.find(step["by"], step["locator"]).click()
                if "send" == action:
                    self.find(step["by"], step["locator"]).send_keys(step["value"])
                if "len > 0" == action:
                    eles = self.finds(step["by"], step["locator"])
                    return len(eles) > 0


"""
店：  store
商：  business
本月指标：  new_month_index
销售数据：   sales_data
分货规则：   distributionrules
北京线下：  new_capa_ms_view   
本月销售汇总：   new_month_data_view
专卖店返利数据：   new_rebate_data_view
当日销售：  new_today_data_view
本月合作商排名： new_business_top_view
本月门店排名：  new_store_top_view
零售学院：  Retail College
我的：  My view


"""




