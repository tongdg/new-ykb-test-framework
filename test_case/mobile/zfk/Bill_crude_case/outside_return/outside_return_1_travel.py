#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'2019-05-29 Created by Zhangfukai'
import unittest
from selenium import webdriver
import time
from pages.mobile_pages.Bill_crud_page.Bill_order_submit_page import Bill_my_order_page
from pages.mobile_pages.Bill_crud_page.out_side_return.out_side_1_page import out_side_1_page
from pages.mobile_pages.zfk_mobile_index_page import zfk_Mobile_index_page
class outside_return_1_borrow(unittest.TestCase):
    def setUp(self):
        self.out_side_1_page = zfk_Mobile_index_page(webdriver.Chrome())
        self.out_side_1_page.Login_Person()  # 登录账号
        self.out_side_1_page.Choince_Login_god()#登陆企业
        options = webdriver.ChromeOptions()
        #新开浏览器，以Mobile的格式打开
        mobileEmulation = {'deviceName': 'iPhone 6 Plus'}
        options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
        MobileUrl = self.out_side_1_page.Get_mobile_url()
        #这里以移动端打开的浏览器实例化的driver,在不继承Basepage的driver时是无法使用Basepage的driver方法
        self.out_side_1_page= out_side_1_page(self.driver)
        self.driver.get(MobileUrl)
        time.sleep(3)
        # 跳转到我的单据
    def test_My_bills(self):
        #进入待提交
        self.out_side_1_page.To_approval_return_travel()
        #执行退回
        self.out_side_1_page.return_order_travel()
        time.sleep(2)
    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()

