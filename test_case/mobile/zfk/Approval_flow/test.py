from selenium import webdriver
import unittest, time


def highLightElement(driver, element):
    # 封装好的高亮显示页面元素的方法
    # 使用JavaScript代码将传入的页面元素对象的背景颜色和边框颜色分别
    # 设置为绿色和红色
    # driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",
    #                       element,"border:2px solid red;")
    # time.sleep(2)
    # driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",
    #                       element, "border:0px solid  ;")
    pass
class TeseDemo(unittest.TestCase):
    # def setUp(self):
    #     self.driver = webdriver.Chrome()
    # def test_highLightWebElement(self):
    #     url = "http://106.75.114.250/"
    #     # 访问百度首页
    #     self.driver.get(url)
    #     searchBox = self.driver.find_element_by_id('loginname')
    #     # 调用高亮显示的元素封装函数
    #     highLightElement(self.driver, searchBox)
    #     # 等待3秒，以便 查看高亮效果
    #     time.sleep(3)
    #     searchBox.send_keys(u"光荣之路自动化测试")
    #     sumbitButton = self.driver.find_element_by_id("stb")
    #     # 调用高亮显示的封装函数，将搜索按钮进行高亮显示
    #     highLightElement(self.driver, sumbitButton)
    #     time.sleep(3)
    #     sumbitButton.click()
    #     time.sleep(3)
    def tearDown(self):
        # 退出浏览器
        # self.driver.quit()
        pass

if __name__ == '__main()__':
    unittest.TestCase()
