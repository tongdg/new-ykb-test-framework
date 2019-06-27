#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-06-13 Created by tongdg'

from pages.pc_pages.approval_page import ApprovalPage
import unittest
from selenium import webdriver
import os


class LoanCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.appro_page = ApprovalPage(driver=self.driver, path=os.path.dirname(__file__))
        # 普通员工登录
        self.appro_page.log.info('--[普通员工登录]')
        self.appro_page.login_ordinary_staff()
        # 切换企业
        self.appro_page.switching_enterprises(_enterprise='tongdg艺赛旗', _login_name='普通员工')
        self.appro_page.log.info('--[切换企业ok,登录ok]')

    def test_loan_process1(self):
        u"""借款申请单-业务-会计-财务经理-出纳"""
        self.appro_page.log.info('--[进入借款申请单-填写借款申请单-断言]')
        self.result = self.appro_page.enter_fill_loan_bill()
        self.assertTrue(self.result, '进入借款申请单-填写借款申请单-断言失败')

        self.appro_page.log.info('--[部门领导登录]')
        self.appro_page.login_department_leader()

        self.appro_page.log.info('--[部门领导查找单据-断言]')
        self.result = self.appro_page.enter_list_find_old_bill()
        self.assertTrue(self.result, '部门领导查找单据断言失败')

        self.appro_page.log.info('--[部门领导审批状态-断言]')
        self.result = self.appro_page.judge_approval_process('审批中')
        self.assertTrue(self.result, '部门领导审批状态断言失败')

        self.appro_page.log.info('--[部门领导业务同意-断言]')
        self.result = self.appro_page.approval_old_agree([''])
        self.assertTrue(self.result, '下一个环节审批领导断言失败')

        self.appro_page.log.info('--[部门领导业务确定-断言]')
        self.result = self.appro_page.old_apply_confirm()
        self.assertTrue(self.result, '部门领导业务审批失败')

        self.appro_page.log.info('--[会计登录]')
        self.appro_page.login_accounting()

        self.appro_page.log.info('--[会计查找单据-断言]')
        self.result = self.appro_page.enter_list_find_finance_loan()
        self.assertTrue(self.result,'会计查找单据断言失败')

        self.appro_page.log.info('--[会计审核状态-断言]')
        self.result = self.appro_page.judge_approval_process('财务初审中')
        self.assertTrue(self.result, '会计审核状态断言失败')

        self.appro_page.log.info('--[会计同意-断言]')
        self.result = self.appro_page.approval_old_agree([''])
        self.assertTrue(self.result, '下一个环节审批领导断言失败')

        self.appro_page.log.info('--[会计确定-断言]')
        self.result = self.appro_page.old_apply_confirm()
        self.assertTrue(self.result, '会计审核失败')

        self.appro_page.log.info('--[财务经理登录]')
        self.appro_page.login_financial_manager()

        self.appro_page.log.info('--[财务经理查找单据-断言]')
        self.result = self.appro_page.enter_list_find_review_loan()
        self.assertTrue(self.result, '财务经理查找单据断言失败')

        self.appro_page.log.info('--[财务经理审批状态-断言]')
        self.result = self.appro_page.judge_approval_process('财务复核中')
        self.assertTrue(self.result, '财务经理审批状态断言失败')

        self.appro_page.log.info('--[财务经理审批同意-断言]')
        self.result = self.appro_page.approval_old_agree([''])
        self.assertTrue(self.result, '下一个环节审批领导断言失败')

        self.appro_page.log.info('--[财务经理审批确定-断言]')
        self.result = self.appro_page.old_apply_confirm()
        self.assertTrue(self.result, '财务经理审批失败')

        self.appro_page.log.info('--[出纳登录]')
        self.appro_page.login_cashier()

        self.appro_page.log.info('--[出纳查找单据-断言]')
        self.result = self.appro_page.enter_list_find_payment()
        self.assertTrue(self.result, '出纳查找单据断言失败')

        self.appro_page.log.info('--[出纳付款状态-断言]')
        self.result = self.appro_page.judge_approval_process('出纳付款中')
        self.assertTrue(self.result, '出纳付款状态失败')

        self.appro_page.log.info('--[出纳支付-断言]')
        self.result = self.appro_page.old_payment()
        self.assertTrue(self.result,'出纳支付失败')

    def test_loan_process2(self):
        u"""借款申请单-业务-会计-加审领导-会计-财务经理-出纳"""
        self.appro_page.log.info('--[进入借款申请单-填写借款申请单-断言]')
        self.result = self.appro_page.enter_fill_loan_bill()
        self.assertTrue(self.result, '进入借款申请单-填写借款申请单-断言失败')

        self.appro_page.log.info('--[部门领导登录]')
        self.appro_page.login_department_leader()

        self.appro_page.log.info('--[部门领导查找单据-断言]')
        self.result = self.appro_page.enter_list_find_old_bill()
        self.assertTrue(self.result, '部门领导查找单据断言失败')

        self.appro_page.log.info('--[部门领导审批状态-断言]')
        self.result = self.appro_page.judge_approval_process('审批中')
        self.assertTrue(self.result, '部门领导审批状态断言失败')

        self.appro_page.log.info('--[部门领导业务同意-断言]')
        self.result = self.appro_page.approval_old_agree([''])
        self.assertTrue(self.result, '下一个环节审批领导断言失败')

        self.appro_page.log.info('--[部门领导业务确定-断言]')
        self.result = self.appro_page.old_apply_confirm()
        self.assertTrue(self.result, '部门领导业务审批失败')

        self.appro_page.log.info('--[会计登录]')
        self.appro_page.login_accounting()

        self.appro_page.log.info('--[会计查找单据-断言]')
        self.result = self.appro_page.enter_list_find_finance_loan()
        self.assertTrue(self.result, '会计查找单据断言失败')

        self.appro_page.log.info('--[会计审核状态-断言]')
        self.result = self.appro_page.judge_approval_process('财务初审中')
        self.assertTrue(self.result, '会计审核状态断言失败')

        self.appro_page.log.info('--[会计加审-断言]')
        self.result = self.appro_page.add_financial_approval_cofirm_loan()
        self.assertTrue(self.result,'会计加审失败')

        self.appro_page.log.info('--[加审领导登录]')
        self.appro_page.login_add_approval()

        self.appro_page.log.info('--[加审领导查找单据-断言]')
        self.result = self.appro_page.enter_list_find_old_bill()
        self.assertTrue(self.result, '加审领导查找单据断言失败')

        self.appro_page.log.info('--[加审领导审批状态-断言]')
        self.result = self.appro_page.judge_approval_process('财务加审中')
        self.assertTrue(self.result, '加审领导审批状态断言失败')

        self.appro_page.log.info('--[加审领导业务同意-断言]')
        self.result = self.appro_page.add_approval_old_agree()
        self.assertTrue(self.result, '加审领导同意断言失败')

        self.appro_page.log.info('--[会计登录]')
        self.appro_page.login_accounting()

        self.appro_page.log.info('--[会计查找单据-断言]')
        self.result = self.appro_page.enter_list_find_finance_loan()
        self.assertTrue(self.result, '会计查找单据断言失败')

        self.appro_page.log.info('--[会计审核状态-断言]')
        self.result = self.appro_page.judge_approval_process('财务初审中')
        self.assertTrue(self.result, '会计审核状态断言失败')

        self.appro_page.log.info('--[会计同意-断言]')
        self.result = self.appro_page.approval_old_agree([''])
        self.assertTrue(self.result, '下一个环节审批领导断言失败')

        self.appro_page.log.info('--[会计确定-断言]')
        self.result = self.appro_page.old_apply_confirm()
        self.assertTrue(self.result, '会计审核失败')

        self.appro_page.log.info('--[财务经理登录]')
        self.appro_page.login_financial_manager()

        self.appro_page.log.info('--[财务经理查找单据-断言]')
        self.result = self.appro_page.enter_list_find_review_loan()
        self.assertTrue(self.result, '财务经理查找单据断言失败')

        self.appro_page.log.info('--[财务经理审批状态-断言]')
        self.result = self.appro_page.judge_approval_process('财务复核中')
        self.assertTrue(self.result, '财务经理审批状态断言失败')

        self.appro_page.log.info('--[财务经理审批同意-断言]')
        self.result = self.appro_page.approval_old_agree([''])
        self.assertTrue(self.result, '下一个环节审批领导断言失败')

        self.appro_page.log.info('--[财务经理审批确定-断言]')
        self.result = self.appro_page.old_apply_confirm()
        self.assertTrue(self.result, '财务经理审批失败')

        self.appro_page.log.info('--[出纳登录]')
        self.appro_page.login_cashier()

        self.appro_page.log.info('--[出纳查找单据-断言]')
        self.result = self.appro_page.enter_list_find_payment()
        self.assertTrue(self.result, '出纳查找单据断言失败')

        self.appro_page.log.info('--[出纳付款状态-断言]')
        self.result = self.appro_page.judge_approval_process('出纳付款中')
        self.assertTrue(self.result, '出纳付款状态失败')

        self.appro_page.log.info('--[出纳支付-断言]')
        self.result = self.appro_page.old_payment()
        self.assertTrue(self.result, '出纳支付失败')

    def test_loan_process3(self):
        u"""借款申请单-业务-会计-加审领导-会计-财务经理-财务总监-出纳"""
        self.appro_page.log.info('--[进入借款申请单-填写借款申请单-断言]')
        self.result = self.appro_page.enter_fill_loan_bill()
        self.assertTrue(self.result, '进入借款申请单-填写借款申请单-断言失败')

        self.appro_page.log.info('--[部门领导登录]')
        self.appro_page.login_department_leader()

        self.appro_page.log.info('--[部门领导查找单据-断言]')
        self.result = self.appro_page.enter_list_find_old_bill()
        self.assertTrue(self.result, '部门领导查找单据断言失败')

        self.appro_page.log.info('--[部门领导审批状态-断言]')
        self.result = self.appro_page.judge_approval_process('审批中')
        self.assertTrue(self.result, '部门领导审批状态断言失败')

        self.appro_page.log.info('--[部门领导业务同意-断言]')
        self.result = self.appro_page.approval_old_agree([''])
        self.assertTrue(self.result, '下一个环节审批领导断言失败')

        self.appro_page.log.info('--[部门领导业务确定-断言]')
        self.result = self.appro_page.old_apply_confirm()
        self.assertTrue(self.result, '部门领导业务审批失败')

        self.appro_page.log.info('--[会计登录]')
        self.appro_page.login_accounting()

        self.appro_page.log.info('--[会计查找单据-断言]')
        self.result = self.appro_page.enter_list_find_finance_loan()
        self.assertTrue(self.result, '会计查找单据断言失败')

        self.appro_page.log.info('--[会计审核状态-断言]')
        self.result = self.appro_page.judge_approval_process('财务初审中')
        self.assertTrue(self.result, '会计审核状态断言失败')

        self.appro_page.log.info('--[会计加审-断言]')
        self.result = self.appro_page.add_financial_approval_cofirm_loan()
        self.assertTrue(self.result,'会计加审失败')

        self.appro_page.log.info('--[加审领导登录]')
        self.appro_page.login_add_approval()

        self.appro_page.log.info('--[加审领导查找单据-断言]')
        self.result = self.appro_page.enter_list_find_old_bill()
        self.assertTrue(self.result, '加审领导查找单据断言失败')

        self.appro_page.log.info('--[加审领导审批状态-断言]')
        self.result = self.appro_page.judge_approval_process('财务加审中')
        self.assertTrue(self.result, '加审领导审批状态断言失败')

        self.appro_page.log.info('--[加审领导业务同意-断言]')
        self.result = self.appro_page.add_approval_old_agree()
        self.assertTrue(self.result, '加审领导同意断言失败')

        self.appro_page.log.info('--[会计登录]')
        self.appro_page.login_accounting()

        self.appro_page.log.info('--[会计查找单据-断言]')
        self.result = self.appro_page.enter_list_find_finance_loan()
        self.assertTrue(self.result, '会计查找单据断言失败')

        self.appro_page.log.info('--[会计审核状态-断言]')
        self.result = self.appro_page.judge_approval_process('财务初审中')
        self.assertTrue(self.result, '会计审核状态断言失败')

        self.appro_page.log.info('--[会计同意-断言]')
        self.result = self.appro_page.approval_old_agree([''])
        self.assertTrue(self.result, '下一个环节审批领导断言失败')

        self.appro_page.log.info('--[会计确定-断言]')
        self.result = self.appro_page.old_apply_confirm()
        self.assertTrue(self.result, '会计审核失败')

        self.appro_page.log.info('--[财务经理登录]')
        self.appro_page.login_financial_manager()

        self.appro_page.log.info('--[财务经理查找单据-断言]')
        self.result = self.appro_page.enter_list_find_review_loan()
        self.assertTrue(self.result, '财务经理查找单据断言失败')

        self.appro_page.log.info('--[财务经理审批状态-断言]')
        self.result = self.appro_page.judge_approval_process('财务复核中')
        self.assertTrue(self.result, '财务经理审批状态断言失败')

        self.appro_page.log.info('--[财务经理审批同意-断言]')
        self.result = self.appro_page.approval_old_agree([''])
        self.assertTrue(self.result, '下一个环节审批领导断言失败')

        self.appro_page.log.info('--[财务经理审批确定-断言]')
        self.result = self.appro_page.add_old_approval_confirm_loan('财务总监')
        self.assertTrue(self.result, '财务经理审批失败')

        self.appro_page.log.info('--[财务总监登录]')
        self.appro_page.login_financial_chief_inspector()

        self.appro_page.log.info('--[财务总监查找单据-断言]')
        self.result = self.appro_page.enter_list_find_review_loan()
        self.assertTrue(self.result, '财务总监查找单据断言失败')

        self.appro_page.log.info('--[财务总监审批状态-断言]')
        self.result = self.appro_page.judge_approval_process('财务总监审核中')
        self.assertTrue(self.result, '财务总监审批状态断言失败')

        self.appro_page.log.info('--[财务总监审批同意-断言]')
        self.result = self.appro_page.approval_old_agree([''])
        self.assertTrue(self.result, '下一个环节审批领导断言失败')

        self.appro_page.log.info('--[财务总监加审确定-断言]')
        self.result = self.appro_page.old_apply_confirm()
        self.assertTrue(self.result, '财务总监加审确定失败')

        self.appro_page.log.info('--[出纳登录]')
        self.appro_page.login_cashier()

        self.appro_page.log.info('--[出纳查找单据-断言]')
        self.result = self.appro_page.enter_list_find_payment()
        self.assertTrue(self.result, '出纳查找单据断言失败')

        self.appro_page.log.info('--[出纳付款状态-断言]')
        self.result = self.appro_page.judge_approval_process('出纳付款中')
        self.assertTrue(self.result, '出纳付款状态失败')

        self.appro_page.log.info('--[出纳支付-断言]')
        self.result = self.appro_page.old_payment()
        self.assertTrue(self.result, '出纳支付失败')

    def tearDown(self):
        # self.appro_page.driver.quit()
        self.appro_page.log.info('--[ 测试用例结束，截图]')

if __name__ == '__main__':
    unittest.main()
