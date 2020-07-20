import shelve
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Test():
  def setup_method(self, method):
    options = Options()
    #和浏览器打开的调试窗口进行通信
    #浏览器要使用--remote-debugging-port=9222
    options.debugger_address = "127.0.0.1:9222"
    self.driver = webdriver.Chrome(options=options)

  # def teardown_method(self, method):
  #   self.driver.quit()

  def test_baidu(self):
    self.driver.get("https://www.baidu.com/")
    self.driver.find_element(By.ID, "kw").send_keys("霍格沃兹测试学院")
    self.driver.find_element(By.ID, "su").click()
    time.sleep(2)
    self.driver.find_element(By.LINK_TEXT, "霍格沃兹测试学院 – 测试开发工程师的黄埔军校").click()

  def test_wework(self):
    self.driver.get("https://work.weixin.qq.com/")
    #创建或者打开一个数据库
    db = shelve.open("cookies")
    # cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1595056046'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a6499289'}, {'domain': '.qq.com', 'expiry': 1595056066, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688851936808918'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688851936808918'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '5124164772250655'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'kd0GumIO-aLYbx155IAkwtEpa3_rRobjMJEV7j0LAxzbdbGedAUxdfC3SokVyeW0'}, {'domain': '.qq.com', 'expiry': 1595142438, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.401794814.1595049362'}, {'domain': 'work.weixin.qq.com', 'expiry': 1595080897, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '34vqqr4'}, {'domain': '.qq.com', 'expiry': 1895578723, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/', 'secure': False, 'value': '60f43413a05feb99'}, {'domain': '.work.weixin.qq.com', 'expiry': 1595080897, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1658128038, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1768954037.1594901102'}, {'domain': '.work.weixin.qq.com', 'expiry': 1597648046, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-cn'}, {'domain': '.qq.com', 'expiry': 1597074957, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/', 'secure': False, 'value': '1442678679'}, {'domain': '.qq.com', 'expiry': 1595575034, 'httpOnly': False, 'name': 'psrf_qqaccess_token', 'path': '/', 'secure': False, 'value': '72D7BE0F4ECB885DDC9A3FF9FFEC27B1'}, {'domain': '.qq.com', 'expiry': 1595575034, 'httpOnly': False, 'name': 'psrf_qqunionid', 'path': '/', 'secure': False, 'value': '2625521B3E5E33D13FF20E643A2B73EB'}, {'domain': '.qq.com', 'expiry': 1595575034, 'httpOnly': False, 'name': 'psrf_access_token_expiresAt', 'path': '/', 'secure': False, 'value': '1595575034'}, {'domain': '.qq.com', 'expiry': 2147483649, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 't2ypjGf4FA'}, {'domain': '.qq.com', 'expiry': 1595575034, 'httpOnly': False, 'name': 'psrf_qqrefresh_token', 'path': '/', 'secure': False, 'value': '07C5A2E5D285B4B75547FD3D2C95C828'}, {'domain': '.qq.com', 'expiry': 2147483646, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': 'f6a92c7c1c8a3ff3e1b0d3e1a17d25ab2bc707e8b0dd45d905a3a1883ac8a5d0'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/', 'secure': False, 'value': '1442678679'}, {'domain': '.qq.com', 'expiry': 1900767406, 'httpOnly': False, 'name': 'mobileUV', 'path': '/', 'secure': False, 'value': '1_17121a532ad_ff50'}, {'domain': '.qq.com', 'expiry': 1595575034, 'httpOnly': False, 'name': 'psrf_qqopenid', 'path': '/', 'secure': False, 'value': '16D0945258C9DA995660B19CB1B75859'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324976151351'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '24604804'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '1709671424'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'jjT2_0ykGb4VguvyjVvx1QUElFMtZ-ad5KlUnGVTHduZQl0o_wWIPyJRd3ZMdmjmM0afH95xg9B9lIdjpts79k0fuNysvjLFp33ZVve48c_8xbjk3MDJKR1sxDMuf1MF3PpB0pCxY-raMCWVUIiMvlpGEdCtPKZrErAtE6bKVsCBCHtlSo05D5OiJdO0sVNPAGY2pGdKrCN9Tr51mq_3X4VCKHqPFbK9QqdCQSozObKULZaYOTUg7VgczRirOuX2v0jj48EpLPmR1WXKX_V7Bg'}, {'domain': '.qq.com', 'expiry': 1892378384, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': False, 'value': '0_5dff641052650'}, {'domain': '.work.weixin.qq.com', 'expiry': 1626592046, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1594901114,1595054255'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}]
    #将数据存储到shelve中
    # db["cookies"] = cookies
    #取出数据
    cookies = db["cookies"]
    #获取cookies
    # cookies = self.driver.get_cookies()
    # print(cookies)
    #cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1595056046'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a6499289'}, {'domain': '.qq.com', 'expiry': 1595056066, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688851936808918'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688851936808918'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '5124164772250655'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'kd0GumIO-aLYbx155IAkwtEpa3_rRobjMJEV7j0LAxzbdbGedAUxdfC3SokVyeW0'}, {'domain': '.qq.com', 'expiry': 1595142438, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.401794814.1595049362'}, {'domain': 'work.weixin.qq.com', 'expiry': 1595080897, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '34vqqr4'}, {'domain': '.qq.com', 'expiry': 1895578723, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/', 'secure': False, 'value': '60f43413a05feb99'}, {'domain': '.work.weixin.qq.com', 'expiry': 1595080897, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1658128038, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1768954037.1594901102'}, {'domain': '.work.weixin.qq.com', 'expiry': 1597648046, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-cn'}, {'domain': '.qq.com', 'expiry': 1597074957, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/', 'secure': False, 'value': '1442678679'}, {'domain': '.qq.com', 'expiry': 1595575034, 'httpOnly': False, 'name': 'psrf_qqaccess_token', 'path': '/', 'secure': False, 'value': '72D7BE0F4ECB885DDC9A3FF9FFEC27B1'}, {'domain': '.qq.com', 'expiry': 1595575034, 'httpOnly': False, 'name': 'psrf_qqunionid', 'path': '/', 'secure': False, 'value': '2625521B3E5E33D13FF20E643A2B73EB'}, {'domain': '.qq.com', 'expiry': 1595575034, 'httpOnly': False, 'name': 'psrf_access_token_expiresAt', 'path': '/', 'secure': False, 'value': '1595575034'}, {'domain': '.qq.com', 'expiry': 2147483649, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 't2ypjGf4FA'}, {'domain': '.qq.com', 'expiry': 1595575034, 'httpOnly': False, 'name': 'psrf_qqrefresh_token', 'path': '/', 'secure': False, 'value': '07C5A2E5D285B4B75547FD3D2C95C828'}, {'domain': '.qq.com', 'expiry': 2147483646, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': 'f6a92c7c1c8a3ff3e1b0d3e1a17d25ab2bc707e8b0dd45d905a3a1883ac8a5d0'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/', 'secure': False, 'value': '1442678679'}, {'domain': '.qq.com', 'expiry': 1900767406, 'httpOnly': False, 'name': 'mobileUV', 'path': '/', 'secure': False, 'value': '1_17121a532ad_ff50'}, {'domain': '.qq.com', 'expiry': 1595575034, 'httpOnly': False, 'name': 'psrf_qqopenid', 'path': '/', 'secure': False, 'value': '16D0945258C9DA995660B19CB1B75859'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324976151351'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '24604804'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '1709671424'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'jjT2_0ykGb4VguvyjVvx1QUElFMtZ-ad5KlUnGVTHduZQl0o_wWIPyJRd3ZMdmjmM0afH95xg9B9lIdjpts79k0fuNysvjLFp33ZVve48c_8xbjk3MDJKR1sxDMuf1MF3PpB0pCxY-raMCWVUIiMvlpGEdCtPKZrErAtE6bKVsCBCHtlSo05D5OiJdO0sVNPAGY2pGdKrCN9Tr51mq_3X4VCKHqPFbK9QqdCQSozObKULZaYOTUg7VgczRirOuX2v0jj48EpLPmR1WXKX_V7Bg'}, {'domain': '.qq.com', 'expiry': 1892378384, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': False, 'value': '0_5dff641052650'}, {'domain': '.work.weixin.qq.com', 'expiry': 1626592046, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1594901114,1595054255'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}]
    for cookie in cookies:
      if "expiry" in  cookie.keys():
        cookie.pop("expiry")
      #把字典加入到driver的cookie中
      self.driver.add_cookie(cookie)
    self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
    self.driver.find_element(By.ID, "menu_contacts").click()
    db.close()








  
