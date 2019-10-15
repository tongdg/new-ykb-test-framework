#普通员工登录-制单（存取唯一数据,后继审批领导根据这个数据去查找）-选择审批领导-提单
#审批领导登录-我的审批-找到普通员工提交的单据-审批通过-结束
import unittest
from selenium import webdriver
from pages.mobile_pages.Approval_flow_page.zfk_Approval_flow_1_page import zfk_Approval_1_page

import time
class Approval_flow_case(unittest.TestCase):
     def setUp(self):
         self.zfk_Approval_1_page = zfk_Approval_1_page(webdriver.Chrome())
         self.zfk_Approval_1_page.Login_Person()
         self.zfk_Approval_1_page.Chionce_Login_staff()  # 登陆企业
         # 这里切换成移动端模式
         options = webdriver.ChromeOptions()
         # 新开浏览器，以Mobile的格式打开
         mobileEmulation = {'deviceName': 'iPhone 6 Plus'}
         options.add_experimental_option('mobileEmulation', mobileEmulation)
         self.driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
         MobileUrl = self.zfk_Approval_1_page.Get_mobile_url()
         # 这里以移动端打开的浏览器实例化的driver,在不继承Basepage的driver时是无法使用Basepage的driver方法
         self.zfk_Approval_1_page = zfk_Approval_1_page(self.driver)
         self.driver.get(MobileUrl)
         time.sleep(3)
     def test_Approval_flow_case(self):
        # #普通员提单机票至审批领导
         self.zfk_Approval_1_page.log.info('[--普通员工选择领导提单开始--]')
         self.zfk_Approvale_result = self.zfk_Approval_1_page.Make_Evection_order_plan()
         self.assertTrue(self.zfk_Approvale_result)
         self.driver.quit()
         self.zfk_Approval_1_page.quit_chrom()
        #审批领导批单
         self.zfk_Approval_1_page = zfk_Approval_1_page(webdriver.Chrome())
         self.zfk_Approval_1_page.Login_Person()
         self.zfk_Approval_1_page.Chionce_Login_leader()#登陆企业
         # 这里切换成移动端模式
         options = webdriver.ChromeOptions()
         # 新开浏览器，以Mobile的格式打开
         mobileEmulation = {'deviceName': 'iPhone 6 Plus'}
         options.add_experimental_option('mobileEmulation', mobileEmulation)
         self.driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
         MobileUrl = self.zfk_Approval_1_page.Get_mobile_url()
         # 这里以移动端打开的浏览器实例化的driver,在不继承Basepage的driver时是无法使用Basepage的driver方法
         self.zfk_Approval_1_page = zfk_Approval_1_page(self.driver)
         self.driver.get(MobileUrl)
         # 审批领导登录进行审批
         self.zfk_Approval_1_page.log.info('[--普通员工选择领导提单开始--]')
         self.zfk_Approvale_result = self.zfk_Approval_1_page.leader_approvel()
         self.assertTrue(self.zfk_Approvale_result)

     def tearDown(self):
      pass
if __name__=="__main__":
    unittest.main()

