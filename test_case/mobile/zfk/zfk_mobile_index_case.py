#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'2019-05-29 Created by Zhangfukai'
import unittest
from selenium import webdriver
import time

from pages.mobile_pages.zfk_UnReimbursement_page.zfk_create_Unreimbursement import zfk_create_Unreimbursement
from pages.mobile_pages.zfk_bills_page.zfk_bills_MyBills import zfk_bills_MyBills
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
        self.zfk_mobile_index_Page= zfk_Mobile_index_page(self.driver)
        self.zfk_create_Unreimbursement = zfk_create_Unreimbursement(self.driver)
        self.driver.get(MobileUrl)
        time.sleep(3)

    # 跳转移动端首页-作为上帝视角所有的功能入口是否跳转正常
    def test_Login_mobile_addressTest(self):
        self.zfk_mobile_index_Page.log.info('[--首页-未报销-跳转地址检测开始--]')
        self.UnReimbursement_result = self.zfk_mobile_index_Page.UnReimbursement()
        self.assertTrue(self.zfk_mobile_index_Page.UnReimbursement)
        self.zfk_mobile_index_Page.back()

        self.zfk_mobile_index_Page.log.info('[--首页-报销中-跳转地址检测开始--]')
        self.ReimbursementIng_result=self.zfk_mobile_index_Page.ReimbursementIng()
        self.assertTrue(self.zfk_mobile_index_Page.ReimbursementIng)
        self.zfk_mobile_index_Page.back()

        self.zfk_mobile_index_Page.log.info('[--首页-待还欠款-跳转地址检测开始--]')
        self.Stay_still_owed_result = self.zfk_mobile_index_Page.Stay_still_owed()
        self.assertTrue(self.zfk_mobile_index_Page.Stay_still_owed)
        self.zfk_mobile_index_Page.back()

        self.zfk_mobile_index_Page.log.info('[--首页-记一笔-跳转地址检测开始--]')
        self.Remember_whit_result=self.zfk_mobile_index_Page.Remember_whit()
        self.assertTrue(self.zfk_mobile_index_Page.Remember_whit)
        self.zfk_mobile_index_Page.back()

        self.zfk_mobile_index_Page.log.info('[--首页-我要制单-跳转地址检测开始--]')
        self.Make_order_result = self.zfk_mobile_index_Page.Make_order()
        self.assertTrue(self.zfk_mobile_index_Page.Make_order)
        self.zfk_mobile_index_Page.back()

        self.zfk_mobile_index_Page.log.info('[--首页-智能报表-跳转地址检测开始--]')
        self.Statement_result = self.zfk_mobile_index_Page.Statement()
        self.assertTrue(self.zfk_mobile_index_Page.Statement)
        self.zfk_mobile_index_Page.back()

        self.zfk_mobile_index_Page.log.info('[--首页-商旅预定-跳转地址检测开始--]')
        self.Travel_booking_result = self.zfk_mobile_index_Page.Travel_booking()
        self.assertTrue(self.zfk_mobile_index_Page.Travel_booking)

        self.zfk_mobile_index_Page.log.info('[--首页-商场采购-跳转地址检测开始--]')
        self.Store_Purchase_result = self.zfk_mobile_index_Page.Store_Purchase()
        self.assertTrue(self.zfk_mobile_index_Page.Store_Purchase)
        self.zfk_mobile_index_Page.back()
        self.zfk_mobile_index_Page.log.info('[--首页-出行用车-跳转地址检测开始--]')
        self.Travel_car_result = self.zfk_mobile_index_Page.Travel_car()
        self.assertTrue(self.zfk_mobile_index_Page.Travel_car)
        self.zfk_mobile_index_Page.back()

    def test_Login_mobile_UnReimbursement(self):
        time.sleep(2)
        self.zfk_mobile_index_Page.log.info('[--首页-未报销测试用例开始--]')

        # self.zfk_create_Unreimbursement.ReimbursementIng()
        # # time.sleep(2)
        # # 记一笔包含全选删除和单笔删除
        # self.zfk_create_Unreimbursement.UnReim_Remember_whit_Delete()
        # # 记一笔包含全选提交和单笔提交
        # self.zfk_create_Unreimbursement.UnReim_Remember_whit_Submit_Travel()
        # # 全选提交和单笔提交至费用报销单
        # self.zfk_create_Unreimbursement.UnReim_Remember_whit_Submit_Cost()
        # # 页面回退到主页
        # self.zfk_create_Unreimbursement.write_back()
        # # 进入我的订单
        # self.zfk_bills_MyBills.Entrance_My_bills()
        # # 进入审批中
        # self.zfk_bills_MyBills.In_approval_recall()
        # # 撤回报销单-审批中
        # for i in range(1, 5):
        #     if i % 2 == 0:
        #         self.zfk_bills_MyBills.In_recall_order()
        #     else:
        #         self.zfk_bills_MyBills.recall_order()
        # # 进入待提交执行作废
        # time.sleep(2)
        # self.zfk_bills_MyBills.To_submit()
        # time.sleep(2)
        # for j in range(1, 5):
        #     self.zfk_bills_MyBills.delete_order()

    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()

