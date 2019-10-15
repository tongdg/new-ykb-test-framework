#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-05-29 Created by zhangfukai'
from config.zfk_config import returnIntegrateUrl
from pages.base_page import BasePage
import time
class Login_HouTaiPage(BasePage):
    def loginName(self):
        loginName = self.find_element_by_id_ykb('loginname')
        return loginName
    def loginPassWord(self):
        password=self.find_element_by_id_ykb('password')
        return password
    def loginButton(self):
        login=self.find_element_by_id_ykb('login')
        return login
    # -------------------------------------Cut-Off Rule-----------------------------------------------------------
    #登录人  这里后期调整逻辑，暂留一个人
    def Login_Person(self):
        self.driver.maximize_window()
        time.sleep(1)
        self.driver.get(returnIntegrateUrl())
        time.sleep(3)
        self.send_keys(self.loginName(),"tongdingguo")
        time.sleep(3)
        self.send_keys(self.loginPassWord(),"123456")
        time.sleep(3)
        self.click(self.loginButton())
        time.sleep(2)





