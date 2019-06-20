#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-06-06 Created by tongdg'

from selenium import webdriver
import unittest
from pages.pc_pages.bill_page import BillPage
import os

class BillCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.bill_page = BillPage(driver=self.driver,path=os.path.dirname(__file__))
        # 普通员工登录
        self.bill_page.login_ordinary_staff()
        # 切换企业
        self.bill_page.switching_enterprises(_enterprise='tongdg艺赛旗',_login_name='普通员工')
        self.bill_page.log.info('--[切换企业ok,登录ok]')

    def test_enter_fill_evecation_bill(self):
        u"""进入出差申请单-填写出差申请单-断言"""
        self.bill_page.log.info('--[进入出差申请单-填写出差申请单-断言]')
        self.evecation_result = self.bill_page.enter_fill_evecation_bill()
        self.assertTrue(self.evecation_result,'进入出差申请单-填写出差申请单-断言失败')

    def test_enter_fill_loan_bill(self):
        self.bill_page.log.info('--[进入借款申请单-填写借款申请单-断言]')
        self.loan_result = self.bill_page.enter_fill_loan_bill()
        self.assertTrue(self.loan_result,'进入借款申请单-填写借款申请单-断言失败')
        u"""进入借款申请单-填写借款申请单-断言"""

    def test_enter_fill_travel_reimbursement_bill(self):
        u"""进入差旅报销单-填写差旅报销单-断言"""
        self.bill_page.log.info('--[进入差旅报销单--填写差旅报销单-断言]')
        self.travel_result = self.bill_page.enter_fill_travel_reimbursement_bill()
        self.assertTrue(self.travel_result,'进入差旅报销单--填写差旅报销单-断言失败')

    def test_enter_fill_cost_bill(self):
        u"""进入费用报销单-填写费用报销单-断言"""
        self.bill_page.log.info('--[进入费用报销单-填写费用报销单-断言]')
        self.cost_result = self.bill_page.enter_fill_cost_bill()
        self.assertTrue(self.cost_result,'进入费用报销单-填写费用报销单-断言失败')

    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()