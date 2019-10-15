import os
import time

from pages.mobile_pages.zfk_mobile_index_page import zfk_Mobile_index_page

class photograph_writ_page(zfk_Mobile_index_page):

    #点击拍票识别
    def take_phot(self):
        self.click(
            self.find_element_by_id_ykb('cphone')
        )
        time.sleep(3)
    #判断发票是否导入至消费记录内
    def  examine_bill(self):
        bill_css=self.find_element_by_class_name_ykb('invoice-list-card')
        time.sleep(2)
        if bill_css is not False:
            print('发票接口调取成功~')
    # 记一笔
    def Remember_whit_photo(self):
        time.sleep(3)
        # 进入记一笔
        self.click(
            self.find_element_by_css_ykb(
                "#guo > div.main.scroller > div > div.ykb_content > div.ykb_main_content > div.ykb_main > p:nth-child(1)"
            )
        )
        # 正确记一笔的URL地址
        Remember_whit_True = "static/expenses/anyRecord.html"
        # 获取当前跳转页面的URL
        Remember_whit_url = self.current_url()
        if Remember_whit_True in Remember_whit_url:
            time.sleep(2)
            self.log.info("首页“”-记一笔-跳转成功")
            time.sleep(2)
            self.take_phot()
            os.system('C:\\Users\\Administrator.USER-20180320AW\Desktop\\anthor.exe')
            time.sleep(5)
            self.examine_bill()

            return True
        else:
            time.sleep(2)
            self.log.info("首页-记一笔-地址错误")
            return False
