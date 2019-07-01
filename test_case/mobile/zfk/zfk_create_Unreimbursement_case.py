#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from pages.mobile_pages.zfk_UnReimbursement_page.zfk_create_Unreimbursement import zfk_create_Unreimbursement
from pages.mobile_pages.zfk_bills_page.zfk_bills_MyBills import zfk_bills_MyBills
import time


class zfk_create_Unreimbursement_case(unittest.TestCase):
    def setUp(self):
        self.zfk_create_Unreimbursement = zfk_create_Unreimbursement(webdriver.Chrome())
        self.zfk_create_Unreimbursement.Login_Person()  # 登录账号
        self.zfk_create_Unreimbursement.Chionce_enterprise()
        #这里切换成移动端模式
        options = webdriver.ChromeOptions()
        mobileEmulation = {'deviceName': 'iPhone 6 Plus'}
        options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver=webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
        MobileUrl=self.zfk_create_Unreimbursement.Get_mobile_url()
        self.zfk_create_Unreimbursement= zfk_create_Unreimbursement(self.driver)
        self.driver.get(MobileUrl)
        self.Test = zfk_bills_MyBills(self.driver)
    def test_Login_mobile_enterprise(self):
         time.sleep(5)
         self.zfk_create_Unreimbursement.UnReimbursement
         self.zfk_create_Unreimbursement.UnReim_Remember_whit_Delete()
         self.zfk_create_Unreimbursement.UnReim_Remember_whit_Submit_Travel()
         self.zfk_create_Unreimbursement.back()
         self.zfk_create_Unreimbursement.UnReim_Remember_whit_Submit_Cost()
         self.Test.Entrance_My_bills()

         time.sleep(5000)
    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()

