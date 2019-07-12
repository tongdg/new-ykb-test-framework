#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-07-10 Created by lff'

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

    def test(self):
        # 进入组织机构
        self.organ_page.enter_organization_institution()
        time.sleep(1)
        # 根目录添加机构
        self.organ_page.add_institution_method()
        time.sleep(1)
        # 查找根目录添加的机构点击编辑
        self.organ_page.find_institution_edit_what('编辑')
        time.sleep(1)
        # 编辑机构
        self.organ_page.edit_ins_method()
        time.sleep(1)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()