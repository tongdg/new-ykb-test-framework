#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'2019-05-29 Created by Zhangfukai'
import unittest
from selenium import webdriver
import time
from pages.mobile_pages.Bill_crud_page.Bill_my_order_delete_page import Bill_my_order_page
from pages.mobile_pages.zfk_mobile_index_page import zfk_Mobile_index_page
class zfk_mobile_index_case(unittest.TestCase):
    def setUp(self):
        self.zfk_mobile_index_Page = zfk_Mobile_index_page(webdriver.Chrome())
        self.zfk_mobile_index_Page.Login_Person()  # 登录账号
        self.zfk_mobile_index_Page.Choince_Login_god()#登陆企业
        options = webdriver.ChromeOptions()
        #新开浏览器，以Mobile的格式打开
        mobileEmulation = {'deviceName': 'iPhone 6 Plus'}
        options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
        MobileUrl = self.zfk_mobile_index_Page.Get_mobile_url()
        #这里以移动端打开的浏览器实例化的driver,在不继承Basepage的driver时是无法使用Basepage的driver方法
        self.Bill_my_order_page= Bill_my_order_page(self.driver)
        self.driver.get(MobileUrl)
        time.sleep(3)
        # 跳转到我的单据
    def test_My_bills(self):
        #进入待提交
        self.Bill_my_order_page.To_submit()
        self.Bill_my_order_page.delete_order_travel()
        self.Bill_my_order_page.log.info('差旅报销单-作废成功-')
        time.sleep(2)
    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()

