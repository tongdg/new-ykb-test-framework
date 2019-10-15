#差旅报销单
#普通员工-提单至审批领导-财务初审-财务复审-出纳付款
import unittest
from selenium import webdriver
from pages.mobile_pages.Approval_flow_page.zfk_Approval_flow_4_page import zfk_Approval_4_page
import time
class Approval_flow_case(unittest.TestCase):
     def setUp(self):
         self.zfk_Approval_4_page = zfk_Approval_4_page(webdriver.Chrome())
         self.zfk_Approval_4_page.Login_Person()
         self.zfk_Approval_4_page.Chionce_Login_staff()  # 登陆企业
         # 这里切换成移动端模式
         options = webdriver.ChromeOptions()
         # 新开浏览器，以Mobile的格式打开
         mobileEmulation = {'deviceName': 'iPhone 6 Plus'}
         options.add_experimental_option('mobileEmulation', mobileEmulation)
         self.driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
         MobileUrl = self.zfk_Approval_4_page.Get_mobile_url()
         # 这里以移动端打开的浏览器实例化的driver,在不继承Basepage的driver时是无法使用Basepage的driver方法
         self.zfk_Approval_4_page = zfk_Approval_4_page(self.driver)
         self.driver.get(MobileUrl)
         time.sleep(15)

     def test_Approval_flow_case(self):
        #普通员提单-----------------------------------------------------------------------------------------------------------------------
         self.zfk_Approval_4_page.log.info('[-差旅报销单-普通员工选择领导提单开始--]')
         self.zfk_Approvale_result = self.zfk_Approval_4_page.approval_cost_order()
         assert(True,self.zfk_Approvale_result)
         self.driver.quit()
         self.zfk_Approval_4_page.quit_chrom()

         #审批领导批单-----------------------------------------------------------------------------------------------------------------------
         self.zfk_Approval_4_page = zfk_Approval_4_page(webdriver.Chrome())
         self.zfk_Approval_4_page.Login_Person()
         self.zfk_Approval_4_page.Chionce_Login_leader()#登陆企业
         # 这里切换成移动端模式
         options = webdriver.ChromeOptions()
         # 新开浏览器，以Mobile的格式打开
         mobileEmulation = {'deviceName': 'iPhone 6 Plus'}
         options.add_experimental_option('mobileEmulation', mobileEmulation)
         self.driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
         MobileUrl = self.zfk_Approval_4_page.Get_mobile_url()
         # 这里以移动端打开的浏览器实例化的driver,在不继承Basepage的driver时是无法使用Basepage的driver方法
         self.zfk_Approval_4_page = zfk_Approval_4_page(self.driver)
         self.driver.get(MobileUrl)
         time.sleep(15)
         # 审批领导登录进行审批
         self.zfk_Approval_4_page.log.info('[-差旅报销单-审批领导-批单开始-]')
         self.zfk_Approvale_result = self.zfk_Approval_4_page.cost_leader_approvel()
         self.assertTrue(self.zfk_Approvale_result)
         self.driver.quit()
         self.zfk_Approval_4_page.quit_chrom()

         #会计批单---------------------------------------------- -------------------------------------------------------------------------
         self.zfk_Approval_4_page = zfk_Approval_4_page(webdriver.Chrome())
         self.zfk_Approval_4_page.Login_Person()
         self.zfk_Approval_4_page.Chionce_Login_accountant()  # 登陆企业
         # 这里切换成移动端模式
         options = webdriver.ChromeOptions()
         # 新开浏览器，以Mobile的格式打开
         mobileEmulation = {'deviceName': 'iPhone 6 Plus'}
         options.add_experimental_option('mobileEmulation', mobileEmulation)
         self.driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
         MobileUrl = self.zfk_Approval_4_page.Get_mobile_url()
         # 这里以移动端打开的浏览器实例化的driver,在不继承Basepage的driver时是无法使用Basepage的driver方法
         self.zfk_Approval_4_page = zfk_Approval_4_page(self.driver)
         self.driver.get(MobileUrl)
         time.sleep(15)
         #会计角色登录进行审批
         self.zfk_Approval_4_page.log.info('[-差旅报销单-会计-批单开始-]')
         self.zfk_Approvale_result = self.zfk_Approval_4_page.cost_accountant()
         self.assertTrue(self.zfk_Approvale_result)
         self.driver.quit()
         self.zfk_Approval_4_page.quit_chrom()

         # #复核批单-----------------------------------------------------------------------------------------------------------------------
         self.zfk_Approval_4_page = zfk_Approval_4_page(webdriver.Chrome())
         self.zfk_Approval_4_page.Login_Person()
         self.zfk_Approval_4_page.Chionce_Login_manager()  # 登陆企业
         # 这里切换成移动端模式
         options = webdriver.ChromeOptions()
         # 新开浏览器，以Mobile的格式打开
         mobileEmulation = {'deviceName': 'iPhone 6 Plus'}
         options.add_experimental_option('mobileEmulation', mobileEmulation)
         self.driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
         MobileUrl = self.zfk_Approval_4_page.Get_mobile_url()
         # 这里以移动端打开的浏览器实例化的driver,在不继承Basepage的driver时是无法使用Basepage的driver方法
         self.zfk_Approval_4_page = zfk_Approval_4_page(self.driver)
         self.driver.get(MobileUrl)
         time.sleep(15)
         self.zfk_Approval_4_page.log.info('[-差旅报销单-财务复核-批单开始-]')
         self.zfk_Approvale_result = self.zfk_Approval_4_page.cost_manager_account()
         self.assertTrue(self.zfk_Approvale_result)
         self.driver.quit()
         self.zfk_Approval_4_page.quit_chrom()

         #出纳进行审批
         self.zfk_Approval_4_page = zfk_Approval_4_page(webdriver.Chrome())
         self.zfk_Approval_4_page.Login_Person()
         self.zfk_Approval_4_page.Choince_login_cashier()  # 登陆企业
         time.sleep(5)
         self.zfk_Approval_4_page.cost_cashier()
         self.assertTrue(self.zfk_Approval_4_page)

     def tearDown(self):
      pass
if __name__=="__main__":
    unittest.main()

