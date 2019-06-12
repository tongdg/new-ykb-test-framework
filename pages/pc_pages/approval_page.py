#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-06-10 Created by tongdg'

from pages.pc_pages.bill_page import BillPage
import time

class ApprovalPage(BillPage):

    """
        头部：等待审批 审批记录 关键字 搜索按钮
        中部： 勾选 最后更新 提单日期 人员 类别 摘要 金额（元） 应付金额（元） 处理状态
        单据部分：

    """
    # 头部导航条
    # 等待审批
    @property
    def list_approval_wait(self):
        return self.find_element_by_link_text_ykb('等待审批')
    # 审批记录
    @property
    def list_approval_recored(self):
        return self.find_element_by_link_text_ykb('审批记录')
    # 输入关键字
    @property
    def list_approval_input_keyword(self):
        return self.find_element_by_css_ykb("input[class='condition']")
    # 搜索按钮
    @property
    def list_approval_keyword_search(self):
        return self.find_element_by_css_ykb("span[class='btnSearch']")
    # 中部导航条
    # 找出所有的td的集合
    @property
    def list_middle_navigation_bar(self):
        return self.find_element_by_hierarchy(
            lambda var : self.driver.find_element_by_id('MyDraft_Header').find_elements_by_tag_name('td')
        )
    # 单据列表
    # 找出所有的tr的集合
    @property
    def list_approval_bill(self):
        return self.find_element_by_hierarchy(
            lambda var: self.driver.find_element_by_id('myBusinessApprvalTask').find_elements_by_tag_name('tr')
        )
    """
        新老单据通用
    """
    # 审批记录按钮
    @property
    def approval_record_button(self):
        return self.find_element_by_css_ykb("button[class='eui-btn eui-btn-grey2 btn-approvedtrace']")
    # 会签展开按钮
    @property
    def open_countersign(self):
        return self.find_element_by_css_ykb("span[class='workflow-hq-icon handTabHq workflow-hq-iconed']")
    # 审批状态
    @property
    def approval_status(self):
        return self.find_element_by_hierarchy(
            lambda var : self.driver.find_element_by_css_selector("span[class='workflow-status']").find_element_by_tag_name('b')
        )
    # 审批记录关闭按钮
    @property
    def apporval_record_close_button(self):
        return self.find_element_by_css_ykb("button[class='btn btn-default']")
    """
        老单据 同意 退回 返回 
    """
    # 同意按钮
    @property
    def old_approval_agree(self):
        return self.find_element_by_css_ykb("button[class='eui-btn eui-btn-blue btn-agree']")
    # 退回按钮
    @property
    def old_approval_reject(self):
        return self.find_element_by_css_ykb("button[class='eui-btn eui-btn-red btn-reject']")
    # 确定按钮
    @property
    def old_approval_confirm(self):
        return self.find_element_by_css_ykb("button[class='eui-btn eui-btn-blue btn-approval-confirm']")
    # 返回按钮
    @property
    def old_approval_back(self):
        return self.find_element_by_css_ykb("button[class='eui-btn eui-btn-grey btn-back']")
    """
        通用方法
    """
    # 等待错误弹窗消失
    def wait_element_disappear_messager_error(self):
        return self.wait_element_disappear_true("div[class='messager error']",0.05)
    # 等待正确弹窗消失
    def wait_element_disappear_messager_success(self):
        return self.wait_element_disappear_true("div[class='messager success']",0.05)
    # 等待老单据审批处理中
    def wait_element_disappear_old_in_handle(self):
        return self.wait_element_disappear_true("button[class='eui-btn eui-btn-blue btn-approval-confirm disabled']")
    # 进入我的审批列表
    def __enter_approval_list(self):
        time.sleep(1)
        # 点击我的审批列表
        self.click(self.my_approva_link)
        time.sleep(1)
    # 找到单据，进到单据页面
    def __find_evecation_bill(self):
        time.sleep(1)
        # 点击等待审批列表，确定当前列表正确
        self.click(self.list_approval_wait)
        # 等待数据加载
        self.wait_element_disappear_data_load()
        # 输入单据号
        self.send_keys(self.list_approval_input_keyword,self.bill_number)
        time.sleep(1)
        # 搜索
        self.click(self.list_approval_keyword_search)
        time.sleep(2)
        # 判断提单的单据号是否与当前单据号一致
        if self.old_bill_number is not False:
            if self.bill_number == self.old_bill_number.text:
                self.log.debug('--[ 单据查找正确]')
                return True
            else:
                self.log.debug('--[ 单据查找错误]')
                return False
        else:
            self.log.debug('--[ 单据查找不到]')
            return False
    # 进入审批列表，找到提交的单据
    def enter_list_find_evecation_bill(self):
        self.__enter_approval_list()
        return self.__find_evecation_bill()
    # 判断当前流程是否正确
    def judge_approval_process(self,process):
        time.sleep(1)
        self.click(self.approval_record_button)
        time.sleep(1)
        if '会签中' in self.approval_status.text:
            self.click(self.open_countersign)
            time.sleep(1)
        if process in self.approval_status.text:
            self.log.debug('--[审批状态正确]')
            self.click(self.apporval_record_close_button)
            return True
        else:
            self.log.debug('--[审批状态错误]')
            return False
    # 审批单子
    def evection_approval_agree(self,appro_person):
        time.sleep(1)
        self.click(self.old_approval_agree)
        time.sleep(1)
        # 判断下一个审批人是否正确，断言
        opis = []
        if self.old_approval_input is not False:
            for opi in self.old_approval_input:
                opis.append(opi.get_attribute('textContent'))
            if set(appro_person) <= set(opis):
                self.log.debug('--[ 下一个环节审批领导带出正确]')
                return True
            else:
                self.log.debug('--[ 下一个环节审批领导带出错误]')
                return False
        else:
            self.log.debug('--[ 下一个环节没有审批领导]')
            return True
    # 确定审批过去
    def evection_apply_confirm(self):
        time.sleep(1)
        self.click(self.old_approval_confirm)
        messager_success = self.judge_js_pop_exist_visible("div[class='messager success']")
        self.wait_element_disappear_messager_success()
        if messager_success is True:
            self.log.debug('--[ 单据审批成功]')
            return True
        else:
            self.log.debug('--[ 单据审批失败]')
            return False





































