#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-05-29 Created by tongdg'

import unittest
from pages.pc_pages.login_page import LoginPage
from selenium import webdriver

class LoginCase(unittest.TestCase):
    def setUp(self):
        self.longin_page = LoginPage(webdriver.Chrome())
        self.longin_page.login_mention_person()

    def test_login_case(self):
        pass


    def tearDown(self):
        self.longin_page.quit()
