#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-05-29 Created by tongdg'
from config.zfk_config import returnIntegrateUrl
from pages.base_page import BasePage
import time
class Login_HouTaiPage(BasePage):
    '页面元素'
    @property
    def loginName(self):
        return self.find_element_by_id_ykb('loginname')
    @property
    def loginPassWord(self):
        return self.find_element_by_id_ykb('password')
    @property
    def loginButton(self):
        return  self.find_element_by_id_ykb('login')


    #登录人  这里后期调整逻辑，暂留一个人
    def login_person(self):
        self.driver.maximize_window()
        time.sleep(1)
        self.driver.get(returnIntegrateUrl())
        time.sleep(1)
        self.send_keys(self.loginName, 'tongdingguo')
        time.sleep(1)
        self.send_keys(self.loginPassWord, '123456')
        time.sleep(1)
        self.click(self.loginButton)
        time.sleep(2)





