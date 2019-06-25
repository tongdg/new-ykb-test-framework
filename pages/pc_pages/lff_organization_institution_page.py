#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-06-24 Created by lff'

from pages.pc_pages.index_page import IndexPage
import time

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
        return self.find_element_by_css_ykb('#treeDim > li > ul > li.leaf > div > span.text')
    @property
    def add_institution1(self):
        return self.find_element_by_css_ykb('#treeDim > li > ul > li.leaf > div > div > div:nth-child(2)')

    #进入组织机构
    def enter_organization_institution(self):
        self.click(self.setting)
        time.sleep(1)
        self.click(self.organization_institution)
        time.sleep(1)

