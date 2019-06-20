#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-06-17 Created by tongdg'

from pages.pc_pages.approval_page import ApprovalPage
import unittest
from selenium import webdriver
import os

class CostBillCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.appro_page = ApprovalPage(driver=self.driver, path=os.path.dirname(__file__))
        # 普通员工登录
        self.appro_page.log.info('--[普通员工登录]')
        self.appro_page.login_ordinary_staff()
        # 切换企业
        self.appro_page.switching_enterprises(_enterprise='tongdg艺赛旗', _login_name='普通员工')
        self.appro_page.log.info('--[切换企业ok,登录ok]')

    def test_cost_bill_process1(self):
        u"""费用报销单-会签（项目）-业务-财务-复核-出纳"""
        self.appro_page.log.info('--[ 进入费用报销单-填写费用报销单-断言]')
        self.result = self.appro_page.enter_fill_cost_bill(project='ykb-测试项目')
        self.assertTrue(self.result, '进入费用报销单-填写费用报销单-断言失败')

        self.appro_page.log.info('--[ 项目经理登录]')
        self.result = self.appro_page.login_project_manager()
        self.assertTrue(self.result, '项目经理登录失败')

        self.appro_page.log.info('--[ 项目经理查找单据-断言]')
        self.result = self.appro_page.enter_list_find_new_bill()
        self.assertTrue(self.result, '项目经理查找单据失败')

        self.appro_page.log.info('--[ 项目经理会签状态-断言]')
        self.result = self.appro_page.judge_new_approval_process('审批中')
        self.assertTrue(self.result,'项目经理会签状态错误')

        self.appro_page.log.info('--[ 项目经理同意-断言]')
        self.result = self.appro_page.approval_new_agree('部门领导')
        self.assertTrue(self.result, '下一个环节审批领导断言失败')

        self.appro_page.log.info('--[ 项目经理会签确定-断言]')
        self.result = self.appro_page.new_bill_confirm_approval()
        self.assertTrue(self.result, '项目经理会签审批失败')

        self.appro_page.log.info('--[ 部门领导登录]')
        self.result = self.appro_page.login_department_leader()
        self.assertTrue(self.result, '部门领导登录失败')

        self.appro_page.log.info('--[ 部门领导查找单据-断言]')
        self.result = self.appro_page.enter_list_find_new_bill()
        self.assertTrue(self.result, '部门领导查找单据失败')

        self.appro_page.log.info('--[ 部门领导业务审批状态-断言]')
        self.result = self.appro_page.judge_new_approval_process('审批中')
        self.assertTrue(self.result, '部门领导业务审批状态错误')

        self.appro_page.log.info('--[ 部门领导同意-断言]')
        self.result = self.appro_page.approval_new_agree()
        self.assertTrue(self.result, '下一个环节审批领导断言失败')

        self.appro_page.log.info('--[ 部门领导业务审批确定-断言]')
        self.result = self.appro_page.new_bill_confirm_approval()
        self.assertTrue(self.result, '部门领导业务审批失败')

        self.appro_page.log.info('--[ 会计登录]')
        self.result = self.appro_page.login_accounting()
        self.assertTrue(self.result, '会计登录失败')

        self.appro_page.log.info('--[ 会计查找单据-断言]')
        self.result = self.appro_page.enter_list_find_finance_reimbursement()
        self.assertTrue(self.result, '会计查找单据失败')

        self.appro_page.log.info('--[ 会计审批状态-断言]')
        self.result = self.appro_page.judge_new_approval_process('财务初审中')
        self.assertTrue(self.result, '会计审批状态错误')

        self.appro_page.log.info('--[ 会计同意-断言]')
        self.result = self.appro_page.approval_new_agree()
        self.assertTrue(self.result, '下一个环节审批领导断言失败')

        self.appro_page.log.info('--[ 会计审核确定-断言]')
        self.result = self.appro_page.new_bill_confirm_approval()
        self.assertTrue(self.result, '会计审核失败')

        self.appro_page.log.info('--[ 财务经理登录]')
        self.result = self.appro_page.login_financial_manager()
        self.assertTrue(self.result, '财务经理登录失败')

        self.appro_page.log.info('--[ 财务经理查找单据—断言]')
        self.result = self.appro_page.enter_list_find_review_reimbursement()
        self.assertTrue(self.result, '财务经理查找单据失败')

        self.appro_page.log.info('--[ 财务经理审批状态-断言]')
        self.result = self.appro_page.judge_new_approval_process('财务复核中')
        self.assertTrue(self.result, '财务经理审批状态断言失败')

        self.appro_page.log.info('--[ 财务经理同意断言]')
        self.result = self.appro_page.approval_new_agree()
        self.assertTrue(self.result, '财务经理同意失败')

        self.appro_page.log.info('--[ 财务经理审批确定-断言]')
        self.result = self.appro_page.new_bill_confirm_approval()
        self.assertTrue(self.result, '财务经理审批确定失败')

        self.appro_page.log.info('--[ 出纳登录]')
        self.appro_page.login_cashier()

        self.appro_page.log.info('--[ 出纳查找单据-断言]')
        self.result =  self.appro_page.enter_list_find_payment(bill_type='new')
        self.assertTrue(self.result,'出纳查找单据断言失败')

        self.appro_page.log.info('--[ 出纳状态-断言]')
        self.result = self.appro_page.judge_new_approval_process('出纳付款中')
        self.assertTrue(self.result, '出纳状态断言失败')

        self.appro_page.log.info('--[ 出纳支付-断言]')
        self.result = self.appro_page.new_payment()
        self.assertTrue(self.result, '出纳支付断言失败')

    def test_cost_bill_process2(self):
        u"""费用报销单-会签（项目）-业务-财务-加审领导-财务-复核-出纳"""
        self.appro_page.log.info('--[ 进入费用报销单-填写费用报销单-断言]')
        self.result = self.appro_page.enter_fill_cost_bill(project='ykb-测试项目')
        self.assertTrue(self.result, '进入费用报销单-填写费用报销单-断言失败')

        self.appro_page.log.info('--[ 项目经理登录]')
        self.result = self.appro_page.login_project_manager()
        self.assertTrue(self.result, '项目经理登录失败')

        self.appro_page.log.info('--[ 项目经理查找单据-断言]')
        self.result = self.appro_page.enter_list_find_new_bill()
        self.assertTrue(self.result, '项目经理查找单据失败')

        self.appro_page.log.info('--[ 项目经理会签状态-断言]')
        self.result = self.appro_page.judge_new_approval_process('审批中')
        self.assertTrue(self.result, '项目经理会签状态错误')

        self.appro_page.log.info('--[ 项目经理同意-断言]')
        self.result = self.appro_page.approval_new_agree('部门领导')
        self.assertTrue(self.result, '下一个环节审批领导断言失败')

        self.appro_page.log.info('--[ 项目经理会签确定-断言]')
        self.result = self.appro_page.new_bill_confirm_approval()
        self.assertTrue(self.result, '项目经理会签审批失败')

        self.appro_page.log.info('--[ 部门领导登录]')
        self.result = self.appro_page.login_department_leader()
        self.assertTrue(self.result, '部门领导登录失败')

        self.appro_page.log.info('--[ 部门领导查找单据-断言]')
        self.result = self.appro_page.enter_list_find_new_bill()
        self.assertTrue(self.result, '部门领导查找单据失败')

        self.appro_page.log.info('--[ 部门领导业务审批状态-断言]')
        self.result = self.appro_page.judge_new_approval_process('审批中')
        self.assertTrue(self.result, '部门领导业务审批状态错误')

        self.appro_page.log.info('--[ 部门领导同意-断言]')
        self.result = self.appro_page.approval_new_agree()
        self.assertTrue(self.result, '下一个环节审批领导断言失败')

        self.appro_page.log.info('--[ 部门领导业务审批确定-断言]')
        self.result = self.appro_page.new_bill_confirm_approval()
        self.assertTrue(self.result, '部门领导业务审批失败')

        self.appro_page.log.info('--[ 会计登录]')
        self.result = self.appro_page.login_accounting()
        self.assertTrue(self.result, '会计登录失败')

        self.appro_page.log.info('--[ 会计查找单据-断言]')
        self.result = self.appro_page.enter_list_find_finance_reimbursement()
        self.assertTrue(self.result, '会计查找单据失败')

        self.appro_page.log.info('--[ 会计审批状态-断言]')
        self.result = self.appro_page.judge_new_approval_process('财务初审中')
        self.assertTrue(self.result, '会计审批状态错误')

        self.appro_page.log.info('--[ 会计加审-断言]')
        self.result = self.appro_page.add_approval_finance_confirm()
        self.assertTrue(self.result, '会计加审失败')

        self.appro_page.log.info('--[ 加审领导登录]')
        self.appro_page.login_add_approval()

        self.appro_page.log.info('--[ 加审领导查找单据-断言]')
        self.result = self.appro_page.enter_list_find_new_bill()
        self.assertTrue(self.result, '加审领导查找单据失败')

        self.appro_page.log.info('--[ 加审领导业务审批状态-断言]')
        self.result = self.appro_page.judge_new_approval_process('财务加审中')
        self.assertTrue(self.result, '加审领导业务审批状态错误')

        self.appro_page.log.info('--[ 加审领导同意断言]')
        self.result = self.appro_page.new_payment()
        self.assertTrue(self.result, '加审领导同意断言失败')

        self.appro_page.log.info('--[ 会计登录]')
        self.result = self.appro_page.login_accounting()
        self.assertTrue(self.result, '会计登录失败')

        self.appro_page.log.info('--[ 会计查找单据-断言]')
        self.result = self.appro_page.enter_list_find_finance_reimbursement()
        self.assertTrue(self.result, '会计查找单据失败')

        self.appro_page.log.info('--[ 会计审批状态-断言]')
        self.result = self.appro_page.judge_new_approval_process('财务初审中')
        self.assertTrue(self.result, '会计审批状态错误')

        self.appro_page.log.info('--[ 会计同意-断言]')
        self.result = self.appro_page.approval_new_agree()
        self.assertTrue(self.result, '下一个环节审批领导断言失败')

        self.appro_page.log.info('--[ 会计审核确定-断言]')
        self.result = self.appro_page.new_bill_confirm_approval()
        self.assertTrue(self.result, '会计审核失败')

        self.appro_page.log.info('--[ 财务经理登录]')
        self.result = self.appro_page.login_financial_manager()
        self.assertTrue(self.result, '财务经理登录失败')

        self.appro_page.log.info('--[ 财务经理查找单据—断言]')
        self.result = self.appro_page.enter_list_find_review_reimbursement()
        self.assertTrue(self.result, '财务经理查找单据失败')

        self.appro_page.log.info('--[ 财务经理审批状态-断言]')
        self.result = self.appro_page.judge_new_approval_process('财务复核中')
        self.assertTrue(self.result, '财务经理审批状态断言失败')

        self.appro_page.log.info('--[ 财务经理同意断言]')
        self.result = self.appro_page.approval_new_agree()
        self.assertTrue(self.result, '财务经理同意失败')

        self.appro_page.log.info('--[ 财务经理审批确定-断言]')
        self.result = self.appro_page.new_bill_confirm_approval()
        self.assertTrue(self.result, '财务经理审批确定失败')

        self.appro_page.log.info('--[ 出纳登录]')
        self.appro_page.login_cashier()

        self.appro_page.log.info('--[ 出纳查找单据-断言]')
        self.result = self.appro_page.enter_list_find_payment(bill_type='new')
        self.assertTrue(self.result, '出纳查找单据断言失败')

        self.appro_page.log.info('--[ 出纳状态-断言]')
        self.result = self.appro_page.judge_new_approval_process('出纳付款中')
        self.assertTrue(self.result, '出纳状态断言失败')

        self.appro_page.log.info('--[ 出纳支付-断言]')
        self.result = self.appro_page.new_payment()
        self.assertTrue(self.result, '出纳支付断言失败')

    def test_cost_bill_process3(self):
        u"""费用报销单-业务-财务-加审领导-财务-复核加审-财务总监-出纳"""
        self.appro_page.log.info('--[ 进入费用报销单-填写费用报销单-断言]')
        self.result = self.appro_page.enter_fill_cost_bill()
        self.assertTrue(self.result, '进入费用报销单-填写费用报销单-断言失败')

        self.appro_page.log.info('--[ 部门领导登录]')
        self.result = self.appro_page.login_department_leader()
        self.assertTrue(self.result, '部门领导登录失败')

        self.appro_page.log.info('--[ 部门领导查找单据-断言]')
        self.result = self.appro_page.enter_list_find_new_bill()
        self.assertTrue(self.result, '部门领导查找单据失败')

        self.appro_page.log.info('--[ 部门领导业务审批状态-断言]')
        self.result = self.appro_page.judge_new_approval_process('审批中')
        self.assertTrue(self.result, '部门领导业务审批状态错误')

        self.appro_page.log.info('--[ 部门领导同意-断言]')
        self.result = self.appro_page.approval_new_agree()
        self.assertTrue(self.result, '下一个环节审批领导断言失败')

        self.appro_page.log.info('--[ 部门领导业务审批确定-断言]')
        self.result = self.appro_page.new_bill_confirm_approval()
        self.assertTrue(self.result, '部门领导业务审批失败')

        self.appro_page.log.info('--[ 会计登录]')
        self.result = self.appro_page.login_accounting()
        self.assertTrue(self.result, '会计登录失败')

        self.appro_page.log.info('--[ 会计查找单据-断言]')
        self.result = self.appro_page.enter_list_find_finance_reimbursement()
        self.assertTrue(self.result, '会计查找单据失败')

        self.appro_page.log.info('--[ 会计审批状态-断言]')
        self.result = self.appro_page.judge_new_approval_process('财务初审中')
        self.assertTrue(self.result, '会计审批状态错误')

        self.appro_page.log.info('--[ 会计同意-断言]')
        self.result = self.appro_page.approval_new_agree()
        self.assertTrue(self.result, '下一个环节审批领导断言失败')

        self.appro_page.log.info('--[ 会计审核确定-断言]')
        self.result = self.appro_page.new_bill_confirm_approval()
        self.assertTrue(self.result, '会计审核失败')

        self.appro_page.log.info('--[ 财务经理登录]')
        self.result = self.appro_page.login_financial_manager()
        self.assertTrue(self.result, '财务经理登录失败')

        self.appro_page.log.info('--[ 财务经理查找单据—断言]')
        self.result = self.appro_page.enter_list_find_review_reimbursement()
        self.assertTrue(self.result, '财务经理查找单据失败')

        self.appro_page.log.info('--[ 财务经理审批状态-断言]')
        self.result = self.appro_page.judge_new_approval_process('财务复核中')
        self.assertTrue(self.result, '财务经理审批状态断言失败')

        self.appro_page.log.info('--[ 财务经理同意断言]')
        self.result = self.appro_page.approval_new_agree()
        self.assertTrue(self.result, '财务经理同意失败')

        self.appro_page.log.info('--[ 财务经理添加审批人审批确定-断言]')
        self.result = self.appro_page.add_approval_person_review_confirm()
        self.assertTrue(self.result, '财务经理添加审批人审批确定失败')

        self.appro_page.log.info('--[ 财务总监登录]')
        self.appro_page.login_financial_chief_inspector()

        self.appro_page.log.info('--[ 财务总监查找单据-断言]')
        self.result = self.appro_page.enter_list_find_review_reimbursement()
        self.assertTrue(self.result, '财务总监查找单据断言失败')

        self.appro_page.log.info('--[ 财务总监审批状态-断言]')
        self.result = self.appro_page.judge_new_approval_process('财务总监审核中')
        self.assertTrue(self.result, '财务总监审批状态断言失败')

        self.appro_page.log.info('--[ 财务总监同意断言]')
        self.result = self.appro_page.approval_new_agree()
        self.assertTrue(self.result, '财务总监同意失败')

        self.appro_page.log.info('--[ 财务总监审批确定-断言]')
        self.result = self.appro_page.new_bill_confirm_approval()
        self.assertTrue(self.result, '财务总监审批确定失败')

        self.appro_page.log.info('--[ 出纳登录]')
        self.appro_page.login_cashier()

        self.appro_page.log.info('--[ 出纳查找单据-断言]')
        self.result = self.appro_page.enter_list_find_payment(bill_type='new')
        self.assertTrue(self.result, '出纳查找单据断言失败')

        self.appro_page.log.info('--[ 出纳状态-断言]')
        self.result = self.appro_page.judge_new_approval_process('出纳付款中')
        self.assertTrue(self.result, '出纳状态断言失败')

        self.appro_page.log.info('--[ 出纳支付-断言]')
        self.result = self.appro_page.new_payment()
        self.assertTrue(self.result, '出纳支付断言失败')

    def test_cost_bill_process4(self):
        u"""费用报销单-两个会签-业务-财务-复核出纳"""
        self.appro_page.log.info('--[ 进入费用报销单-填写费用报销单-断言]')
        self.result = self.appro_page.enter_fill_cost_bill(department='ykb-测试小组',project='ykb-测试项目')
        self.assertTrue(self.result, '进入费用报销单-填写费用报销单-断言失败')

        self.appro_page.log.info('--[ 项目经理登录]')
        self.result = self.appro_page.login_project_manager()
        self.assertTrue(self.result, '项目经理登录失败')

        self.appro_page.log.info('--[ 项目经理查找单据-断言]')
        self.result = self.appro_page.enter_list_find_new_bill()
        self.assertTrue(self.result, '项目经理查找单据失败')

        self.appro_page.log.info('--[ 项目经理会签状态-断言]')
        self.result = self.appro_page.judge_new_approval_process('会签中','new')
        self.assertTrue(self.result,'项目经理会签状态错误')

        self.appro_page.log.info('--[ 项目经理同意-断言]')
        self.result = self.appro_page.approval_new_agree('部门领导')
        self.assertTrue(self.result, '下一个环节审批领导断言失败')

        self.appro_page.log.info('--[ 项目经理会签确定-断言]')
        self.result = self.appro_page.new_bill_confirm_approval()
        self.assertTrue(self.result, '项目经理会签审批失败')

        self.appro_page.log.info('--[ 公司领导登录]')
        self.result = self.appro_page.login_company_leader()
        self.assertTrue(self.result, '公司领导登录失败')

        self.appro_page.log.info('--[ 公司领导查找单据-断言]')
        self.result = self.appro_page.enter_list_find_new_bill()
        self.assertTrue(self.result, '公司领导查找单据失败')

        self.appro_page.log.info('--[ 公司领导会签状态-断言]')
        self.result = self.appro_page.judge_new_approval_process('会签中','new')
        self.assertTrue(self.result, '公司领导会签状态错误')

        self.appro_page.log.info('--[ 公司领导同意-断言]')
        self.result = self.appro_page.approval_new_agree('部门领导')
        self.assertTrue(self.result, '下一个环节审批领导断言失败')

        self.appro_page.log.info('--[ 公司领导会签确定-断言]')
        self.result = self.appro_page.new_bill_confirm_approval()
        self.assertTrue(self.result, '公司领导会签审批失败')

        self.appro_page.log.info('--[ 部门领导登录]')
        self.result = self.appro_page.login_department_leader()
        self.assertTrue(self.result, '部门领导登录失败')

        self.appro_page.log.info('--[ 部门领导查找单据-断言]')
        self.result = self.appro_page.enter_list_find_new_bill()
        self.assertTrue(self.result, '部门领导查找单据失败')

        self.appro_page.log.info('--[ 部门领导业务审批状态-断言]')
        self.result = self.appro_page.judge_new_approval_process('审批中')
        self.assertTrue(self.result, '部门领导业务审批状态错误')

        self.appro_page.log.info('--[ 部门领导同意-断言]')
        self.result = self.appro_page.approval_new_agree()
        self.assertTrue(self.result, '下一个环节审批领导断言失败')

        self.appro_page.log.info('--[ 部门领导业务审批确定-断言]')
        self.result = self.appro_page.new_bill_confirm_approval()
        self.assertTrue(self.result, '部门领导业务审批失败')
        #

        self.appro_page.log.info('--[ 会计登录]')
        self.result = self.appro_page.login_accounting()
        self.assertTrue(self.result, '会计登录失败')

        self.appro_page.log.info('--[ 会计查找单据-断言]')
        self.result = self.appro_page.enter_list_find_finance_reimbursement()
        self.assertTrue(self.result, '会计查找单据失败')

        self.appro_page.log.info('--[ 会计审批状态-断言]')
        self.result = self.appro_page.judge_new_approval_process('财务初审中')
        self.assertTrue(self.result, '会计审批状态错误')

        self.appro_page.log.info('--[ 会计同意-断言]')
        self.result = self.appro_page.approval_new_agree()
        self.assertTrue(self.result, '下一个环节审批领导断言失败')

        self.appro_page.log.info('--[ 会计审核确定-断言]')
        self.result = self.appro_page.new_bill_confirm_approval()
        self.assertTrue(self.result, '会计审核失败')

        self.appro_page.log.info('--[ 财务经理登录]')
        self.result = self.appro_page.login_financial_manager()
        self.assertTrue(self.result, '财务经理登录失败')

        self.appro_page.log.info('--[ 财务经理查找单据—断言]')
        self.result = self.appro_page.enter_list_find_review_reimbursement()
        self.assertTrue(self.result, '财务经理查找单据失败')

        self.appro_page.log.info('--[ 财务经理审批状态-断言]')
        self.result = self.appro_page.judge_new_approval_process('财务复核中')
        self.assertTrue(self.result, '财务经理审批状态断言失败')

        self.appro_page.log.info('--[ 财务经理同意断言]')
        self.result = self.appro_page.approval_new_agree()
        self.assertTrue(self.result, '财务经理同意失败')

        self.appro_page.log.info('--[ 财务经理审批确定-断言]')
        self.result = self.appro_page.new_bill_confirm_approval()
        self.assertTrue(self.result, '财务经理审批确定失败')

        self.appro_page.log.info('--[ 出纳登录]')
        self.appro_page.login_cashier()

        self.appro_page.log.info('--[ 出纳查找单据-断言]')
        self.result = self.appro_page.enter_list_find_payment(bill_type='new')
        self.assertTrue(self.result, '出纳查找单据断言失败')

        self.appro_page.log.info('--[ 出纳状态-断言]')
        self.result = self.appro_page.judge_new_approval_process('出纳付款中')
        self.assertTrue(self.result, '出纳状态断言失败')

        self.appro_page.log.info('--[ 出纳支付-断言]')
        self.result = self.appro_page.new_payment()
        self.assertTrue(self.result, '出纳支付断言失败')

    def tearDown(self):
        self.appro_page.log.info('--[ 测试用例结束，截图]')

if __name__ == '__main__':
    unittest.main()

