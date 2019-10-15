#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from pages.mobile_pages.zfk_create_Unreimbursement import zfk_create_Unreimbursement
class zfk_create_Unreimbursement_case(unittest.TestCase):
    def setUp(self):
        self.zfk_create_Unreimbursement = zfk_create_Unreimbursement(webdriver.Chrome())
        self.zfk_create_Unreimbursement.Login_Person()  # 登录账号
        self.zfk_create_Unreimbursement.Choince_Login_god()
        #这里切换成移动端模式
        options = webdriver.ChromeOptions()
        mobileEmulation = {'deviceName': 'iPhone 6 Plus'}
        options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver=webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
        MobileUrl=self.zfk_create_Unreimbursement.Get_mobile_url()
        self.zfk_create_Unreimbursement= zfk_create_Unreimbursement(self.driver)
        self.driver.get(MobileUrl)
        self.zfk_create_Unreimbursement.UnReimbursement()
    def test_Login_mobile_Unreimbursement(self):

         self.zfk_create_Unreimbursement.log.info('[--首页-未报销-全选删除开始]')
         self.UnReimbursement_result=self.zfk_create_Unreimbursement.UnReim_Remember_whit_Delete()
         self.assertTrue(self.UnReimbursement_result)

    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()

