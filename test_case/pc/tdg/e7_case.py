#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-06-10 Created by tongdg'

from pages.pc_pages.e7_page import E7Page
import unittest
from selenium import webdriver
import os
import time

class E7Case(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.e7_page = E7Page(self.driver,os.path.dirname(__file__))

    def test_e7(self):
        self.e7_page.e7_login()
        self.e7_page.enter_time_manage()
        self.e7_page.multiple_execute_task(['SyncAllCOAObjectJob','creditMail','updateU8VoucherNumJob'])

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()