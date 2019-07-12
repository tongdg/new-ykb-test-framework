#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-06-10 Created by tongdg'

from pages.mobile_pages.index_page import IndexPage
import unittest
from selenium import webdriver
import os
import time

class TestIndexCase(unittest.TestCase):

    def setUp(self):
        mobile_emulation = {"deviceName": "iPhone 6/7/8"}
        option = webdriver.ChromeOptions()
        option.add_experimental_option('mobileEmulation', mobile_emulation)
        self.driver = webdriver.Chrome(chrome_options=option)
        self.index_page = IndexPage(self.driver, path=os.path.dirname(__file__))
        self.index_page.login_test_person()

    def test_index(self):
        self.index_page.create_train_bill()

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
