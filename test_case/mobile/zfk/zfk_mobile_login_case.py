#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-05-29 Created by Zhangfukai'
import unittest
from selenium import webdriver
from pages.mobile_pages.zfk_mobile_login_Page import Mobile_login_page
import time
class zfk_mobile_LoginCase(unittest.TestCase):
    def setUp(self):
        self.zfk_mobile_login_Page = Mobile_login_page(webdriver.Chrome())
        self.zfk_mobile_login_Page.Login_Person() # 登录账号
        self.zfk_mobile_login_Page.Chionce_enterprise()
        # 跳转到代客下单界面，并进入到需要测试的企业
    def test_Login_mobile_enterprise(self):
        #这里切换成移动端模式
        options = webdriver.ChromeOptions()
        mobileEmulation = {'deviceName': 'iPhone 6 Plus'}
        options.add_experimental_option('mobileEmulation', mobileEmulation)
        driver=webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
        MobileUrl=self.zfk_mobile_login_Page.Get_mobile_url()
        # 访问云快报移动端首页
        driver.get(MobileUrl)
        time.sleep(10)
    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()

