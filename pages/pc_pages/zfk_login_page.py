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

    """
        提单人
    """
    def login_mention_person(self):
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



