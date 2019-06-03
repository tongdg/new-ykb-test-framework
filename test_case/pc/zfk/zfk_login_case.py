#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-05-29 Created by Zhangfukai'

import unittest
from pages.pc_pages.zfk_login_HouTaipage import Login_HouTaiPage
from selenium import webdriver
import os
import time
class LoginCase(unittest.TestCase):
    def setUp(self):
        self.longin_page = Login_HouTaiPage(webdriver.Chrome(),os.getcwd())
        self.longin_page.login_person()
        time.sleep(500000)


    def test_login_case(self):
        pass
    def tearDown(self):
        print("登录管理后台登录成功")
if __name__=="__main__":
    unittest.main()

