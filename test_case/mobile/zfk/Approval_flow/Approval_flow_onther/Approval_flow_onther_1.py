#财务环节的加审业务环节
import sys
import unittest
from selenium import webdriver
import time

from pages.mobile_pages.Approval_flow_page.zfk_Approval_flow_onther_page import zfk_Approval_flow_onther_page


class Approval_flow_case(unittest.TestCase):
     def setUp(self):
         self.zfk_Approval_flow_onther_page = zfk_Approval_flow_onther_page(webdriver.Chrome())
         self.zfk_Approval_flow_onther_page.Login_Person()
         self.zfk_Approval_flow_onther_page.Choince_Login_god()  # 登陆企业
         # 这里切换成移动端模式
         options = webdriver.ChromeOptions()
         # 新开浏览器，以Mobile的格式打开
         mobileEmulation = {'deviceName': 'iPhone 6 Plus'}
         options.add_experimental_option('mobileEmulation', mobileEmulation)
         self.driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
         MobileUrl = self.zfk_Approval_flow_onther_page.Get_mobile_url()
         # 这里以移动端打开的浏览器实例化的driver,在不继承Basepage的driver时是无法使用Basepage的driver方法
         self.zfk_Approval_flow_onther_page = zfk_Approval_flow_onther_page(self.driver)
         self.driver.get(MobileUrl)
         time.sleep(15)
     def test_Approval_flow_case(self):
        #借款单财务初审环节加审业务环节-----------------------------------------------------------------------------------------------------------------------
         self.zfk_Approval_flow_onther_page.log.info('[-财务初审环节-加审-业务环节-开始]')
         self.zfk_Approvale_result = self.zfk_Approval_flow_onther_page.To_Approvel_borrow()
         self.zfk_Approvale_result=self.zfk_Approval_flow_onther_page.add_Approvel_borrow()
         self.zfk_Approvale_result=self.zfk_Approval_flow_onther_page.submit_borrow_approver()
         assert(True,self.zfk_Approvale_result)
         self.driver.quit()
         self.zfk_Approval_flow_onther_page.quit_chrom()

     def tearDown(self):
      sys.exit()
if __name__=="__main__":
    unittest.main()

