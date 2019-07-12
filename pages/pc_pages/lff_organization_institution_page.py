#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-06-24 Created by lff'

from pages.pc_pages.index_page import IndexPage
import time
import random
from selenium.webdriver.common.action_chains import ActionChains

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
    #姓名
    @property
    def add_name(self):
        return self.find_element_by_name_ykb('name')
    #性别——男
    @property
    def add_sex(self):
        return self.find_element_by_css_ykb('#userModal > div > div > div.confirmnew-modal-body.modal-body > div > div:nth-child(3) > span.text-wrap > label:nth-child(1)')
    #性别——女
    @property
    def add_sex1(self):
        return self.find_element_by_css_ykb('#userModal > div > div > div.confirmnew-modal-body.modal-body > div > div:nth-child(3) > span.text-wrap > label:nth-child(2)')
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
        return self.find_element_by_css_ykb('#e7ccplugincombobox_AZ > ul > li > div > ul > li > span > a')
    #职级
    @property
    def rank_text(self):
        return self.find_element_by_css_ykb('#userModal > div > div > div.confirmnew-modal-body.modal-body > div > div:nth-child(7) > input')

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
    # 角色
    # 下拉框
    @property
    def sel_role(self):
        return self.find_element_by_class_name_ykb('select2-search-field')
    # 角色列表
    @property
    def role_list(self):
        return self.find_element_by_hierarchy(lambda var : self.driver.find_element_by_css_selector('#select2-drop > ul').find_elements_by_tag_name('li'))
    # 收起下拉框
    @property
    def pop(self):
        return self.find_element_by_id_ykb('select2-drop-mask')
    # 用户名称
    @property
    def add_user_name(self):
        return self.find_element_by_class_name_ykb('user-name')
    #上级部门
    @property
    def superior_department(self):
        return self.find_element_by_css_ykb('#cpModal > div > div > div.confirmnew-modal-body.modal-body > div > div:nth-child(2) > input')
    #上级部门——管理团队
    @property
    def superior_department1(self):
        return self.find_element_by_css_ykb('#e7ccplugincombobox_AZ > ul > li > div > ul > li:nth-child(2) > span > a')
    #确定按钮
    @property
    def submit_btn2(self):
        return self.find_element_by_css_ykb('#cpModal > div > div > div.confirmnew-modal-footer > button.eui-btn.eui-btn-blue.btn-modal-confirm')
    #删除——确定
    @property
    def submit_btn3(self):
        return self.find_element_by_css_ykb('#delModal > div > div > div.confirmnew-modal-footer > button.eui-btn.eui-btn-blue.btn-modal-confirm')
    #导入
    @property
    def import_btn(self):
        return self.find_element_by_id_ykb('ImportBtn')
     #进入组织机构
    def enter_organization_institution(self):
        self.click(self.setting)
        time.sleep(1)
        self.click(self.organization_institution)
        time.sleep(1)

    # 根目录添加组织机构
    def add_institution_method(self):
        # 根目录
        self.click(self.edit_btn)
        time.sleep(1)
        # 添加机构
        self.click(self.add_institution)
        time.sleep(1)
        # 记住需要添加机构的名字
        self._institution_name = '自动化测试小组'+self.random_num
        print(self._institution_name + 'aaa')
        #机构名称
        self.send_keys(self.institution_name, self._institution_name)
        time.sleep(1)
        # 机构编码
        self.send_keys(self.institution_code, self.random_num)
        time.sleep(1)
        # 机构负责人
        # 下拉按钮
        self.click(self.institution_person)
        time.sleep(1)
        # 搜索机构负责人
        self.send_keys(self.institution_person_text, '童定国')
        time.sleep(1)
        # 选机构负责人
        self.click(self.institution_person_sel)
        time.sleep(1)
        # 确定按钮
        self.click(self.submit_btn)
        time.sleep(1)

    #子目录添加组织机构
    def add_institutions_method(self):
        # 记住需要添加机构的名字
        self._institutions_name = '自动化测试小小组' + self.random_num
        print(self._institution_name + 'bbb')
        # 机构名称
        self.send_keys(self.institution_name, self._institutions_name)
        time.sleep(1)
        # 机构编码
        self.send_keys(self.institution_code, self.random_num)
        time.sleep(1)
        # 机构负责人
        # 下拉按钮
        self.click(self.find_element_by_css_ykb('span[class="select2-arrow"]'))
        time.sleep(1)
        # 搜索机构负责人
        self.send_keys(self.institution_person_text, '童定国')
        time.sleep(1)
        # 选机构负责人
        self.click(self.institution_person_sel)
        time.sleep(1)
        # 确定按钮
        self.click(self.submit_btn)
        time.sleep(1)

    # 组织机构列表
    @property
    def institution_list(self):
        return self.find_element_by_hierarchy(
            lambda var: self.driver.find_element_by_id('treeDim').find_elements_by_tag_name('li')
        )
    # 查找根目录添加的机构点击添加机构
    def find_institution_add_what(self, add_what):
        ils = self.institution_list
        for il in ils:
            il_text = self.find_element_by_hierarchy(
                lambda var: il.find_element_by_css_selector("span[class='text']")
            )
            print(il_text.text)
            if il_text.text == self._institution_name:
                self.click(il)
                if add_what == '添加机构':
                    il_add_persons = self.find_element_by_hierarchy(
                        lambda var: il.find_elements_by_css_selector("div[class='actionitem']")
                    )
                    for iap in il_add_persons:
                        if iap.text == '添加机构':
                            self.click(iap)
                            print(iap.text)
                            break
                print(il_text.text)
                break

    # 查找组织机构
    def find_institutions_click(self):
        ils = self.institution_list
        for il in ils:
            il_text = self.find_element_by_hierarchy(
                lambda var: il.find_element_by_css_selector("span[class='text']")
            )
            if il_text.text == self._institution_name:
                self.click(il.find_element_by_css_selector("span[class='icon']"))


    # 查找子目录添加的机构点击添加人员
    def find_institutions_add_what(self, add_what):
        ils = self.institution_list
        for il in ils:
            il_text = self.find_element_by_hierarchy(
                lambda var: il.find_element_by_css_selector("span[class='text']")
            )
            print(il_text.text)
            if il_text.text == self._institution_name:
                self.click(il)
                if add_what == '添加人员':
                    il_add_persons = self.find_element_by_hierarchy(
                        lambda var: il.find_elements_by_css_selector("div[class='actionitem']")
                    )
                    for iap in il_add_persons:
                        if iap.text == '添加人员':
                            self.click(iap)
                            print(iap.text)
                            break
                print(il_text.text)
                break

    # 查找子目录添加的机构点击编辑
    def find_institution_edit_what(self, add_what):
        ils = self.institution_list
        for il in ils:
            il_text = self.find_element_by_hierarchy(
                lambda var: il.find_element_by_css_selector("span[class='text']")
            )
            print(il_text.text)
            if il_text.text == self._institution_name:
                self.click(il)
                if add_what == '编辑':
                    il_add_persons = self.find_element_by_hierarchy(
                        lambda var: il.find_elements_by_css_selector("div[class='actionitem']")
                    )
                    for iap in il_add_persons:
                        if iap.text == '编辑':
                            self.click(iap)
                            print(iap)
                            # print(iap.text)
                            break
                print(il_text.text)
                break

    # 查找子目录添加的机构点击修改上级部门
    def find_institution_edit_department(self, add_what):
        ils = self.institution_list
        for il in ils:
            il_text = self.find_element_by_hierarchy(
                lambda var: il.find_element_by_css_selector("span[class='text']")
            )
            print(il_text.text)
            if il_text.text == self._institution_name:
                self.click(il)
                if add_what == '修改上级部门':
                    il_add_persons = self.find_element_by_hierarchy(
                        lambda var: il.find_elements_by_css_selector("div[class='actionitem']")
                    )
                    for iap in il_add_persons:
                        if iap.text == '修改上级部门':
                            self.click(iap)
                            print(iap)
                            break
                print(il_text.text)
                break

    # 人员信息
    @property
    def find_person_info(self):
        return self.find_elements_by_class_name_ykb('text')
    # 编辑按钮
    @property
    def edit_person(self):
        return self.find_elements_by_class_name_ykb('actionitem')[0]
     # 修改部门按钮
    @property
    def edit_department(self):
        return self.find_elements_by_class_name_ykb('actionitem')[1]
    # 删除按钮
    @property
    def del_person(self):
        return self.find_elements_by_class_name_ykb('actionitem')[2]

    # 查找子目录添加人员点击编辑
    def find_person_edit_what(self):
        person_info = self.find_person_info
        for pi in person_info:
            if self._person_name in pi.text:
                self.click(pi)
                time.sleep(1)
                self.click(self.edit_person)
                break

    # 查找子目录添加人员点击修改部门
    def find_edit_department(self):
        person_info = self.find_person_info
        for pi in person_info:
            if self._person_name in pi.text:
                self.click(pi)
                time.sleep(1)
                self.click(self.edit_department)
                break

    # 查找子目录添加人员点击删除
    def find_del_person_what(self):
        person_info = self.find_person_info
        for pi in person_info:
            if self._person_name in pi.text:
                self.click(pi)
                time.sleep(1)
                self.click(self.del_person)
                break

    # 查找子目录添加的机构点击删除
    def find_institution_del_institution(self, add_what):
        ils = self.institution_list
        for il in ils:
            il_text = self.find_element_by_hierarchy(
                lambda var: il.find_element_by_css_selector("span[class='text']")
            )
            print(il_text.text)
            if il_text.text == self._institution_name:
                self.click(il)
                if add_what == '删除':
                    il_add_persons = self.find_element_by_hierarchy(
                        lambda var: il.find_elements_by_css_selector("div[class='actionitem']")
                    )
                    for iap in il_add_persons:
                        if iap.text == '删除':
                            self.click(iap)
                            print(iap)
                            break
                print(il_text.text)
                break

    # 查找子目录添加人员点击修改部门
    def find_edit_department_what(self, add_what):
        ils = self.institution_list
        for il in ils:
            il_text = self.find_element_by_hierarchy(
                lambda var: il.find_element_by_css_selector("span[class='text']")
            )
            print(il_text.text)
            if il_text.text == self._person_name:
                self.click(il)
                if add_what == '修改部门':
                    il_add_persons = self.find_element_by_hierarchy(
                        lambda var: il.find_elements_by_css_selector("div[class='actionitem']")
                    )
                    for iap in il_add_persons:
                        if iap.text == '修改部门':
                            self.click(iap)
                            break
                print(il_text.text)
                break

    # 获取错误弹框
    @property
    def messager_error(self):
        return self.find_element_by_css_ykb('div[class="messager error"]',3)
    # 获取错误弹框的信息
    @property
    def messager_error_info(self):
        return self.find_element_by_css_ykb('ob[class="text"]')

    # 添加人员
    def add_person_method(self):
        # 记住添加人员的名字
        self._person_name='张三' + self.random_num
        print(self._person_name + 'ccc')
        # 姓名
        self.send_keys(self.add_user_name, self._person_name)
        time.sleep(1)
        # 性别
        self.click(self.add_sex)
        time.sleep(1)
        # 手机号
        self.send_keys(self.add_tel, '13' + self.random_telnum)
        time.sleep(1)
        # 员工编号
        self.send_keys(self.add_code, self.random_num)
        time.sleep(1)
        #点击直属领导文本框
        self.click(self.direct_leader)
        time.sleep(1)
        # 搜索直属领导
        self.send_keys(self.direct_leader,'童定国')
        time.sleep(1)
        #选择直属领导
        self.click(self.sel_direct_leader)
        time.sleep(1)
        # 职级
        self.send_keys(self.rank_text, '员工' + self.random_num)
        time.sleep(1)
        # 角色
        # 下拉框
        self.click(self.sel_role)
        time.sleep(1)
        # 部门领导
        self.click(self.role_list[2])
        time.sleep(1)
        # 会计
        self.click(self.role_list[4])
        time.sleep(1)
        # 出纳
        self.click(self.role_list[7])
        time.sleep(1)
        # 收回角色下拉框
        self.click(self.pop)
        time.sleep(1)
        # 岗位
        self.send_keys(self.post_text, '测试' + self.random_num)
        time.sleep(1)
        # 邮箱
        self.send_keys(self.email_text,self.random_num + '@qq.com')
        time.sleep(1)
        # 确认按钮
        self.click(self.submit_btn1)
        time.sleep(1)
        self.driver.refresh()

        # 判断添加是否成功
        if self.messager_error is not False:
            messager_error_info = self.messager_error_info.text
            self.log.debug(messager_error_info)
            print(messager_error_info)
            return False
        else:
            return True

    #编辑
    def edit_ins_method(self):
        #修改机构名称
        self.institution_name.clear()
        time.sleep(1)
        self.send_keys(self.institution_name,'编辑自动化测试小组' + self.random_num)
        time.sleep(1)
        #修改机构编码
        self.institution_code.clear()
        time.sleep(1)
        self.send_keys(self.institution_code,self.random_num)
        time.sleep(1)
        #修改机构负责人
        self.click(self.find_element_by_css_ykb('span[class="select2-arrow"]'))
        time.sleep(1)
        self.send_keys(self.institution_person_text, '部门领导')
        time.sleep(1)
        self.click(self.institution_person_sel)
        time.sleep(1)
        #确认按钮
        self.click(self.submit_btn)
        time.sleep(1)

    #修改上级部门
    def update_department_method(self):
        #点击上级部门下拉框
        self.click(self.superior_department)
        time.sleep(1)
        #选择上级部门
        self.click(self.superior_department1)
        time.sleep(1)
        #点击确定
        self.click(self.submit_btn2)
        time.sleep(1)

    #删除机构
    def del_ins_method(self):
        self.click(self.submit_btn3)

    #编辑人员
    def edit_person_method(self):
        #编辑姓名
        self.add_user_name.clear()
        time.sleep(1)
        self.send_keys(self.add_user_name,'1张三'+self.random_num)
        time.sleep(1)
        #编辑性别
        self.click(self.add_sex1)
        time.sleep(1)
        #编辑员工编号
        self.add_code.clear()
        time.sleep(1)
        self.send_keys(self.add_code,self.random_num)
        time.sleep(1)
        #编辑直属领导
        self.click(self.direct_leader)
        time.sleep(1)
        self.direct_leader.clear()
        time.sleep(1)
        self.send_keys(self.direct_leader, '部门领导')
        time.sleep(1)
        self.click(self.sel_direct_leader)
        time.sleep(1)
        #编辑职级
        self.rank_text.clear()
        time.sleep(1)
        self.send_keys(self.rank_text,'1员工'+self.random_num)
        time.sleep(1)
        #编辑角色
        #清空已选的
        self.click(self.sel_role)
        time.sleep(1)
        # 部门领导
        self.click(self.role_list[2])
        time.sleep(1)
        # 会计
        self.click(self.role_list[4])
        time.sleep(1)
        # 出纳
        self.click(self.role_list[7])
        time.sleep(1)
        self.click(self.sel_role)
        time.sleep(1)
        # 普通员工
        self.click(self.role_list[0])
        time.sleep(1)
        # 会计
        self.click(self.role_list[4])
        time.sleep(1)
        # 收回角色下拉框
        self.click(self.pop)
        time.sleep(1)
        #编辑岗位
        self.post_text.clear()
        time.sleep(1)
        self.send_keys(self.post_text,'1测试'+self.random_num)
        time.sleep(1)
        #编辑邮箱
        self.email_text.clear()
        time.sleep(1)
        self.send_keys(self.email_text, self.random_num + '@qq.com')
        time.sleep(1)
        # 确认按钮
        self.click(self.submit_btn1)
        time.sleep(1)































