#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-05-29 Created by tongdg'

from pages.base_page import BasePage
import time

class LoginPage(BasePage):

    """
        页面元素
    """
    @property
    def login_btn(self):
        return self.find_element_by_link_text_ykb('登录')

    @property
    def register_btn(self):
        return self.find_element_by_link_text_ykb('免费体验')

    @property
    def username(self):
        return self.find_element_by_id_ykb('LoginName')

    @property
    def password(self):
        return self.find_element_by_id_ykb('Password')

    @property
    def login_btn2(self):
        return self.find_element_by_id_ykb('loginBtn')

    #
    @property
    def login_success_flag(self):
        return self.find_element_by_css_ykb("span[class='seldropdown']")

    """
        我的账号 15216625816 123456 童定国
    """
    def login_test_person(self):
        self.driver.maximize_window()
        time.sleep(1)
        # 'http://120.132.23.147:840/logon'  'https://www.51ykb.com/Logon'  120.132.23.147:840
        self.driver.get('http://120.132.23.147:840/logon')
        self.click(self.login_btn)
        time.sleep(1)
        self.send_keys(self.username,'15216625816')
        time.sleep(1)
        self.send_keys(self.password,'123456')
        time.sleep(1)
        self.click(self.login_btn2)
        time.sleep(2)
        # 判断登录是否成功
        if self.login_success_flag is False:
            self.log.debug('--[ tongdg login fail]')
            return False
        else:
            self.log.debug('--[tongdg ok]')
            return True

    """
        普通员工 16700000001 
    """
    def login_ordinary_staff(self):
        self.driver.maximize_window()
        time.sleep(1)
        # 'http://120.132.23.147:840/logon'  'https://www.51ykb.com/Logon'  120.132.23.147:840
        self.driver.get('http://120.132.23.147:840/logon')
        self.click(self.login_btn)
        time.sleep(1)
        self.send_keys(self.username, '16700000001')
        time.sleep(1)
        self.send_keys(self.password, '123456')
        time.sleep(1)
        self.click(self.login_btn2)
        time.sleep(2)
        # 判断登录是否成功
        if self.login_success_flag is False:
            self.log.debug('--[ ordinary staff fail]')
            return False
        else:
            self.log.debug('--[ ordinarystaff ok]')
            return True
























