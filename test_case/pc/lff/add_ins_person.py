#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-07-01 Created by lff'

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
        #根目录添加机构
        self.organ_page.add_institution_methond()
        time.sleep(1)
        # 查找根目录添加的机构点击添加机构
        self.organ_page.find_institution_add_what('添加机构')
        time.sleep(1)
        # 子目录添加机构
        self.organ_page.add_institutions_methond()
        time.sleep(1)
        # 查找根目录添加的机构点击添加人员
        self.organ_page.find_institutions_add_what('添加人员')
        time.sleep(1)
        #子目录添加人员
        self.result = self.organ_page.add_person_methond()
        self.assertTrue(self.result, '【断言】添加人员报错')
        time.sleep(1)
        # 查找根目录添加的机构点击添加人员
        self.organ_page.find_institutions_update_what('修改上级部门')
        time.sleep(1)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()