#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-06-20 Created by tongdg'

from pages.mobile_pages.login_page import LoginPage
import time

class IndexPage(LoginPage):
    # 未报销入口
    @property
    def no_res(self):
        return self.find_elements_by_class_name_ykb('ykb_banner_item')[0]
    # 记一笔入口
    @property
    def write_a_pen(self):
        return self.find_element_by_class_name_ykb('paning')

    # 打车
    @property
    def taxi(self):
        return self.find_element_by_id_ykb('taxiIcon')

    # 进入记一笔
    def enter_write_a_pen(self):
        self.click(self.no_res)
    # 创建打车消费记录
    def create_taxi_res(self):
        time.sleep(2)
        self.click(self.write_a_pen)
        js = "document.getElementById('taxiIcon').style.display='block';"
        self.driver.execute_script(js)
        print(self.taxi.is_displayed())
        self.wait_element_disappear_false('#taxiIcon')
        self.click(self.taxi)
        time.sleep(2)
        self.click(self.find_element_by_css_ykb("span[class='span-lab cellInfo rzrqsj ca9']"))
        time.sleep(1)
        self.click(self.find_element_by_css_ykb("li[class='dl jr cur']"))
        time.sleep(1)
        self.send_keys(self.find_element_by_id_ykb('fromPlace'),'111')
        time.sleep(1)
        self.send_keys(self.find_element_by_id_ykb('toPlace'),'222')
        time.sleep(1)
        self.click(self.find_elements_by_class_name_ykb('c9')[0])
        time.sleep(1)
        self.click(self.find_element_by_css_ykb('#keybord > span:nth-child(1)'))
        time.sleep(1)
        self.click(self.find_element_by_id_ykb('submitNumCal'))
        time.sleep(1)
        self.click(self.find_element_by_css_ykb('#setting > div.mui-bar.mui-bar-tab.ab > button.mui-btn.themebgStyle.themeBtn17ab'))
        time.sleep(2)

    # 创建多笔消费记录
    def multiple_taxi_res(self):
        self.enter_write_a_pen()
        while True:
            self.create_taxi_res()






