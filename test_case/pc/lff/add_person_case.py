#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-06-26 Created by lff'

import unittest
from pages.pc_pages.lff_organization_institution_page import OrganizationInstitution
from selenium import webdriver
import os
import time
class AddPersonCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.organ_page= OrganizationInstitution(self.driver, path=os.path.dirname(__file__))
        self.organ_page.log.info('[--浏览器打开成功]')
        self.organ_page.login_test_person()
        self.organ_page.switching_enterprises(_enterprise='tongdg艺赛旗', _login_name='童定国')

    def test(self):
        #进入组织机构
        self.organ_page.enter_organization_institution()
        time.sleep(1)
        # 子目录
        self.organ_page.click(self.organ_page.subdirectory_btn)
        time.sleep(1)
        # 添加人员
        self.organ_page.click(self.organ_page.add_person)
        time.sleep(1)
        # 姓名
        self.organ_page.send_keys(self.organ_page.add_name,'张三'+self.organ_page.random_num)
        time.sleep(1)
        # 性别
        self.organ_page.click(self.organ_page.add_sex)
        time.sleep(1)
        # 手机号
        self.organ_page.send_keys(self.organ_page.add_tel,'132'+self.organ_page.random_telnum)
        time.sleep(1)
        # 员工编号
        self.organ_page.send_keys(self.organ_page.add_code,self.organ_page.random_num)
        time.sleep(1)
        # 直属领导
        # 下拉框
        self.organ_page.click(self.organ_page.direct_leader)
        time.sleep(1)
        # 选直属领导
        self.organ_page.click(self.organ_page.sel_direct_leader)
        time.sleep(1)
        # 职级
        self.organ_page.send_keys(self.organ_page.rank_text,'员工'+self.organ_page.random_num)
        time.sleep(1)
        # 角色
        # 下拉框
        self.organ_page.click(self.organ_page.sel_role)
        time.sleep(1)
        # 部门领导
        self.organ_page.click(self.organ_page.role_list[2])
        time.sleep(1)
        # 会计
        self.organ_page.click(self.organ_page.role_list[4])
        time.sleep(1)
        # 出纳
        self.organ_page.click(self.organ_page.role_list[7])
        time.sleep(1)
        #收回角色下拉框
        self.organ_page.click(self.organ_page.pop)
        time.sleep(1)
        # 岗位
        self.organ_page.send_keys(self.organ_page.post_text,'测试'+self.organ_page.random_num)
        time.sleep(1)
        # 邮箱
        self.organ_page.send_keys(self.organ_page.email_text,'lvff@yuanian.com')
        time.sleep(1)
        # 确认按钮
        self.organ_page.click(self.organ_page.submit_btn1)

    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()