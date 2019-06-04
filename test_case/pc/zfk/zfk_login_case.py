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
        self.longin_page = Login_HouTaiPage(webdriver.Chrome(),os.path.dirname(__file__))
        self.longin_page.login_person()
        time.sleep(500000)


    def test_login_case(self):
        pass
    def tearDown(self):
<<<<<<< HEAD:test_case/pc/zfk/zfk_login_case.py
        print("登录管理后台登录成功")
=======
        print("登录测成功")

>>>>>>> 46d3cf866c413132f8841c9d293367ff32254b69:test_case/mobile/zfk/login_case.py
if __name__=="__main__":
    unittest.main()

