#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-06-25 Created by lff'

import unittest
from pages.pc_pages.lff_organization_institution_page import OrganizationInstitution
from selenium import webdriver
import os
import time
class AddInstitutionCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.organ_page = OrganizationInstitution(self.driver, path=os.path.dirname(__file__))
        self.organ_page.log.info('[--浏览器打开成功]')
        self.organ_page.login_test_person()
        self.organ_page.switching_enterprises(_enterprise='tongdg艺赛旗', _login_name='童定国')

    def test1(self):
        self.organ_page.enter_organization_institution()
        self.organ_page.click(self.organ_page.subdirectory_btn)
        self.organ_page.click(self.organ_page.add_institution1)

    def tearDown(self):
        time.sleep(20)
        pass

if __name__ == '__main__':
    unittest.main()
