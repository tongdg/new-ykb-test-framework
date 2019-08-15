#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-07-11 Created by lff'

import unittest
from pages.pc_pages.lff_organization_institution_page import OrganizationInstitution
from selenium import webdriver
import os
import time
class AddInstPersonCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.organ_page= OrganizationInstitution(self.driver, path=os.path.dirname(__file__))
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
        # 查找根目录添加的机构点击添加人员
        self.organ_page.find_institutions_add_what('添加人员')
        time.sleep(1)
        # 子目录添加人员
        self.organ_page.add_person_method()
        time.sleep(1)
        # 查找组织机构
        self.organ_page.find_institutions_click()
        # 查找添加的人员点击编辑
        self.organ_page.find_person_edit_what()
        time.sleep(1)
        # 编辑人员
        self.organ_page.edit_person_method()
        time.sleep(1)


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()