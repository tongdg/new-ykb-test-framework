#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-06-20 Created by tongdg'

from pages.mobile_pages.login_page import LoginPage
from selenium.webdriver.common.action_chains import ActionChains
import time


class IndexPage(LoginPage):
    def __init__(self,driver,path):
        super(IndexPage, self).__init__(driver=driver,path=path)
        self.train_num = 0
        self.exceeding_standard_num = 0
        self.train_seat_num = 0

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

    # 商旅预定
    @property
    def business_travel_reservation(self):
        return self.find_elements_by_class_name_ykb('ykb_main_item')[3]

    # 火车
    @property
    def train(self):
        return self.find_element_by_css_ykb("div[class='rows_link rows_nobd icon_on']")

    # 出发地
    @property
    def train_from_city(self):
        return self.find_element_by_class_name_ykb('departure-city',20)
    # 搜索城市框
    @property
    def train_query_city(self):
        return self.find_element_by_name_ykb('search')
    # 选择第一个城市
    @property
    def train_choose_first_city(self):
        return self.find_elements_by_class_name_ykb('city-list')[0]
    # 目的地
    @property
    def train_to_city(self):
        return self.find_element_by_class_name_ykb('arrival-city')

    # 出行日期   #container > div.index-content > button
    @property
    def train_time(self):
        return self.find_element_by_class_name_ykb('gather')

    # 选择出行日期
    @property
    def train_choose_time(self):
        return self.find_element_by_css_ykb("span[class='active single']")

    # 查询按钮
    @property
    def train_query_btn(self):
        return self.find_element_by_css_ykb('#container > div.index-content > button')

    # 等待数据加载loding
    def wait_train_data_loding(self):
        return self.wait_element_disappear_true("div[class='mint-indicator-wrapper']")

    # 选择所有车次
    @property
    def train_choose_all_data(self):
        return self.find_element_by_css_ykb("a[class='mint-tab-item is-selected']")

    # 所有车次数据列表
    @property
    def train_all_data_list(self):
        return self.find_element_by_hierarchy(
            lambda var : self.driver.find_element_by_css_selector("div[class='train-list-box']").find_elements_by_tag_name('li')
        )

    # 坐席列表
    @property
    def train_seating_list(self):
        return self.find_element_by_hierarchy(
            lambda var : self.driver.find_element_by_class_name('seating-list').find_elements_by_class_name('order-button')
        )

    # 提交
    @property
    def train_submit(self):
        return self.find_element_by_css_ykb("span[class='booking']")

    # 出差事由
    @property
    def evecation_reason(self):
        return self.find_element_by_id_ykb('desc')

    # 提交申请
    @property
    def evecation_bill_apply(self):
        return self.find_element_by_id_ykb('submitApply')

    # 确定按钮
    @property
    def evecation_bill_confirm(self):
        return self.find_element_by_id_ykb('confirmBtn')

    # 确定出票
    @property
    def evecation_bill_confirm_pop(self):
        return self.find_element_by_css_ykb('body > div.mui-popup.mui-popup-in > div.mui-popup-buttons > span.mui-popup-button.mui-popup-button-bold')

    def enter_train_crea(self,from_city,to_city):
        time.sleep(1)
        self.click(self.business_travel_reservation)
        self.create_train_bill(from_city,to_city)

    def create_train_bill(self,from_city,to_city):
        time.sleep(1)
        self.click(self.train)
        time.sleep(1)
        self.driver.refresh()
        self.wait_train_data_loding()
        self.click(self.train_from_city)
        time.sleep(1)
        self.send_keys(self.train_query_city, from_city)
        time.sleep(1)
        self.click(self.train_choose_first_city)
        time.sleep(1)
        self.click(self.train_to_city)
        time.sleep(1)
        self.train_query_city.clear()
        self.send_keys(self.train_query_city, to_city)
        time.sleep(1)
        self.click(self.train_choose_first_city)
        time.sleep(1)
        self.click(self.train_query_btn)
        time.sleep(1)
        self.wait_train_data_loding()
        self.click(self.train_choose_all_data)
        time.sleep(1)
        dl = self.train_all_data_list
        dl_num = len(dl)
        print('火车数量：'+ str(dl_num))
        while self.train_num < dl_num:
            print('当前火车的数量:' + str(self.train_num))
            train_result = self.find_element_by_hierarchy(
                lambda var : dl[self.train_num].find_element_by_class_name('sold-out'),3
            )
            print('火车无价结果：' + str(train_result))
            if train_result is False:
                if self.train_num>=5:
                    if self.train_num+2 < dl_num:
                        ActionChains(self.driver).move_to_element(dl[self.train_num+2]).perform()
                time.sleep(1)
                self.click(dl[self.train_num])
                time.sleep(2)
                sl = self.train_seating_list
                sl_num = len(sl)
                print('坐席数量：' + str(sl_num))
                while self.train_seat_num < sl_num:
                    print('当前火车坐席的数量：' + str(self.train_seat_num))
                    seats_button = self.find_element_by_hierarchy(
                        lambda var: sl[self.train_seat_num].find_element_by_tag_name('button')
                    )
                    print(seats_button.text)
                    if seats_button.text != '售完':
                        self.click(sl[self.train_seat_num])
                        time.sleep(1)
                        self.click(self.train_submit)
                        self.train_seat_num = self.train_seat_num + 1
                        time.sleep(1)
                        self.send_keys(self.evecation_reason,'当前火车：'+str(self.train_num)+'，当前座次：'+str(self.train_seat_num))
                        time.sleep(2)
                        self.click(self.evecation_bill_apply)
                        time.sleep(1)
                        self.click(self.evecation_bill_confirm)
                        time.sleep(1)
                        self.click(self.evecation_bill_confirm_pop)
                        time.sleep(1)
                        self.train_seat_num = 0
                        self.train_num = self.train_num + 1
                        return self.create_train_bill(from_city,to_city)
                    else:
                        self.train_seat_num = self.train_seat_num + 1
            else:
                self.train_num = self.train_num + 1





































































































