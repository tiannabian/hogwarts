from selenium.webdriver.android.webdriver import WebDriver


class BasePage:
    """基础数据PO"""
    def __init__(self, driver: WebDriver = None):
        self.driver = driver