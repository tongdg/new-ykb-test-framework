#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'2019-05-29 Created by Zhangfukai'
import unittest
from selenium import webdriver
import time

from pages.mobile_pages.zfk_bills_MyBills import zfk_bills_MyBills
from pages.mobile_pages.zfk_mobile_index_page import zfk_Mobile_index_page
class zfk_mobile_index_case(unittest.TestCase):
    def setUp(self):
        self.zfk_mobile_index_Page = zfk_Mobile_index_page(webdriver.Chrome())
        self.zfk_mobile_index_Page.Login_Person()  # 登录账号
        self.zfk_mobile_index_Page.Chionce_enterprise()#登陆企业
        options = webdriver.ChromeOptions()
        #新开浏览器，以Mobile的格式打开
        mobileEmulation = {'deviceName': 'iPhone 6 Plus'}
        options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
        MobileUrl = self.zfk_mobile_index_Page.Get_mobile_url()
        #这里以移动端打开的浏览器实例化的driver,在不继承Basepage的driver时是无法使用Basepage的driver方法
        self.zfk_bills_MyBills= zfk_bills_MyBills(self.driver)
        self.driver.get(MobileUrl)
        time.sleep(3)
        # 跳转到我的单据
    def test_My_bills(self):
        self.zfk_bills_MyBills.Entrance_My_bills()
        self.zfk_bills_MyBills.In_approval_recall()
        for i in range(1,5):
            if i%2==0:
                self.zfk_bills_MyBills.In_recall_order()
            else:
                self.zfk_bills_MyBills.recall_order()
        #待提交作废
        self.zfk_bills_MyBills.To_submit()
        time.sleep(2)
        # for j in range(1,4):
        #     self.zfk_bills_MyBills.delete_order()
    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()

