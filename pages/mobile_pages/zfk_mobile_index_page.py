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
    @property
    def UnReimbursement(self):
        UnReimbursement_True="static/expenses/anyRecord.html"
        UnReimbursement_url=self.current_url()
        print(UnReimbursement_url)
        if UnReimbursement_True in UnReimbursement_url:
         print("首页“”-未报销页面跳转成功")
        return self.click(self.find_element_by_css_ykb("#guo > div.main.scroller > div > div.ykb_content > div.ykb_main_content > div.ykb_home_wrap > div.ykb_banner > p:nth-child(1)"))
    # 报销中
    @property
    def ReimbursementIng(self):
        return self.click(self.find_element_by_css_ykb("#guo > div.main.scroller > div > div.ykb_content > div.ykb_main_content > div.ykb_home_wrap > div.ykb_banner > p:nth-child(2)"))
    #待还欠款
    @property
    def Stay_still_owed(self):
        return self.click(self.find_element_by_css_ykb("#guo > div.main.scroller > div > div.ykb_content > div.ykb_main_content > div.ykb_home_wrap > div.ykb_banner > p:nth-child(3)"))
    #记一笔
    def Remember_whit(self):
        return self.click(
            self.find_element_by_css_ykb(
                "#guo > div.main.scroller > div > div.ykb_content > div.ykb_main_content > div.ykb_main > p:nth-child(1)"
            )
        )
    def Remember_whit_back(self):
        return self.click(self.find_element_by_css_ykb("#backNative > span"))
    #我要制单
    def Make_order(self):
        return self.click(self.find_element_by_css_ykb("#guo > div.main.scroller > div > div.ykb_content > div.ykb_main_content > div.ykb_main > p:nth-child(2)"))

    def Make_order_back(self):
        return self.click(self.find_element_by_css_ykb("#header > em"))
    #智能报表
    def Statement(self):
        return self.click(self.find_element_by_css_ykb("#guo > div.main.scroller > div > div.ykb_content > div.ykb_main_content > div.ykb_main > p:nth-child(3)"))
    def Statement_back(self):
        return self.click(self.find_element_by_css_ykb("#header > em"))
    #商旅预定
    def Travel_booking(self):
        return self.click(self.find_element_by_css_ykb("#guo > div.main.scroller > div > div.ykb_content > div.ykb_main_content > div.ykb_main > p:nth-child(4)"))
    def Travel_booling_back(self):
        return self.click(self.find_element_by_css_ykb("#header > em"))
    #商城采购
    def Store_Purchase(self):
        return self.click(self.find_element_by_css_ykb("#guo > div.main.scroller > div > div.ykb_content > div.ykb_main_content > div.ykb_main > p:nth-child(5)"))
    def Store_Purchase_back(self):
        return self.back()
    #出行用车
    def Travel_car(self):
        return self.click(self.find_element_by_css_ykb("#guo > div.main.scroller > div > div.ykb_content > div.ykb_main_content > div.ykb_main > p:nth-child(6)"))
    def Travel_car_back(self):
        self.back()
    #未报销返回
    @property
    def UnReimbursement_back(self):
        return self.click(self.find_element_by_css_ykb("#app > div > div.mui-navbar > div > button > span"))
    #报销中,代换借款的返回
    @property
    def ReimbursementIng_back(self):
        return self.click(self.find_element_by_id_ykb("spBack"))