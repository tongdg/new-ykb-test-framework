#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-05-29 Created by Zhangfukai'

import unittest
from pages.pc_pages.zfk_Valet_orderPage import Valet_orderPage
from pages.pc_pages.zfk_login_HouTaipage import Login_HouTaiPage
from selenium import webdriver
import os
import time
class LoginCase(unittest.TestCase):
    def setUp(self):
        self.longin_page = Login_HouTaiPage(webdriver.Chrome(),os.path.dirname(__file__))
        #等录至后台的操作
        self.longin_page.Login_Person()

    def test_login_case(self):
        # 代课下单_模块
        self.Search_page = Valet_orderPage()
        self.Search_page.Chionce_enterprise()
    def tearDown(self):
        print("登录测成功")


if __name__=="__main__":
    unittest.main()

