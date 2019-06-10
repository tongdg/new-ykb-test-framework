#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-05-29 Created by tongdg'

import unittest
from pages.pc_pages.login_page import LoginPage
from selenium import webdriver
import os

class LoginCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.longin_page = LoginPage(self.driver, path=os.path.dirname(__file__))
        self.longin_page.log.info('[--浏览器打开成功]')

    def test_login_case(self):
        u"""登录测试用例"""
        self.longin_page.log.info('[--登录测试用例开始]')
        self.login_result = self.longin_page.login_test_person()
        self.assertTrue(self.login_result)

    def tearDown(self):
        self.longin_page.log.info('[--登录测试用例结束，截图]')

if __name__=='__main__':
    unittest.main()
