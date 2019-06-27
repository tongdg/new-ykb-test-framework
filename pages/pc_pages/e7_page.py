#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-06-27 Created by tongdg'

from pages.base_page import BasePage
import time
from common.utils import Utils
from selenium.webdriver.common.action_chains import ActionChains

class E7Page(BasePage):

    # 登录操作
    def e7_login(self):
        self.driver.maximize_window()
        self.driver.get('http://192.168.64.12:9000/pages/home.jsp')
        self.send_keys(self.find_element_by_id_ykb('usernameInput'),'y1')
        self.send_keys(self.find_element_by_id_ykb('passwordInput'),'1')
        self.click(self.find_element_by_id_ykb('submitButton'))

    # 进入定时任务管理
    def enter_time_manage(self):
        ActionChains(self.driver).move_to_element(self.find_element_by_id_ykb('fist_0')).perform()
        ActionChains(self.driver).move_to_element(self.find_element_by_css_ykb("a[title='管理员日常维护']")).perform()
        self.click(self.find_element_by_css_ykb("a[title='定时任务管理']"))

    # 查找指定的定时任务并点击
    def find_task_and_click(self,name=None):
        time.sleep(1)
        self.driver.switch_to_frame(self.find_element_by_id_ykb('main'))
        time.sleep(1)
        self.driver.switch_to_frame(self.find_element_by_id_ykb('ie_px'))
        all_tr = self.find_element_by_hierarchy(lambda var : self.find_element_by_id_ykb('tbl').find_elements_by_tag_name('tr'))
        print(len(all_tr))
        for a_tr in all_tr:
            all_td = self.find_element_by_hierarchy(lambda var : a_tr.find_elements_by_tag_name('td'),3)
            if all_td is not False:
                if name is not None:
                    if all_td[1].text == name:
                        self.click(all_td[11])
                        time.sleep(1)
                        self.driver.switch_to_frame(self.find_element_by_id_ykb('jd_iframe'))
                        time.sleep(1)
                        self.click(self.find_element_by_id_ykb('closeBtn'))
                        time.sleep(1)
                        print(1)
                        self.driver.switch_to_frame(self.find_element_by_id_ykb('main'))
                        time.sleep(1)
                        self.driver.switch_to_frame(self.find_element_by_id_ykb('ie_px'))
                        time.sleep(1)
                        self.driver.switch_to_frame(self.find_element_by_id_ykb('jd_iframe'))
                        time.sleep(1)
                        print(self.find_element_by_id_ykb('msgContentId').text)
                        if u'执行成功' in self.find_element_by_id_ykb('msgContentId').text:
                            print(name+'执行成功！')
                        else:
                            print(name+'执行失败！')
                        self.click(self.find_element_by_id_ykb('closeBtn'))
                        break
                else:
                    self.click(all_td[11])
                    time.sleep(1)
                    self.driver.switch_to_frame(self.find_element_by_id_ykb('jd_iframe'))
                    time.sleep(1)
                    self.click(self.find_element_by_id_ykb('closeBtn'))
                    time.sleep(1)
                    print(1)
                    self.driver.switch_to_frame(self.find_element_by_id_ykb('main'))
                    time.sleep(1)
                    self.driver.switch_to_frame(self.find_element_by_id_ykb('ie_px'))
                    time.sleep(1)
                    self.driver.switch_to_frame(self.find_element_by_id_ykb('jd_iframe'))
                    time.sleep(1)
                    print(self.find_element_by_id_ykb('msgContentId').text)
                    if u'执行成功' in self.find_element_by_id_ykb('msgContentId').text:
                        print(name + '执行成功！')
                    else:
                        print(name + '执行失败！')
                    self.click(self.find_element_by_id_ykb('closeBtn'))
                    break
            else:
                print('超时！')

    # 执行多个定时任务
    def multiple_execute_task(self,names=None):
        if names is None:
            self.find_task_and_click()
        else:
            for name in names:
                self.find_task_and_click(name)









