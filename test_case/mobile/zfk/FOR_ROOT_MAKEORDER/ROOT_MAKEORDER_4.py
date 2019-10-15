import unittest
from selenium import webdriver
import time

from pages.mobile_pages.FOR_ROOT_MAKEORDER_PAGE.MAKEORDE_PAGE import MAKEORDER_PAGE
from pages.mobile_pages.zfk_mobile_index_page import zfk_Mobile_index_page
class zfk_mobile_makeorder_case(unittest.TestCase):
    def setUp(self):
        # self.MAKEORDER_PAGE = zfk_Mobile_index_page(webdriver.Chrome())
        # self.MAKEORDER_PAGE.Login_Person()  # 登录账号
        # self.MAKEORDER_PAGE.Choince_Login_god()#登陆企业
        # options = webdriver.ChromeOptions()
        # #新开浏览器，以Mobile的格式打开
        # mobileEmulation = {'deviceName': 'iPhone 6 Plus'}
        # options.add_experimental_option('mobileEmulation', mobileEmulation)
        # self.driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
        # MobileUrl = self.MAKEORDER_PAGE.Get_mobile_url()
        # #这里以移动端打开的浏览器实例化的driver,在不继承Basepage的driver时是无法使用Basepage的driver方法
        # self.MAKEORDER_PAGE= MAKEORDER_PAGE(self.driver)
        # self.driver.get(MobileUrl)
        # time.sleep(3)
        pass
    def test_makeorder_case(self):
        # for i in  range(0,50):
        #     self.MAKEORDER_PAGE.log.info('[--循环制-费用报销单--]')
        #     self.Make_Evection_order_plan_result = self.MAKEORDER_PAGE.cost_order()
        pass
    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()

