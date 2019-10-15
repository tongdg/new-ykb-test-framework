#!/usr/bin/env python3
import unittest
from selenium import webdriver
import time

from pages.mobile_pages.Photograph_writ.photograph_writ_page import photograph_writ_page
from pages.mobile_pages.zfk_create_Unreimbursement import zfk_create_Unreimbursement
from pages.mobile_pages.zfk_mobile_index_page import zfk_Mobile_index_page

class photograph_write_case_1(unittest.TestCase):
    def setUp(self):
        self.photograph_writ_page = zfk_Mobile_index_page(webdriver.Chrome())
        self.photograph_writ_page.Login_Person()  # 登录账号
        self.photograph_writ_page.Choince_Login_god()#登陆企业
        options = webdriver.ChromeOptions()
        #新开浏览器，以Mobile的格式打开
        mobileEmulation = {'deviceName': 'iPhone 6 Plus'}
        options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
        MobileUrl = self.photograph_writ_page.Get_mobile_url()
        #这里以移动端打开的浏览器实例化的driver,在不继承Basepage的driver时是无法使用Basepage的driver方法
        self.photograph_writ_page= photograph_writ_page(self.driver)
        self.driver.get(MobileUrl)
        time.sleep(3)
    # 跳转移动端首页-作为上帝视角所有的功能入口是否跳转正常
    def test_Login_mobile_addressTest(self):
        self.photograph_writ_page.log.info('[--首页-记一笔-跳转地址检测开始--]')
        self.ReimbursementIng_result=self.photograph_writ_page.Remember_whit_photo()
        self.assertTrue(self.photograph_writ_page.ReimbursementIng)

    def tearDown(self):
        time.sleep(5)
        pass
if __name__=="__main__":
    unittest.main()

