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
        #进入组织机构
        self.organ_page.enter_organization_institution()
        time.sleep(1)
        # 子目录
        self.organ_page.click(self.organ_page.subdirectory_btn)
        time.sleep(1)
        # 添加机构
        self.organ_page.click(self.organ_page.add_institution1)
        time.sleep(1)
        self.organ_page.send_keys(self.organ_page.institution_name,'自动化测试小小组'+self.organ_page.random_num)
        time.sleep(1)
        # 机构编码
        self.organ_page.send_keys(self.organ_page.institution_code,self.organ_page.random_num)
        time.sleep(1)
        # 机构负责人
        # 下拉按钮
        self.organ_page.click(self.organ_page.institution_person)
        time.sleep(1)
        # 搜索机构负责人
        self.organ_page.send_keys(self.organ_page.institution_person_text,'童定国')
        time.sleep(1)
        # 选机构负责人
        self.organ_page.click(self.organ_page.institution_person_sel)
        time.sleep(1)
        # 确定按钮
        self.organ_page.click(self.organ_page.submit_btn)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
