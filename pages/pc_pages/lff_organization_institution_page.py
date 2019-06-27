#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-06-24 Created by lff'

from pages.pc_pages.index_page import IndexPage
import time
import random

class OrganizationInstitution(IndexPage):
    '''
        组织机构设置页面
    '''

    #组织机构——设置
    @property
    def organization_institution(self):
        return self.find_element_by_class_name_ykb('zzjg_btn')
    #根目录
    @property
    def edit_btn(self):
        return self.find_element_by_class_name_ykb('text')
    #添加机构
    @property
    def add_institution(self):
        return self.find_element_by_class_name_ykb('actionitem')
    #机构名称
    @property
    def institution_name(self):
        return self.find_element_by_css_ykb('#depModal > div > div > div.confirmnew-modal-body.modal-body > div > div:nth-child(2) > input')
    #机构编码
    @property
    def institution_code(self):
        return self.find_element_by_css_ykb('#depModal > div > div > div.confirmnew-modal-body.modal-body > div > div:nth-child(3) > input')
    #机构负责人
    #下拉按钮
    @property
    def institution_person(self):
        return self.find_element_by_css_ykb('#s2id_autogen3 > a > span.select2-arrow > b')
    #搜索机构负责人
    @property
    def institution_person_text(self):
        return  self.find_element_by_class_name_ykb('select2-focused')
    #选机构负责人
    @property
    def institution_person_sel(self):
        return self.find_element_by_class_name_ykb('select2-match')
    #确定按钮
    @property
    def submit_btn(self):
        return self.find_element_by_css_ykb('#depModal > div > div > div.confirmnew-modal-footer > button.eui-btn.eui-btn-blue.btn-modal-confirm')
    #子目录
    @property
    def subdirectory_btn(self):
        return self.find_element_by_css_ykb('#treeDim > li > ul > li:nth-child(3) > div > span.text')
    # 添加机构
    @property
    def add_institution1(self):
        return self.find_element_by_css_ykb('#treeDim > li > ul > li:nth-child(3) > div > div > div:nth-child(2)')
    #随机数
    @property
    def random_num(self):
        return str(random.randint(1,10000))
    #添加人员
    @property
    def add_person(self):
        return self.find_element_by_css_ykb('#treeDim > li > ul > li:nth-child(3) > div > div > div:nth-child(3)')
    #姓名
    @property
    def add_name(self):
        return self.find_element_by_name_ykb('name')
    #性别
    @property
    def add_sex(self):
        return self.find_element_by_css_ykb('#userModal > div > div > div.confirmnew-modal-body.modal-body > div > div:nth-child(3) > span.text-wrap > label:nth-child(1)')
    #手机号
    @property
    def add_tel(self):
        return self.find_element_by_css_ykb('#userModal > div > div > div.confirmnew-modal-body.modal-body > div > div:nth-child(4) > input')
    #手机号随机数
    @property
    def random_telnum(self):
        return str(random.randint(100000000, 999999999))
    #员工编号
    @property
    def add_code(self):
        return self.find_element_by_css_ykb('#userModal > div > div > div.confirmnew-modal-body.modal-body > div > div:nth-child(5) > input')
    #直属领导
    #下拉框
    @property
    def direct_leader(self):
        return self.find_element_by_css_ykb('#userModal > div > div > div.confirmnew-modal-body.modal-body > div > div:nth-child(6) > input')
    #选直属领导
    @property
    def sel_direct_leader(self):
        return self.find_element_by_css_ykb('#e7ccplugincombobox_AZ > ul > li > div > ul > li:nth-child(1) > span > a')
    #职级
    @property
    def rank_text(self):
        return self.find_element_by_css_ykb('#userModal > div > div > div.confirmnew-modal-body.modal-body > div > div:nth-child(7) > input')
    #角色
    #下拉框
    @property
    def sel_role(self):
        return self.find_element_by_class_name_ykb('select2-search-field')
    #部门领导
    @property
    def department_head(self):
        return self.find_element_by_id_ykb('select2-result-label-195')
    #会计
    @property
    def sel_accounting(self):
        return self.find_element_by_id_ykb('select2-result-label-197')
    #出纳
    @property
    def sel_cashier(self):
        return self.find_element_by_id_ykb('select2-result-label-200')
    #岗位
    @property
    def post_text(self):
        return self.find_element_by_css_ykb('#userModal > div > div > div.confirmnew-modal-body.modal-body > div > div:nth-child(9) > input')
    #邮箱
    @property
    def email_text(self):
        return self.find_element_by_css_ykb('#userModal > div > div > div.confirmnew-modal-body.modal-body > div > div:nth-child(10) > input')
    #确认按钮
    @property
    def submit_btn1(self):
        return self.find_element_by_css_ykb('#userModal > div > div > div.confirmnew-modal-footer > button.eui-btn.eui-btn-blue.btn-modal-confirm')

    #进入组织机构
    def enter_organization_institution(self):
        self.click(self.setting)
        time.sleep(1)
        self.click(self.organization_institution)
        time.sleep(1)

