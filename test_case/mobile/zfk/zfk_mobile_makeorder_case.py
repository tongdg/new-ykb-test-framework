import unittest
from selenium import webdriver
import time

from pages.mobile_pages.zfk_makeOrder_page import zfk_makeOrder_page
from pages.mobile_pages.zfk_mobile_index_page import zfk_Mobile_index_page
class zfk_mobile_makeorder_case(unittest.TestCase):
    def setUp(self):
        self.zfk_makeOrder_page = zfk_Mobile_index_page(webdriver.Chrome())
        self.zfk_makeOrder_page.Login_Person()  # 登录账号
        self.zfk_makeOrder_page.Chionce_Login_role()#登陆企业
        options = webdriver.ChromeOptions()
        #新开浏览器，以Mobile的格式打开
        mobileEmulation = {'deviceName': 'iPhone 6 Plus'}
        options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
        MobileUrl = self.zfk_makeOrder_page.Get_mobile_url()
        #这里以移动端打开的浏览器实例化的driver,在不继承Basepage的driver时是无法使用Basepage的driver方法
        self.zfk_makeOrder_page= zfk_makeOrder_page(self.driver)
        self.driver.get(MobileUrl)
        time.sleep(3)
    def test_makeorder_case(self):
        self.zfk_makeOrder_page.Make_Evection_order_hotel()
    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()
# //*[@id="ticketList"]/li[1]/div/div[2]/div[4]/div/div[2]
# #ticketList > li:nth-child(1) > div > div.f8f8 > div:nth-child(4) > div > div.abtn.bookticket
# //*[@id="ticketList"]/li[2]/div/div[2]/div[1]/div/div[2]

