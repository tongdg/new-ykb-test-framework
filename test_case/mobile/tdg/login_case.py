#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-06-20 Created by tongdg'

import unittest
from pages.mobile_pages.login_page import LoginPage
from selenium import webdriver
import os
import time

class LoginCase(unittest.TestCase):

    def setUp(self):
        mobile_emulation = {"deviceName": "iPhone 6/7/8"}
        option = webdriver.ChromeOptions()
        option.add_experimental_option('mobileEmulation', mobile_emulation)
        self.driver = webdriver.Chrome(chrome_options=option)
        self.longin_page = LoginPage(self.driver, path=os.path.dirname(__file__))
        self.longin_page.log.info('[--浏览器打开成功]')

    def test_login_case(self):
        u"""登录测试用例"""
        self.longin_page.log.info('[--tongdg登录测试用例开始]')
        self.login_result = self.longin_page.login_test_person()
        self.assertTrue(self.login_result)

        self.longin_page.log.info('[--公司领导登录测试用例开始]')
        self.login_result = self.longin_page.login_company_leader()
        self.assertTrue(self.login_result)

        self.longin_page.log.info('[--出纳登录测试用例开始]')
        self.login_result = self.longin_page.login_cashier()
        self.assertTrue(self.login_result)

        self.longin_page.log.info('[--财务经理登录测试用例开始]')
        self.login_result = self.longin_page.login_financial_manager()
        self.assertTrue(self.login_result)

        self.longin_page.log.info('[--会计登录测试用例开始]')
        self.login_result = self.longin_page.login_accounting()
        self.assertTrue(self.login_result)

        self.longin_page.log.info('[--部门领导登录测试用例开始]')
        self.login_result = self.longin_page.login_department_leader()
        self.assertTrue(self.login_result)

        self.longin_page.log.info('[--项目经理登录测试用例开始]')
        self.login_result = self.longin_page.login_project_manager()
        self.assertTrue(self.login_result)

        self.longin_page.log.info('[--登录测试用例开始]')
        self.login_result = self.longin_page.login_financial_chief_inspector()
        self.assertTrue(self.login_result)

    def tearDown(self):
        self.longin_page.log.info('[--登录测试用例结束，截图]')

if __name__=='__main__':
    unittest.main()
