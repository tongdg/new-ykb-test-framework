#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-06-26 Created by tongdg'

from pages.pc_pages.approval_page import ApprovalPage
import unittest
from selenium import webdriver
import os


class PurchaseBillCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.appro_page = ApprovalPage(driver=self.driver, path=os.path.dirname(__file__))
        # 普通员工登录
        self.appro_page.log.info('--[普通员工登录]')
        self.appro_page.login_ordinary_staff()
        # 切换企业
        self.appro_page.switching_enterprises(_enterprise='tongdg艺赛旗', _login_name='普通员工')
        self.appro_page.log.info('--[切换企业ok,登录ok]')

    def test(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

