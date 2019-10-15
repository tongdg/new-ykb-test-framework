#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-07-25 Created by lff'

import unittest
from pages.pc_pages.lff_organization_institution_page import OrganizationInstitution
from selenium import webdriver
import os
import time
class AddInstEditCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.organ_page = OrganizationInstitution(self.driver, path=os.path.dirname(__file__))
        self.organ_page.log.info('[--浏览器打开成功]')
        self.organ_page.login_test_person()
        self.organ_page.switching_enterprises(_enterprise='tongdg艺赛旗', _login_name='童定国')

    def test_222(self):
        # 进入开票信息
        self.organ_page.enter_invoice_information()
        time.sleep(1)
        # 新增开票信息
        self.organ_page.add_invoice_info()
        time.sleep(1)
        # 修改开票信息
        self.organ_page.update_inv_info()
        time.sleep(1)
        #删除开票信息
        self.organ_page.del_inv_info()
        time.sleep(1)


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()