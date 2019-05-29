#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-05-29 Created by tongdg'

import time
from selenium.webdriver.support.ui import WebDriverWait

__author__ = 'tongdg'


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    """
        常用公用方法
    """

    # 生成报告的名字格式
    @property
    def generate_report_time(self):
        return time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime())

    # 获取年月日的格式为XXXX(年)-XX(月)-XX(日)
    @property
    def get_year_month_day(self):
        local_time = time.localtime()
        year = str(local_time.tm_year)
        month = local_time.tm_mon
        if month < 10:
            month = '0' + str(month)
        else:
            month = str(month)
        day = local_time.tm_mday
        if day < 10:
            day = '0' + str(day)
        else:
            day = str(day)
        local_time = year + '-' + month + '-' + day
        return local_time

    # 获取年月日的格式为XX(时)-XX(分)-XX(秒)
    @property
    def get_hour_min_sec(self):
        local_time = time.localtime()
        hour = local_time.tm_hour
        if hour < 10:
            hour = '0' + str(hour)
        else:
            hour = str(hour)
        min = local_time.tm_min
        if min < 10:
            min = '0' + str(min)
        else:
            min = str(min)
        sec = local_time.tm_sec
        if sec < 10:
            sec = '0' + str(sec)
        else:
            sec = str(sec)
        local_time = hour + '-' + min + '-' + sec
        return local_time

    """
        常用定位方法
        1.id,name,class定位，id唯一
        2.link text,partial test定位
    """

    # 每隔0.5秒去查找这个id所对应的元素，超过timeout,单位(s)，抛出TimeoutException.
    # WebDriverWait方法可以设置每隔多少秒扫描，以及找不到抛出的异常类型.
    # 这里需要注意，用显示等待找不到元素抛出的是超时的错误，而直接用find去寻找，返回的是元素找不到的错误，这个以后
    # 判断元素是否找到有很大的作用

    # 元素id定位，唯一标识
    def find_element_by_id_tdg(self, id, timeout=10):
        """
        :param timeout:最长超时时间
        :param id:需要定位的元素的id
        :return:返回找到的元素
        """
        return WebDriverWait(self.driver, timeout).until(lambda driver=self.driver : driver.find_element_by_id(id))
    # 元素的name属性定位，不唯一
    def find_element_by_name_tdg(self, name, timeout=10):
        return WebDriverWait(self.driver, timeout).until(lambda driver=self.driver : driver.find_element_by_name(name))
    # 元素的标签名字定位，不唯一
    def find_element_by_tag_name_tdg(self, tagname, timeout=10):
        return WebDriverWait(self.driver, timeout).until(lambda driver=self.driver : driver.find_element_by_tag_name(tagname))
    # 元素class的名字定位，不唯一
    def find_element_by_class_name_tdg(self, classname, timeout=10):
        return WebDriverWait(self.driver, timeout).until(lambda driver=self.driver : driver.find_element_by_class_name(classname))
    # 链接的内容定位，也是不唯一的
    def find_element_by_link_text_tdg(self, linktext, timeout=10):
        return WebDriverWait(self.driver, timeout).until(lambda driver=self.driver : driver.find_element_by_link_text(linktext))
    # 部门链接内容定位，不唯一
    def find_element_by_partial_link_text_tdg(self, partiallinktext, timeout=10):
        return WebDriverWait(self.driver, timeout).until(lambda driver=self.driver : driver.find_element_by_partial_link_text(partiallinktext))
    """
        xpath定位 建议少用  维护成本大  尽量向CSS转
    """

    """
        css定位
    """

    def find_element_by_css_tdg(self, css, timeout=10):
        return WebDriverWait(self.driver, timeout).until(lambda driver=self.driver : driver.find_element_by_css_selector(css))

    def find_elements_by_css_tdg(self, css, timeout=10):
        return WebDriverWait(self.driver, timeout).until(lambda driver=self.driver : driver.find_elements_by_css_selector(css))

    """
        层级定位,应用一般是需要定位到下层的一组一样的元素
    """
    def find_element_by_hierarchy(self, method, message, timeout=10):
        return WebDriverWait(self.driver, timeout).until(method, message=message)

    """
        执行javascript脚本
        这部分的类容等具体的实际应用
    """

   # ----------------------------------------------------------------------------------------------
   # 以上方法基本够实际开发




































