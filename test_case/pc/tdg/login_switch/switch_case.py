#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-06-04 Created by tongdg'
from pages.pc_pages.index_page import IndexPage
import unittest
from selenium import webdriver
import os
from config.tdg_config import get_enterprise_login

class SwitchCase(unittest.TestCase):


    def setUp(self):
        self.data = get_enterprise_login()
        self.driver = webdriver.Chrome()
        self.index_case = IndexPage(self.driver,path=os.path.dirname(__file__))
        self.index_case.log.info('--[浏览器打开成功]')
        self.index_case.login_test_person()

    def test_switching_enterprise(self):
        u"""切换企业测试用例--企业正确--用户名正确"""
        self.index_case.log.info('--[切换企业测试用例--企业正确--用户名正确]')
        # 返回切换结果
        self.switch_result = self.index_case.switching_enterprises(self.data[0][0], self.data[0][1])
        # 断言切换企业是否成功
        self.assertTrue(self.switch_result, '企业正确--用户名正确断言失败!')

    def test_switching_enterprise2(self):
        u"""切换企业测试用例--企业正确--用户名错误"""
        self.index_case.log.info('--[切换企业测试用例--企业正确--用户名错误]')
        # 返回切换结果
        self.switch_result = self.index_case.switching_enterprises(self.data[1][0], self.data[1][1])
        # 断言切换企业是否成功
        self.assertFalse(self.switch_result, '企业正确--用户名错误断言失败!')

    def test_switching_enterprise3(self):
        u"""切换企业测试用例--企业错误--用户名错误"""
        self.index_case.log.info('--[切换企业测试用例--企业错误--用户名错误]')
        # 返回切换结果
        self.switch_result = self.index_case.switching_enterprises(self.data[2][0], self.data[2][1])
        # 断言切换企业是否成功
        self.assertFalse(self.switch_result, '企业错误--用户名错误断言失败!')

    def test_switching_enterprise4(self):
        u"""切换企业测试用例--企业错误--用户名正确"""
        self.index_case.log.info('--[切换企业测试用例--企业错误--用户名正确]')
        # 返回切换结果
        self.switch_result = self.index_case.switching_enterprises(self.data[3][0], self.data[3][1])
        # 断言切换企业是否成功
        self.assertFalse(self.switch_result, '企业错误--用户名正确断言失败!')

    def test_sign_out(self):
        u"""退出测试用例"""
        self.index_case.log.info('--[退出测试用例]')
        self.sign_out_result = self.index_case.singn_out()
        self.assertTrue(self.sign_out_result,'退出成功断言成功!')

    def tearDown(self):
        # self.index_case.driver.quit()
        self.index_case.log.info('--[测试用例结束，截图]')

if __name__ == '__main__':
    unittest.main()










    def tearDown(self):
        pass



if __name__ == '__main__':
    unittest.main()
