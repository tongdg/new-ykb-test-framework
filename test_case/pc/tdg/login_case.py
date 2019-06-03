#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-05-29 Created by tongdg'

import unittest
from pages.pc_pages.zfk_login_page import LoginPage
from selenium import webdriver
import os

class LoginCase(unittest.TestCase):
    def setUp(self):
        self.longin_page = LoginPage(driver=webdriver.Chrome(),path=os.path.dirname(__file__))
        self.longin_page.log.info('[-----LoginCase begin execution-----]')
        self.longin_page.login_mention_person()

    def test_login_case(self):
        self.longin_page.log.info('[-----LoginCase in execution-----]')
        print('11111')

    def tearDown(self):
        self.longin_page.log.info('[-----LoginCase end of execution-----]')
        print('22222')
        self.longin_page.quit()

if __name__=='__main__':
    unittest.main()