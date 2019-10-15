#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'2019-05-29 Created by Zhangfukai'
import unittest
from selenium import webdriver
import time

from pages.mobile_pages.zfk_create_Unreimbursement import zfk_create_Unreimbursement
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
        self.zfk_mobile_index_Page= zfk_Mobile_index_page(self.driver)
        self.zfk_create_Unreimbursement = zfk_create_Unreimbursement(self.driver)
        self.driver.get(MobileUrl)
        time.sleep(3)
    # 跳转移动端首页-作为上帝视角所有的功能入口是否跳转正常
    def test_Login_mobile_addressTest(self):
        self.zfk_mobile_index_Page.log.info('[--首页-我要制单-跳转地址检测开始-采购申请单]')
        self.Make_order_result = self.zfk_mobile_index_Page.Make_order_Store_Purchase()
        self.assertTrue(self.Make_order_result)

    def tearDown(self):
        time.sleep(5)
        pass
if __name__=="__main__":
    unittest.main()

