#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-05-29 Created by tongdg'

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from common.logger import Log
from selenium.common.exceptions import TimeoutException,NoSuchElementException

class BasePage(object):
    # 存放图片的集合
    # 传入driver和日志路径
    # path传相对路径

    def __init__(self, driver, path=None):
        self.driver = driver
        self.log = Log(path)

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
    def find_element_by_id_ykb(self, id, timeout=10):
        """
        :param timeout:最长超时时间
        :param id:需要定位的元素的id
        :return:返回找到的元素
        """
        try:
            ele = WebDriverWait(self.driver, timeout).until(lambda driver=self.driver : driver.find_element_by_id(id))
            self.log.info('--[ ' + id + ' find ok]' )
            return ele
        except TimeoutException:
            # self.driver.get_screenshot_as_file("/screenshot/" + Utils.generate_time() + ".png")
            self.log.error('--[ ' + id + ' find timeout]')
            return False

    # 元素的name属性定位，不唯一
    def find_element_by_name_ykb(self, name, timeout=10):
        try:
            ele = WebDriverWait(self.driver, timeout).until(lambda driver=self.driver : driver.find_element_by_name(name))
            self.log.info('--[ ' + name + ' find ok]' )
            return ele
        except TimeoutException:
            # self.driver.get_screenshot_as_file("/screenshot/" + Utils.generate_time() + ".png")
            self.log.error('--[ ' + name + ' find timeout]')
            return False

    # 元素的标签名字定位，不唯一
    def find_element_by_tag_name_ykb(self, tagname, timeout=10):
        try:
            ele = WebDriverWait(self.driver, timeout).until(lambda driver=self.driver : driver.find_element_by_tag_name(tagname))
            self.log.info('--[ ' + tagname + ' find ok]' )
            return ele
        except TimeoutException:
            # self.driver.get_screenshot_as_file("/screenshot/" + Utils.generate_time() + ".png")
            self.log.error('--[ ' + tagname + ' find timeout]')
            return False

    # 元素class的名字定位，不唯一
    def find_element_by_class_name_ykb(self, classname, timeout=10):
        try:
            ele = WebDriverWait(self.driver, timeout).until(lambda driver=self.driver : driver.find_element_by_class_name(classname))
            self.log.info('--[ ' + classname + ' find ok]' )
            return ele
        except TimeoutException:
            # self.driver.get_screenshot_as_file("/screenshot/" + Utils.generate_time() + ".png")
            self.log.error('--[ ' + classname + ' find timeout]')
            return False

    # 链接的内容定位，也是不唯一的
    def find_element_by_link_text_ykb(self, linktext, timeout=10):
        try:
            ele = WebDriverWait(self.driver, timeout).until(lambda driver=self.driver : driver.find_element_by_link_text(linktext))
            self.log.info('--[ ' + linktext + ' find ok]' )
            return ele
        except TimeoutException:
            # self.driver.get_screenshot_as_file("/screenshot/" + Utils.generate_time() + ".png")
            self.log.error('--[ ' + linktext + ' find timeout]')
            return False

    # 部门链接内容定位，不唯一
    def find_element_by_partial_link_text_ykb(self, partiallinktext, timeout=10):
        try:
            ele = WebDriverWait(self.driver, timeout).until(lambda driver=self.driver : driver.find_element_by_partial_link_text(partiallinktext))
            self.log.info('--[ ' + partiallinktext + ' find ok]' )
            return ele
        except TimeoutException:
            # self.driver.get_screenshot_as_file("/screenshot/" + Utils.generate_time() + ".png")
            self.log.error('--[ ' + partiallinktext + ' find timeout]')
            return False

    """
        xpath定位 建议少用  维护成本大  尽量向CSS转
    """

    """
        css定位
    """

    def find_element_by_css_ykb(self, css, timeout=10):
        try:
            ele = WebDriverWait(self.driver, timeout).until(lambda driver=self.driver : driver.find_element_by_css_selector(css))
            self.log.info('--[ ' + css + ' find ok]' )
            return ele
        except TimeoutException:
            # self.driver.get_screenshot_as_file("/screenshot/" + Utils.generate_time() + ".png")
            self.log.error('--[ ' + css + ' find timeout]')
            return False

    def find_elements_by_css_ykb(self, css, timeout=10):
        try:
            ele =  WebDriverWait(self.driver, timeout).until(lambda driver=self.driver : driver.find_elements_by_css_selector(css))
            self.log.info('--[ ' + css + ' list find ok]' )
            return ele
        except TimeoutException:
            # self.driver.get_screenshot_as_file("/screenshot/" + Utils.generate_time() + ".png")
            self.log.error('--[ ' + css + ' list find timeout]')
            return False
        # 部门链接内容定位，不唯一


#create by zfk need use that
#-------------
    def current_window_handle(self):
        return self.driver.current_window_handle

    def window_handles(self):
        return self.driver.window_handles

    def switchTo_default_content(self):
        self.driver.switch_to.default_content()

    def switch_to_window(self):
        return  self.driver.switch_to.window()

    def switch_title(self):
       return self.driver.title
    def page_source(self):
        return self.driver.page_source

    def find_element_by_xpath(self):
        return self.find_element_by_xpath()

    def find_elements_by_xpath(self,Businese):
        return self.driver.find_elements_by_xpath(Businese)

    def find_elements_by_class(self,a):
        return self.find_elements_by_css_ykb(a)


    def current_url(self):
        return self.driver.current_url

    def get_cookies(self):
        return self.driver.get_cookies()

    def add_cookie(self):
        return self.driver.add_cookie()

    def refresh(self):
        return self.driver.refresh()
    def back(self):
        return self.driver.back()
    def implicitly_wait(self):
        return self.driver.implicitly_wait()
    """
        层级定位,应用一般是需要定位到下层的一组一样的元素
    """
    def find_element_by_hierarchy(self, method, timeout=10):
        try:
            ele = WebDriverWait(self.driver, timeout).until(method)
            self.log.info('--[ ' + method + ' find ok]' )
            return ele
        except TimeoutException:
            # self.driver.get_screenshot_as_file("/screenshot/" + Utils.generate_time() + ".png")
            self.log.error('--[ ' + method + ' find timeout]')
            return False

    """
        执行javascript脚本
        这部分的类容等具体的实际应用
    """
    """
        退出浏览器
    """
    def quit(self):
        self.driver.quit()
        self.log.info('--[ exit browser ]')

    # 二次封装click方法
    def click(self, ele):
        if ele is False:
            raise NoSuchElementException('查找超时，请维护脚本！')
        else:
            ele.click()
            self.log.info('--[ click ok ]')

    # 二次封装send_keys方法
    def send_keys(self,ele,value):
        if ele is False:
            raise NoSuchElementException('查找超时，请维护脚本！')

        else:
            ele.send_keys(value)
            self.log.info('--[ send_keys ok ]')

   # ----------------------------------------------------------------------------------------------
   # 以上方法基本够实际开发




































