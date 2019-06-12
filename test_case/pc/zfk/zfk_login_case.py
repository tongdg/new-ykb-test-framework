#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-05-29 Created by Zhangfukai'

import unittest
from pages.pc_pages.zfk_Valet_orderPage import Valet_orderPage
from selenium import webdriver
import os
import time
class LoginCase(unittest.TestCase):

    def setUp(self):
        self.Valet_orderPage = Valet_orderPage(webdriver.Chrome(),os.path.dirname(__file__))

    def test_Login_enterprise (self):
        self.Valet_orderPage.Login_Person()#登录账号
        self.Valet_orderPage.Chionce_enterprise()#跳转到代客下单界面，并进入到需要测试的企业



    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()

