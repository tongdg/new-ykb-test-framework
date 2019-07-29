#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from config import zfk_config
from pages.mobile_pages.zfk_mobile_login_Page import Mobile_login_page
import time
class zfk_mobile_LoginCase(unittest.TestCase):
    # 跳转到代客下单界面，并进入到需要测试的企业
    def test_Login_mobile_enterprise(self):
        #普通员工登录
        self.zfk_mobile_login_Page = Mobile_login_page(webdriver.Chrome())
        self.zfk_mobile_login_Page.Login_Person()
        self.zfk_mobile_login_Page.Chionce_Login_staff()

        #审批领导登录
        self.zfk_mobile_login_Page = Mobile_login_page(webdriver.Chrome())
        self.zfk_mobile_login_Page.Login_Person()
        self.zfk_mobile_login_Page.Chionce_Login_leader()

        #会计角色登录
        self.zfk_mobile_login_Page = Mobile_login_page(webdriver.Chrome())
        self.zfk_mobile_login_Page.Login_Person()
        self.zfk_mobile_login_Page.Chionce_Login_accountant()


    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()

