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
        self.zfk_bills_MyBills = zfk_bills_MyBills(self.driver)
    def test_Login_mobile_enterprise(self):
         time.sleep(5)
         self.zfk_create_Unreimbursement.UnReimbursement
         time.sleep(2)
         #记一笔包含全选删除和单笔删除
         self.zfk_create_Unreimbursement.UnReim_Remember_whit_Delete()
         # 记一笔包含全选提交和单笔提交
         self.zfk_create_Unreimbursement.UnReim_Remember_whit_Submit_Travel()
         #全选提交和单笔提交至费用报销单
         self.zfk_create_Unreimbursement.UnReim_Remember_whit_Submit_Cost()
         #页面回退到主页
         self.zfk_create_Unreimbursement.write_back()
         #进入我的订单
         self.zfk_bills_MyBills.Entrance_My_bills()
         #进入审批中
         self.zfk_bills_MyBills.In_approval_recall()
         #撤回报销单-审批中
         for i in range(1, 5):
             if i % 2 == 0:
                 self.zfk_bills_MyBills.In_recall_order()
             else:
                 self.zfk_bills_MyBills.recall_order()
         #进入待提交执行作废
         time.sleep(2)
         self.zfk_bills_MyBills.To_submit()
         time.sleep(2)
         for j in range(1, 5):
             self.zfk_bills_MyBills.delete_order()
    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()

