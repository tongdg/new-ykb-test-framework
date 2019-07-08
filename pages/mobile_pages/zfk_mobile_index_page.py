import sys
import time
import self as self
from pages.mobile_pages.zfk_mobile_login_Page import Mobile_login_page
class zfk_Mobile_index_page(Mobile_login_page):
    #首页需定位的元素
    #未报销   UnReimbursement
    #报销中   ReimbursementIng
    #待还欠款  Stay_still_owed
    #记一笔    Remember_whit
    #我要制单   Make_order
    #智能报表   Statement
    #商旅预定   Travel_booking
    #商城采购   Store_Purchase
    #出发用车   Travel_car
    #单据      Index_receipts
    #订单      Idex_indent
    #更多      Index_more
    #返回      Index_back

    #未报销
    def UnReimbursement(self):
        time.sleep(3)
        #进入未报销页面
        self.click(
                self.find_element_by_css_ykb(
                    "#guo > div.main.scroller > div > div.ykb_content > div.ykb_main_content > div.ykb_home_wrap > div.ykb_banner > p:nth-child(1)"
                )
            )
        #正确未报销的URL地址
        UnReimbursement_True="static/expenses/anyRecord.html"
        #获取当前跳转页面的URL
        UnReimbursement_url=self.current_url()
        if UnReimbursement_True in UnReimbursement_url:
            time.sleep(2)
            self.log.info("首页“”-未报销页面跳转成功")
            time.sleep(2)
            return True
        else:
            time.sleep(2)
            self.log.info("首页-未报销-地址错误")
            return False
    # 报销中
    def ReimbursementIng(self):
        time.sleep(3)
        # 进入未报销页面
        self.click(
            self.find_element_by_css_ykb(
                "#guo > div.main.scroller > div > div.ykb_content > div.ykb_main_content > div.ykb_home_wrap > div.ykb_banner > p:nth-child(2)"
            )
        )
        # 正确报销中的URL地址
        ReimbursementIng_True = "BusinessTask/HistoryTask"
        # 获取当前跳转页面的URL
        ReimbursementIng_url = self.current_url()
        if ReimbursementIng_True in ReimbursementIng_url:
            time.sleep(2)
            self.log.info("首页“”-报销中页面跳转成功")
            time.sleep(2)
            return True
        else:
            time.sleep(2)
            self.log.info("首页-报销中-地址错误")
            return False
    #待还借款
    def Stay_still_owed(self):
        time.sleep(3)
        # 进入待还欠款
        self.click(
            self.find_element_by_css_ykb(
                "#guo > div.main.scroller > div > div.ykb_content > div.ykb_main_content > div.ykb_home_wrap > div.ykb_banner > p:nth-child(3)"
            )
        )
        # 正确报销中的URL地址
        Stay_still_owed_True ="BusinessTask/WaitingReturnArrears"
        # 获取当前跳转页面的URL
        Stay_still_owed_url = self.current_url()
        if Stay_still_owed_True in Stay_still_owed_url:
            time.sleep(2)
            self.log.info("首页“”-待还欠款-跳转成功")
            time.sleep(2)
            return True
        else:
            time.sleep(2)
            self.log.info("首页-待还欠款-地址错误")
            return False

    #记一笔
    def Remember_whit(self):
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
            return True
        else:
            time.sleep(2)
            self.log.info("首页-记一笔-地址错误")
            return False

    #我要制单
    def Make_order(self):
        time.sleep(3)
        # 进入我要制单
        self.click(
            self.find_element_by_css_ykb(
                "#guo > div.main.scroller > div > div.ykb_content > div.ykb_main_content > div.ykb_main > p:nth-child(2)"
            )
        )
        MakeOrderText=self.find_element_by_css_ykb("#header > div")
        self.log.info(MakeOrderText.text)
        if MakeOrderText.text=="我要制单":
            time.sleep(2)
            self.log.info("首页-我要制单-跳转成功")
            return True
        else:
            time.sleep(2)
            self.log.info("首页-我要制单-跳转失败")
            return False
    #智能报表
    def Statement(self):
        time.sleep(3)
        # 进入记一笔
        self.click(
            self.find_element_by_css_ykb(
                "#guo > div.main.scroller > div > div.ykb_content > div.ykb_main_content > div.ykb_main > p:nth-child(3)"
            )
        )
        StatementrText=self.find_element_by_css_ykb("#header > div")
        print('智能报表title'+StatementrText.text)
        if StatementrText.text=="智能报表":
            time.sleep(2)
            self.log.info("首页-智能报表-跳转成功")
            return True
        else:
            time.sleep(2)
            self.log.info("首页-我要制单-跳转失败")
            return False
    #商旅预定
    #这里包含机酒火的页面跳转
    def Travel_booking(self):
        time.sleep(3)
        # 进入商旅预定
        self.click(
            self.find_element_by_css_ykb(
                "#guo > div.main.scroller > div > div.ykb_content > div.ykb_main_content > div.ykb_main > p:nth-child(4)"
            )
        )
        StatementrText = self.find_element_by_css_ykb("#header > div")
        print('商旅预定title'+StatementrText.text)
        if StatementrText.text == "商旅预订":
            time.sleep(2)
            self.log.info("首页-商旅预定-跳转成功---开始进入二级页面---机票")
            time.sleep(2)
            #进入机票预订界面
            self.click(self.find_element_by_css_ykb("#guo > div.main.scroller.main1 > div > div:nth-child(1)"))
            Plan_url=self.current_url()
            Plan_true_url="http://test.new.flight.mobile.51ykb.com"
            if Plan_true_url in Plan_url:
                self.log.info("首页-商旅预定-机票-跳转成功")
                time.sleep(2)
                self.back()
                time.sleep(3)
            else:
                self.log.info("首页-商旅预定-机票-跳转失败")
                self.back()
            #进入酒店预订界面
            time.sleep(2)
            self.log.info("首页-商旅预定-跳转成功---开始进入二级页面--酒店")
            self.click(self.find_element_by_css_ykb("#guo > div.main.scroller.main1 > div > div:nth-child(2)"))
            time.sleep(3)
            Hotel_true_url="http://test.v2.hotel.mobile.51ykb.com"
            Hotel_url=self.current_url()
            if Hotel_true_url in Hotel_url:
                self.log.info("首页-商旅预定-酒店-跳转成功")
                time.sleep(2)
                self.back()
            else:
                self.log.info("首页-商旅预定-酒店-跳转失败")
                self.back()
            #进入火车预定界面
            time.sleep(2)
            self.log.info("首页-商旅预定-跳转成功---开始进入二级页面--火车")
            self.click(self.find_element_by_css_ykb("#guo > div.main.scroller.main1 > div > div:nth-child(3)"))
            Train_true_url="http://test.train.mobile.51ykb.com"
            Train_url=self.current_url()
            if Train_true_url in Train_url :
                self.log.info("首页-商旅预定-火车-跳转成功")
                time.sleep(2)
                self.back()
                time.sleep(2)
                self.click(self.find_element_by_css_ykb("#header > em"))
            else:
                self.log.info("首页-商旅预定-火车-跳转失败")
                time.sleep(2)
                self.back()
            return True
        else:
            time.sleep(2)
            self.log.info("首页-商旅预定-跳转失败")
            return False
    #商城采购
    def Store_Purchase(self):
        time.sleep(3)
        # 进入记一笔
        self.click(
            self.find_element_by_css_ykb(
                "#guo > div.main.scroller > div > div.ykb_content > div.ykb_main_content > div.ykb_main > p:nth-child(5)"
            )
        )
        # 正确的商城URL地址
        Store_Purchase_True = "http://showfenku.shop.51ykb.com/mobile/index.php"
        # 获取当前跳转页面的URL
        time.sleep(3)
        Store_Purchase_url = self.current_url()
        if Store_Purchase_True in Store_Purchase_url:
            time.sleep(2)
            self.log.info("首页“”-商城采购-跳转成功")
            time.sleep(2)
            return True
        else:
            time.sleep(2)
            self.log.info("首页“”-商城采购-跳转失败")
            return False

    #功能入口待删除
    #出行用车
    def Travel_car(self):
        time.sleep(3)
        # 进入记一笔
        self.click(
            self.find_element_by_css_ykb(
                "#guo > div.main.scroller > div > div.ykb_content > div.ykb_main_content > div.ykb_main > p:nth-child(6)"
            )
        )
        # 正确的出行用车地址
        Travel_car_True = "https://open.es.xiaojukeji.com/webapp/feESWebappLogin/index#?hash_passport_login"
        # 获取当前跳转页面的URL
        time.sleep(3)
        Travel_car_url = self.current_url()
        if Travel_car_True in Travel_car_url:
            time.sleep(2)
            self.log.info("首页“”-出行用车-跳转成功")
            time.sleep(2)
            return True
        else:
            time.sleep(2)
            self.log.info("首页“”-出行用车-跳转失败")
            return False
































