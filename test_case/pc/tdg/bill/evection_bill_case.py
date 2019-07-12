#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-06-10 Created by tongdg'

from pages.pc_pages.approval_page import ApprovalPage
import unittest
from selenium import webdriver
import os

class EvectionCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.appro_page = ApprovalPage(driver=self.driver, path=os.path.dirname(__file__))
        # 普通员工登录
        self.appro_page.log.info('--[普通员工登录]')
        self.appro_page.login_ordinary_staff()
        # 切换企业
        self.appro_page.switching_enterprises(_enterprise='tongdg艺赛旗', _login_name='普通员工')
        self.appro_page.log.info('--[切换企业ok,登录ok]')

    def test_evection_process1(self):
        u"""出差申请单-两个会签-业务（过滤）-直属领导"""
        self.appro_page.log.info('--[进入出差申请单-填写出差申请单-断言]')
        self.result = self.appro_page.enter_fill_evecation_bill('ykb-测试小组','ykb-测试项目')
        self.assertTrue(self.result, '进入出差申请单-填写出差申请单-断言失败')

        self.appro_page.log.info('--[项目经理登录]')
        self.appro_page.login_project_manager()

        self.appro_page.log.info('--[项目经理查找单据-断言]')
        self.result = self.appro_page.enter_list_find_old_bill()
        self.assertTrue(self.result,'项目经理查找单据失败')

        self.appro_page.log.info('--[项目经理会签状态-断言]')
        self.result = self.appro_page.judge_approval_process('会签中')
        self.assertTrue(self.result,'项目经理会签状态断言失败')

        self.appro_page.log.info('--[项目经理会签同意-断言]')
        self.result = self.appro_page.approval_old_agree(['部门领导'])
        self.assertTrue(self.result,'下一个环节审批领导断言失败')

        self.appro_page.log.info('--[项目经理会签确定-断言]')
        self.result = self.appro_page.old_apply_confirm()
        self.assertTrue(self.result,'项目经理会签审批失败')

        self.appro_page.log.info('--[公司领导登录]')
        self.appro_page.login_company_leader()

        self.appro_page.log.info('--[公司领导查找单据-断言]')
        self.result = self.appro_page.enter_list_find_old_bill()
        self.assertTrue(self.result, '公司领导查找单据断言失败')

        self.appro_page.log.info('--[公司领导审批状态-断言]')
        self.result = self.appro_page.judge_approval_process('会签中')
        self.assertTrue(self.result, '公司领导审批状态断言失败')

        self.appro_page.log.info('--[公司领导业务同意-断言]')
        self.result = self.appro_page.approval_old_agree(['部门领导'])
        self.assertTrue(self.result, '下一个环节审批领导断言失败')

        self.appro_page.log.info('--[公司领导业务确定-断言]')
        self.result = self.appro_page.old_apply_confirm()
        self.assertTrue(self.result, '公司领导业务审批失败')

        # 部门领导审批
        self.appro_page.log.info('--[部门领导登录]')
        self.appro_page.login_department_leader()

        self.appro_page.log.info('--[部门领导查找单据-断言]')
        self.result = self.appro_page.enter_list_find_old_bill()
        self.assertTrue(self.result, '部门领导查找单据断言失败')

        self.appro_page.log.info('--[部门领导审批状态-断言]')
        self.result = self.appro_page.judge_approval_process('审批中')
        self.assertTrue(self.result, '部门领导审批状态断言失败')

        self.appro_page.log.info('--[部门领导业务同意-断言]')
        self.result = self.appro_page.approval_old_agree(['公司领导'])
        self.assertTrue(self.result, '下一个环节审批领导断言失败')

        self.appro_page.log.info('--[部门领导业务确定-断言]')
        self.result = self.appro_page.old_apply_confirm()
        self.assertTrue(self.result, '部门领导业务审批失败')

        self.appro_page.log.info('--[公司领导登录]')
        self.appro_page.login_company_leader()

        self.appro_page.log.info('--[公司领导查找单据-断言]')
        self.result = self.appro_page.enter_list_find_old_bill()
        self.assertTrue(self.result, '公司领导查找单据断言失败')

        self.appro_page.log.info('--[公司领导审批状态-断言]')
        self.result = self.appro_page.judge_approval_process('审批中')
        self.assertTrue(self.result, '公司领导审批状态断言失败')

        self.appro_page.log.info('--[公司领导业务同意-断言]')
        self.result = self.appro_page.approval_old_agree([''])
        self.assertTrue(self.result, '下一个环节审批领导断言失败')

        self.appro_page.log.info('--[公司领导业务确定-断言]')
        self.result = self.appro_page.old_apply_confirm()
        self.assertTrue(self.result, '公司领导业务审批失败')

    def test_evection_process2(self):
        u"""出差申请单-业务-直属领导"""
        self.appro_page.log.info('--[进入出差申请单-填写出差申请单-断言]')
        self.result = self.appro_page.enter_fill_evecation_bill()
        self.assertTrue(self.result, '进入出差申请单-填写出差申请单-断言失败')

        self.appro_page.log.info('--[部门领导登录]')
        self.appro_page.login_department_leader()

        self.appro_page.log.info('--[部门领导查找单据-断言]')
        self.result = self.appro_page.enter_list_find_old_bill()
        self.assertTrue(self.result, '部门领导查找单据断言失败')

        self.appro_page.log.info('--[部门领导审批状态-断言]')
        self.result = self.appro_page.judge_approval_process('审批中')
        self.assertTrue(self.result, '部门领导审批状态断言失败')

        self.appro_page.log.info('--[部门领导业务同意-断言]')
        self.result = self.appro_page.approval_old_agree(['公司领导'])
        self.assertTrue(self.result, '下一个环节审批领导断言失败')

        self.appro_page.log.info('--[部门领导业务确定-断言]')
        self.result = self.appro_page.old_apply_confirm()
        self.assertTrue(self.result, '部门领导业务审批失败')

        self.appro_page.log.info('--[公司领导登录]')
        self.appro_page.login_company_leader()

        self.appro_page.log.info('--[公司领导查找单据-断言]')
        self.result = self.appro_page.enter_list_find_old_bill()
        self.assertTrue(self.result, '公司领导查找单据断言失败')

        self.appro_page.log.info('--[公司领导审批状态-断言]')
        self.result = self.appro_page.judge_approval_process('审批中')
        self.assertTrue(self.result, '公司领导审批状态断言失败')

        self.appro_page.log.info('--[公司领导业务同意-断言]')
        self.result = self.appro_page.approval_old_agree([''])
        self.assertTrue(self.result, '下一个环节审批领导断言失败')

        self.appro_page.log.info('--[公司领导业务确定-断言]')
        self.result = self.appro_page.old_apply_confirm()
        self.assertTrue(self.result, '公司领导业务审批失败')

    def test_evection_process3(self):
        u"""出差申请单-部门带出会签-业务（过滤）-直属领导"""
        self.appro_page.log.info('--[进入出差申请单-填写出差申请单-断言]')
        self.result = self.appro_page.enter_fill_evecation_bill(department='ykb-测试小组')
        self.assertTrue(self.result, '进入出差申请单-填写出差申请单-断言失败')

        # 会签带出来 1人会签转业务
        self.appro_page.log.info('--[公司领导登录]')
        self.appro_page.login_company_leader()

        self.appro_page.log.info('--[公司领导查找单据-断言]')
        self.result = self.appro_page.enter_list_find_old_bill()
        self.assertTrue(self.result, '公司领导查找单据断言失败')

        self.appro_page.log.info('--[公司领导审批状态-断言]')
        self.result = self.appro_page.judge_approval_process('审批中')
        self.assertTrue(self.result, '公司领导审批状态断言失败')

        self.appro_page.log.info('--[公司领导业务同意-断言]')
        self.result = self.appro_page.approval_old_agree(['部门领导'])
        self.assertTrue(self.result, '下一个环节审批领导断言失败')

        self.appro_page.log.info('--[公司领导业务确定-断言]')
        self.result = self.appro_page.old_apply_confirm()
        self.assertTrue(self.result, '公司领导业务审批失败')

        self.appro_page.log.info('--[部门领导登录]')
        self.appro_page.login_department_leader()

        self.appro_page.log.info('--[部门领导查找单据-断言]')
        self.result = self.appro_page.enter_list_find_old_bill()
        self.assertTrue(self.result, '部门领导查找单据断言失败')

        self.appro_page.log.info('--[部门领导审批状态-断言]')
        self.result = self.appro_page.judge_approval_process('审批中')
        self.assertTrue(self.result, '部门领导审批状态断言失败')

        self.appro_page.log.info('--[部门领导业务同意-断言]')
        self.result = self.appro_page.approval_old_agree(['公司领导'])
        self.assertTrue(self.result, '下一个环节审批领导断言失败')

        self.appro_page.log.info('--[部门领导业务确定-断言]')
        self.result = self.appro_page.old_apply_confirm()
        self.assertTrue(self.result, '部门领导业务审批失败')

        self.appro_page.log.info('--[公司领导登录]')
        self.appro_page.login_company_leader()

        self.appro_page.log.info('--[公司领导查找单据-断言]')
        self.result = self.appro_page.enter_list_find_old_bill()
        self.assertTrue(self.result, '公司领导查找单据断言失败')

        self.appro_page.log.info('--[公司领导审批状态-断言]')
        self.result = self.appro_page.judge_approval_process('审批中')
        self.assertTrue(self.result, '公司领导审批状态断言失败')

        self.appro_page.log.info('--[公司领导业务同意-断言]')
        self.result = self.appro_page.approval_old_agree([''])
        self.assertTrue(self.result, '下一个环节审批领导断言失败')

        self.appro_page.log.info('--[公司领导业务确定-断言]')
        self.result = self.appro_page.old_apply_confirm()
        self.assertTrue(self.result, '公司领导业务审批失败')

    def test_evection_process4(self):
        u"""出差申请单-项目带出会签-业务-直属领导"""
        self.appro_page.log.info('--[进入出差申请单-填写出差申请单-断言]')
        self.evecation_result = self.appro_page.enter_fill_evecation_bill(project='ykb-测试项目')
        self.assertTrue(self.evecation_result, '进入出差申请单-填写出差申请单-断言失败')

        # 会签带出来 1人会签转业务
        self.appro_page.log.info('--[项目经理登录]')
        self.appro_page.login_project_manager()

        self.appro_page.log.info('--[项目经理查找单据-断言]')
        self.result = self.appro_page.enter_list_find_old_bill()
        self.assertTrue(self.result, '项目经理查找单据失败')

        self.appro_page.log.info('--[项目经理会签状态-断言]')
        self.result = self.appro_page.judge_approval_process('审批中')
        self.assertTrue(self.result, '项目经理会签状态断言失败')

        self.appro_page.log.info('--[项目经理会签同意-断言]')
        self.result = self.appro_page.approval_old_agree(['部门领导'])
        self.assertTrue(self.result, '下一个环节审批领导断言失败')

        self.appro_page.log.info('--[项目经理会签确定-断言]')
        self.result = self.appro_page.old_apply_confirm()
        self.assertTrue(self.result, '项目经理会签审批失败')

        self.appro_page.log.info('--[部门领导登录]')
        self.appro_page.login_department_leader()

        self.appro_page.log.info('--[部门领导查找单据-断言]')
        self.result = self.appro_page.enter_list_find_old_bill()
        self.assertTrue(self.result, '部门领导查找单据断言失败')

        self.appro_page.log.info('--[部门领导审批状态-断言]')
        self.result = self.appro_page.judge_approval_process('审批中')
        self.assertTrue(self.result, '部门领导审批状态断言失败')

        self.appro_page.log.info('--[部门领导业务同意-断言]')
        self.result = self.appro_page.approval_old_agree(['公司领导'])
        self.assertTrue(self.result, '下一个环节审批领导断言失败')

        self.appro_page.log.info('--[部门领导业务确定-断言]')
        self.result = self.appro_page.old_apply_confirm()
        self.assertTrue(self.result, '部门领导业务审批失败')

        self.appro_page.log.info('--[公司领导登录]')
        self.appro_page.login_company_leader()

        self.appro_page.log.info('--[公司领导查找单据-断言]')
        self.result = self.appro_page.enter_list_find_old_bill()
        self.assertTrue(self.result, '公司领导查找单据断言失败')

        self.appro_page.log.info('--[公司领导审批状态-断言]')
        self.result = self.appro_page.judge_approval_process('审批中')
        self.assertTrue(self.result, '公司领导审批状态断言失败')

        self.appro_page.log.info('--[公司领导业务同意-断言]')
        self.result = self.appro_page.approval_old_agree([''])
        self.assertTrue(self.result, '下一个环节审批领导断言失败')

        self.appro_page.log.info('--[公司领导业务确定-断言]')
        self.result = self.appro_page.old_apply_confirm()
        self.assertTrue(self.result, '公司领导业务审批失败')

    def tearDown(self):
        # self.appro_page.driver.quit()
        self.appro_page.log.info('--[测试用例结束，截图]')

if __name__ == '__main__':
    unittest.main()