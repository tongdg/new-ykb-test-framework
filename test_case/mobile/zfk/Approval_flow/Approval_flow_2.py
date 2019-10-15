#普通员工登录-制单（存取唯一数据,后继审批领导根据这个数据去查找）-选择审批领导-提单
#审批领导登录-我的审批-找到普通员工提交的单据-审批通过-结束
import unittest
from selenium import webdriver
from pages.mobile_pages.Approval_flow_page.zfk_Approval_flow_2_page import zfk_Approval_2_page
import time
class Approval_flow_case(unittest.TestCase):
      def setUp(self):
         self.zfk_Approval_2_page = zfk_Approval_2_page(webdriver.Chrome())
         self.zfk_Approval_2_page.Login_Person()
         self.zfk_Approval_2_page.Chionce_Login_staff()  # 登陆企业
         # 这里切换成移动端模式
         options = webdriver.ChromeOptions()
         # 新开浏览器，以Mobile的格式打开
         mobileEmulation = {'deviceName': 'iPhone 6 Plus'}
         options.add_experimental_option('mobileEmulation', mobileEmulation)
         self.driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
         MobileUrl = self.zfk_Approval_2_page.Get_mobile_url()
         # 这里以移动端打开的浏览器实例化的driver,在不继承Basepage的driver时是无法使用Basepage的driver方法
         self.zfk_Approval_2_page = zfk_Approval_2_page(self.driver)
         self.driver.get(MobileUrl)
         time.sleep(15)
      def test_Approval_flow_case(self):
     #     #普通员提单-----------------------------------------------------------------------------------------------------------------------
         self.zfk_Approval_2_page.log.info('[-借款申请单-普通员工选择领导提单开始--]')
         self.zfk_Approvale_result = self.zfk_Approval_2_page.Staff_Borrowing_order()
         self.assertTrue(self.zfk_Approvale_result)
         self.driver.quit()
         self.zfk_Approval_2_page.quit_chrom()

        #审批领导批单-----------------------------------------------------------------------------------------------------------------------
         self.zfk_Approval_2_page = zfk_Approval_2_page(webdriver.Chrome())
         self.zfk_Approval_2_page.Login_Person()
         self.zfk_Approval_2_page.Chionce_Login_leader()#登陆企业
         # 这里切换成移动端模式
         options = webdriver.ChromeOptions()
         # 新开浏览器，以Mobile的格式打开
         mobileEmulation = {'deviceName': 'iPhone 6 Plus'}
         options.add_experimental_option('mobileEmulation', mobileEmulation)
         self.driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
         MobileUrl = self.zfk_Approval_2_page.Get_mobile_url()
         # 这里以移动端打开的浏览器实例化的driver,在不继承Basepage的driver时是无法使用Basepage的driver方法
         self.zfk_Approval_2_page = zfk_Approval_2_page(self.driver)
         self.driver.get(MobileUrl)
         time.sleep(15)
         # 审批领导登录进行审批
         self.zfk_Approval_2_page.log.info('[-借款申请单-审批领导-批单开始-]')
         self.zfk_Approvale_result = self.zfk_Approval_2_page.leader_approvel()
         self.assertTrue(self.zfk_Approvale_result)
         self.driver.quit()
         self.zfk_Approval_2_page.quit_chrom()

         #会计批单-----------------------------------------------------------------------------------------------------------------------
         self.zfk_Approval_2_page = zfk_Approval_2_page(webdriver.Chrome())
         self.zfk_Approval_2_page.Login_Person()
         self.zfk_Approval_2_page.Chionce_Login_accountant()  # 登陆企业
         # 这里切换成移动端模式
         options = webdriver.ChromeOptions()
         # 新开浏览器，以Mobile的格式打开
         mobileEmulation = {'deviceName': 'iPhone 6 Plus'}
         options.add_experimental_option('mobileEmulation', mobileEmulation)
         self.driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
         MobileUrl = self.zfk_Approval_2_page.Get_mobile_url()
         # 这里以移动端打开的浏览器实例化的driver,在不继承Basepage的driver时是无法使用Basepage的driver方法
         self.zfk_Approval_2_page = zfk_Approval_2_page(self.driver)
         self.driver.get(MobileUrl)
         time.sleep(15)
         #会计角色登录进行审批
         self.zfk_Approval_2_page.log.info('[-借款申请单-会计-批单开始-]')
         self.zfk_Approvale_result = self.zfk_Approval_2_page.accountant()
         self.assertTrue(self.zfk_Approvale_result)
         self.driver.quit()
         self.zfk_Approval_2_page.quit_chrom()

         #复核批单-----------------------------------------------------------------------------------------------------------------------
         self.zfk_Approval_2_page = zfk_Approval_2_page(webdriver.Chrome())
         self.zfk_Approval_2_page.Login_Person()
         self.zfk_Approval_2_page.Chionce_Login_manager()  # 登陆企业
         # 这里切换成移动端模式
         options = webdriver.ChromeOptions()
         # 新开浏览器，以Mobile的格式打开
         mobileEmulation = {'deviceName': 'iPhone 6 Plus'}
         options.add_experimental_option('mobileEmulation', mobileEmulation)
         self.driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
         MobileUrl = self.zfk_Approval_2_page.Get_mobile_url()
         # 这里以移动端打开的浏览器实例化的driver,在不继承Basepage的driver时是无法使用Basepage的driver方法
         self.zfk_Approval_2_page = zfk_Approval_2_page(self.driver)
         self.driver.get(MobileUrl)
         time.sleep(15)
         # 会计角色登录进行审批
         self.zfk_Approval_2_page.log.info('[-借款申请单-财务复核-批单开始-]')
         self.zfk_Approvale_result = self.zfk_Approval_2_page.manager_account()
         self.assertTrue(self.zfk_Approvale_result)
         self.driver.quit()
         self.zfk_Approval_2_page.quit_chrom()

         #出纳进行审批
         self.zfk_Approval_2_page = zfk_Approval_2_page(webdriver.Chrome())
         self.zfk_Approval_2_page.Login_Person()
         self.zfk_Approval_2_page.Choince_login_cashier()  # 登陆企业
         time.sleep(5)
         self.zfk_Approval_2_page.cashier()

      def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()

