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
        return self.wait_element_disappear_true("div[class='mint-indicator-mask']")

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
            lambda var : self.driver.find_element_by_class_name('seating-list').find_elements_by_class_name('list')
        )

    # 提交
    @property
    def train_submit(self):
        return self.find_element_by_css_ykb("span[class='booking']")

    # 创建含有火车票的出差申请单，保存
    def create_train_bill(self):
        time.sleep(1)
        self.click(self.business_travel_reservation)
        time.sleep(1)
        self.click(self.train)
        self.click(self.train_from_city)
        time.sleep(1)
        self.send_keys(self.train_query_city, '北京')
        time.sleep(1)
        self.click(self.train_choose_first_city)
        time.sleep(1)
        self.click(self.train_to_city)
        time.sleep(1)
        self.train_query_city.clear()
        self.send_keys(self.train_query_city, '上海')
        time.sleep(1)
        self.click(self.train_choose_first_city)
        time.sleep(1)
        self.click(self.train_query_btn)
        self.wait_train_data_loding()















































































