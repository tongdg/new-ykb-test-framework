#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-06-10 Created by tongdg'

from pages.pc_pages.approval_page import ApprovalPage
import unittest
from selenium import webdriver
import os

class ApprovalCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.appro_page = ApprovalPage(driver=self.driver, path=os.path.dirname(__file__))
        # 普通员工登录
        self.appro_page.log.info('--[普通员工登录]')
        self.appro_page.login_ordinary_staff()
        # 切换企业
        self.appro_page.switching_enterprises(_enterprise='tongdg艺赛旗', _login_name='普通员工')
        self.appro_page.log.info('--[切换企业ok,登录ok]')

    # def test_eve_2countersign_1business(self):
    #     u"""出差申请单-两个会签-业务"""
    #     self.appro_page.log.info('--[进入出差申请单-填写出差申请单-断言]')
    #     self.evecation_result = self.appro_page.enter_fill_evecation_bill('ykb-测试小组','ykb-测试项目')
    #     self.assertTrue(self.evecation_result, '进入出差申请单-填写出差申请单-断言失败')
    #
    #     self.appro_page.log.info('--[普通员工退出测试用例-断言]')
    #     self.sign_out_result = self.appro_page.singn_out()
    #     self.assertTrue(self.sign_out_result, '退出成功断言失败!')
    #
    #     self.appro_page.log.info('--[项目经理登录]')
    #     self.appro_page.login_project_manager()
    #
    #     self.appro_page.log.info('--[项目经理查找单据-断言]')
    #     self.find_eve_result = self.appro_page.enter_list_find_evecation_bill()
    #     self.assertTrue(self.find_eve_result,'项目经理查找单据失败')
    #
    #     self.appro_page.log.info('--[项目经理会签状态-断言]')
    #     self.eve_pro_result = self.appro_page.judge_approval_process('会签中')
    #     self.assertTrue(self.evecation_result,'项目经理会签状态断言失败')
    #
    #     self.appro_page.log.info('--[项目经理会签同意-断言]')
    #     self.eve_agree_result = self.appro_page.evection_approval_agree(['部门领导'])
    #     self.assertTrue(self.eve_agree_result,'下一个环节审批领导断言失败')
    #
    #     self.appro_page.log.info('--[项目经理会签确定-断言]')
    #     self.eve_confirm_result = self.appro_page.evection_apply_confirm()
    #     self.assertTrue(self.eve_confirm_result,'项目经理会签审批失败')
    #
    #     self.appro_page.log.info('--[项目经理退出测试用例-断言]')
    #     self.sign_out_result = self.appro_page.singn_out()
    #     self.assertTrue(self.sign_out_result, '项目经理退出成功断言失败!')
    #
    #     # self.appro_page.log.info('--[部门领导登录]')
    #     # self.appro_page.login_project_manager()
    #     #
    #     # self.appro_page.log.info('--[部门领导查找单据-断言]')
    #     # self.eve_pro_result = self.appro_page.enter_list_find_evecation_bill()
    #     # self.assertTrue(self.eve_pro_result, '部门领导查找单据断言失败')
    #
    #     self.appro_page.log.info('--[部门领导登录]')
    #     self.appro_page.login_department_leader()
    #
    #     self.appro_page.log.info('--[部门领导查找单据-断言]')
    #     self.eve_pro_result = self.appro_page.enter_list_find_evecation_bill()
    #     self.assertTrue(self.evecation_result, '部门领导查找单据断言失败')
    #
    #     self.appro_page.log.info('--[部门领导审批状态-断言]')
    #     self.eve_pro_result = self.appro_page.judge_approval_process('审批中')
    #     self.assertTrue(self.evecation_result, '部门领导审批状态断言失败')
    #
    #     self.appro_page.log.info('--[部门领导业务同意-断言]')
    #     self.eve_agree_result = self.appro_page.evection_approval_agree([''])
    #     self.assertTrue(self.eve_agree_result, '下一个环节审批领导断言失败')
    #
    #     self.appro_page.log.info('--[部门领导业务确定-断言]')
    #     self.eve_confirm_result = self.appro_page.evection_apply_confirm()
    #     self.assertTrue(self.eve_confirm_result, '部门领导业务审批失败')
    #
    # def test_eve_1business(self):
    #     u"""出差申请单-业务"""
    #     self.appro_page.log.info('--[进入出差申请单-填写出差申请单-断言]')
    #     self.evecation_result = self.appro_page.enter_fill_evecation_bill()
    #     self.assertTrue(self.evecation_result, '进入出差申请单-填写出差申请单-断言失败')
    #
    #     self.appro_page.log.info('--[部门领导登录]')
    #     self.appro_page.login_department_leader()
    #
    #     self.appro_page.log.info('--[部门领导查找单据-断言]')
    #     self.eve_pro_result = self.appro_page.enter_list_find_evecation_bill()
    #     self.assertTrue(self.eve_pro_result, '部门领导查找单据断言失败')
    #
    #     self.appro_page.log.info('--[部门领导审批状态-断言]')
    #     self.eve_pro_result = self.appro_page.judge_approval_process('审批中')
    #     self.assertTrue(self.evecation_result, '部门领导审批状态断言失败')
    #
    #     self.appro_page.log.info('--[部门领导业务同意-断言]')
    #     self.eve_agree_result = self.appro_page.evection_approval_agree([''])
    #     self.assertTrue(self.eve_agree_result, '下一个环节审批领导断言失败')
    #
    #     self.appro_page.log.info('--[部门领导业务确定-断言]')
    #     self.eve_confirm_result = self.appro_page.evection_apply_confirm()
    #     self.assertTrue(self.eve_confirm_result, '部门领导业务审批失败')
    #
    # def test_eve_1department_countersign_1business(self):
    #     u"""出差申请单-部门带出会签-业务"""
    #     self.appro_page.log.info('--[进入出差申请单-填写出差申请单-断言]')
    #     self.evecation_result = self.appro_page.enter_fill_evecation_bill(department='ykb-测试小组')
    #     self.assertTrue(self.evecation_result, '进入出差申请单-填写出差申请单-断言失败')
    #
    #     # 会签带出来 1人会签转业务
    #     self.appro_page.log.info('--[公司领导登录]')
    #     self.appro_page.login_company_leader()
    #
    #     self.appro_page.log.info('--[公司领导查找单据-断言]')
    #     self.eve_pro_result = self.appro_page.enter_list_find_evecation_bill()
    #     self.assertTrue(self.evecation_result, '公司领导查找单据断言失败')
    #
    #     self.appro_page.log.info('--[公司领导审批状态-断言]')
    #     self.eve_pro_result = self.appro_page.judge_approval_process('审批中')
    #     self.assertTrue(self.evecation_result, '公司领导审批状态断言失败')
    #
    #     self.appro_page.log.info('--[公司领导业务同意-断言]')
    #     self.eve_agree_result = self.appro_page.evection_approval_agree(['部门领导'])
    #     self.assertTrue(self.eve_agree_result, '下一个环节审批领导断言失败')
    #
    #     self.appro_page.log.info('--[公司领导业务确定-断言]')
    #     self.eve_confirm_result = self.appro_page.evection_apply_confirm()
    #     self.assertTrue(self.eve_confirm_result, '公司领导业务审批失败')
    #
    #     self.appro_page.log.info('--[部门领导登录]')
    #     self.appro_page.login_department_leader()
    #
    #     self.appro_page.log.info('--[部门领导查找单据-断言]')
    #     self.eve_pro_result = self.appro_page.enter_list_find_evecation_bill()
    #     self.assertTrue(self.eve_pro_result, '部门领导查找单据断言失败')
    #
    #     self.appro_page.log.info('--[部门领导审批状态-断言]')
    #     self.eve_pro_result = self.appro_page.judge_approval_process('审批中')
    #     self.assertTrue(self.evecation_result, '部门领导审批状态断言失败')
    #
    #     self.appro_page.log.info('--[部门领导业务同意-断言]')
    #     self.eve_agree_result = self.appro_page.evection_approval_agree([''])
    #     self.assertTrue(self.eve_agree_result, '下一个环节审批领导断言失败')
    #
    #     self.appro_page.log.info('--[部门领导业务确定-断言]')
    #     self.eve_confirm_result = self.appro_page.evection_apply_confirm()
    #     self.assertTrue(self.eve_confirm_result, '部门领导业务审批失败')

    def test_eve_1project_countersign_1business(self):
        u"""出差申请单-项目带出会签-业务"""
        self.appro_page.log.info('--[进入出差申请单-填写出差申请单-断言]')
        self.evecation_result = self.appro_page.enter_fill_evecation_bill(project='ykb-测试项目')
        self.assertTrue(self.evecation_result, '进入出差申请单-填写出差申请单-断言失败')

        # 会签带出来 1人会签转业务
        self.appro_page.log.info('--[项目经理登录]')
        self.appro_page.login_project_manager()

        self.appro_page.log.info('--[项目经理查找单据-断言]')
        self.find_eve_result = self.appro_page.enter_list_find_evecation_bill()
        self.assertTrue(self.find_eve_result, '项目经理查找单据失败')

        self.appro_page.log.info('--[项目经理会签状态-断言]')
        self.eve_pro_result = self.appro_page.judge_approval_process('会签中')
        self.assertTrue(self.evecation_result, '项目经理会签状态断言失败')

        self.appro_page.log.info('--[项目经理会签同意-断言]')
        self.eve_agree_result = self.appro_page.evection_approval_agree(['部门领导'])
        self.assertTrue(self.eve_agree_result, '下一个环节审批领导断言失败')

        self.appro_page.log.info('--[项目经理会签确定-断言]')
        self.eve_confirm_result = self.appro_page.evection_apply_confirm()
        self.assertTrue(self.eve_confirm_result, '项目经理会签审批失败')

        self.appro_page.log.info('--[部门领导登录]')
        self.appro_page.login_department_leader()

        self.appro_page.log.info('--[部门领导查找单据-断言]')
        self.eve_pro_result = self.appro_page.enter_list_find_evecation_bill()
        self.assertTrue(self.eve_pro_result, '部门领导查找单据断言失败')

        self.appro_page.log.info('--[部门领导审批状态-断言]')
        self.eve_pro_result = self.appro_page.judge_approval_process('审批中')
        self.assertTrue(self.evecation_result, '部门领导审批状态断言失败')

        self.appro_page.log.info('--[部门领导业务同意-断言]')
        self.eve_agree_result = self.appro_page.evection_approval_agree([''])
        self.assertTrue(self.eve_agree_result, '下一个环节审批领导断言失败')

        self.appro_page.log.info('--[部门领导业务确定-断言]')
        self.eve_confirm_result = self.appro_page.evection_apply_confirm()
        self.assertTrue(self.eve_confirm_result, '部门领导业务审批失败')








    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()