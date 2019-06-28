#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'2019-05-29 Created by Zhangfukai'
import unittest
from selenium import webdriver
import time
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
        driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
        MobileUrl = self.zfk_mobile_index_Page.Get_mobile_url()
        #这里以移动端打开的浏览器实例化的driver,在不继承Basepage的driver时是无法使用Basepage的driver方法
        self.zfk_mobile_index_Page= zfk_Mobile_index_page(driver)
        driver.get(MobileUrl)
        time.sleep(3)
        # 跳转移动端首页
    def test_Login_mobile_enterprise(self):
        time.sleep(3)
        #未报销
        self.zfk_mobile_index_Page.Make_order
        time.sleep(4)
        # self.zfk_mobile_index_Page.UnReimbursement_back
        # time.sleep(4)
        # #报销中
        # self.zfk_mobile_index_Page.ReimbursementIng
        # time.sleep(4)
        # self.zfk_mobile_index_Page.ReimbursementIng_back
        # time.sleep(4)
        # #待还借款
        # self.zfk_mobile_index_Page.Stay_still_owed
        # time.sleep(4)
        # self.zfk_mobile_index_Page.ReimbursementIng_back
        # time.sleep(4)
        # self.zfk_mobile_index_Page.Remember_whit()
        # time.sleep(5)
        # self.zfk_mobile_index_Page.Remember_whit_back()
        # time.sleep(5)
        # self.zfk_mobile_index_Page.Make_order()
        # time.sleep(5)
        # self.zfk_mobile_index_Page.Make_order_back()
        # time.sleep(5)
        # self.zfk_mobile_index_Page.Statement()
        # time.sleep(5)
        # self.zfk_mobile_index_Page.Statement_back()
        # time.sleep(5)
        # self.zfk_mobile_index_Page.Travel_booking()
        # time.sleep(5)
        # self.zfk_mobile_index_Page.Travel_booling_back()
        # time.sleep(5)
        # self.zfk_mobile_index_Page.Store_Purchase()
        # time.sleep(5)
        # self.zfk_mobile_index_Page.Store_Purchase_back()
        # time.sleep(5)
        # self.zfk_mobile_index_Page.Travel_car()
        # time.sleep(5)
        # self.zfk_mobile_index_Page.Travel_car_back()
        # time.sleep(50)
        # pass
    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()

