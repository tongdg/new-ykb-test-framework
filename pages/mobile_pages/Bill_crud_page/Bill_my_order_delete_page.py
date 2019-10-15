from pages.base_page import BasePage
from pages.mobile_pages.zfk_mobile_index_page import zfk_Mobile_index_page
import time
class Bill_my_order_page(zfk_Mobile_index_page):
#单据-我的审批内需定位的元素
#单据       Index_receipts
#我的单据   My_bills
#待提交     To_submit
#审批中     In_approval
#已完成     Completed
#搜索框     Search_box
#筛选{      Screen
#报销费用    Screen_cost
#差旅报销    Screen_travel
#重置       Screen_reset
#确定       Screen_confirm
# }
    #进入我的单据列表
    def Entrance_My_bills(self):
        time.sleep(3)
        self.click(
            self.find_element_by_css_ykb(
                "#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-tit > div:nth-child(3)"
            )
        )
        time.sleep(3)
        self.click(self.find_element_by_css_ykb("#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-tit > div:nth-child(4)"))

    #进入审批中,执行撤回操作
    def In_approval_recall(self):
        time.sleep(2)
        self.click(self.find_element_by_css_ykb("#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_search > span.form_search_txt"))
        time.sleep(3)
        self.click(self.find_element_by_css_ykb("#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_status_wrap > p:nth-child(2)"))
        time.sleep(3)

    #外部撤回差旅报销和费用报销单
    def recall_order(self):
        In_recall_button = self.find_element_by_css_ykb(
            "#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div:nth-child(3) > div.guo_scroll_content > div.form_item_ul > div:nth-child(1)",
            1.5)
        if In_recall_button is not False:
            CL = self.find_element_by_css_ykb("#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div:nth-child(3) > div.guo_scroll_content > div.form_item_ul > div:nth-child(1) > div.form_item_main > span.form_item_icon.form_item_icon_11",3)
            if CL is not False:
                  time.sleep(3)
                  self.click(self.find_element_by_css_ykb("#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div:nth-child(3) > div.guo_scroll_content > div.form_item_ul > div:nth-child(1) > div.form_item_amount > p.form_item_re > span"))
                  time.sleep(4)
                  self.click(self.find_element_by_css_ykb(
                         "body > div.mui-popup.mui-popup-in > div.mui-popup-buttons > span.mui-popup-button.mui-popup-button-bold"))
                  print("我的单据-审批中-差旅报销单外部撤回成功")
            else:
                self.click(self.find_element_by_css_ykb("#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div:nth-child(3) > div.guo_scroll_content > div.form_item_ul > div:nth-child(1) > div.form_item_amount > p.form_item_re > span"))
                time.sleep(4)
                self.click(self.find_element_by_css_ykb(
                         "body > div.mui-popup.mui-popup-in > div.mui-popup-buttons > span.mui-popup-button.mui-popup-button-bold"))
        else:
            print("我的单据-审批中-不存在可进行外部可以撤回的差旅或费用报销单")

    #内部撤回差旅和费用报销单
    def In_recall_order(self):
        time.sleep(2)
        In_recall_button=self.find_element_by_css_ykb("#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div:nth-child(3) > div.guo_scroll_content > div.form_item_ul > div:nth-child(1)",1.5)
        if In_recall_button is not False:
            self.click(In_recall_button)
            time.sleep(2)
            cl = self.find_element_by_css_ykb('#app > div > div.mui-navbar > div > h1')
            print(cl.text)
            if cl.text=="差旅报销单":
                time.sleep(2)
                self.click(
                self.find_element_by_css_ykb("#traForm > div > div.mui-bar.mui-bar-tab.ab.hasBLine > button"))
                print("我的单据-审批中-差旅报销单内部撤回成功")
                time.sleep(2)
            else:
                time.sleep(2)
                self.click(self.find_element_by_css_ykb("#reiForm > div > div.mui-bar.mui-bar-tab.ab.hasBLine > button"))
                print("我的单据-审批中-费用报销单内部撤回成功")
                time.sleep(3)
        else:
            print("我的单据-审批中-不存在可进行内部撤回的差旅或费用报销单")

    #进入待提交，执行作废操作
    def To_submit(self):
        #点单据
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div.ykb_fot > p:nth-child(2)'
            )
        )
        time.sleep(4)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-tit > div:nth-child(2)'
            )
        )
        time.sleep(3)
        self.click(
            self.find_element_by_css_ykb(
                "#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_search > span.form_search_txt"
            )
        )
        time.sleep(5)
        self.click(
            self.find_element_by_css_ykb(
            "#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_status_wrap > p:nth-child(1)"
            )
        )
        time.sleep(3)

    #作废单子-借款申请单
    def delete_order_borrow(self):
        self.click(
            self.find_element_by_css_ykb(
            '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_search > span.form_search_alt'
            )
        )
        time.sleep(2)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_alt_wrap > div.form_alt > span:nth-child(4)'
            )
        )
        time.sleep(1)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_alt_wrap > div.form_alt_fot > button.button.button-success'
            )
        )
        time.sleep(1)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div:nth-child(2) > div.guo_scroll_content > div.form_item_ul > div:nth-child(1) > div.form_item_amount > p.form_item_re > span'
            )
        )
        time.sleep(1)
        self.click(
            self.find_element_by_css_ykb(
                'body > div.mui-popup.mui-popup-in > div.mui-popup-buttons > span.mui-popup-button.mui-popup-button-bold'
            )
        )
        time.sleep(5)

    #作废单子-出差申请单
    def delete_order_evection(self):
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_search > span.form_search_alt'
            )
        )
        time.sleep(2)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_alt_wrap > div.form_alt > span:nth-child(5)'
            )
        )
        time.sleep(1)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_alt_wrap > div.form_alt_fot > button.button.button-success'
            )
        )
        time.sleep(1)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div:nth-child(2) > div.guo_scroll_content > div.form_item_ul > div:nth-child(1) > div.form_item_amount > p.form_item_re > span'
            )
        )
        time.sleep(1)
        self.click(
            self.find_element_by_css_ykb(
                'body > div.mui-popup.mui-popup-in > div.mui-popup-buttons > span.mui-popup-button.mui-popup-button-bold'
            )
        )
        time.sleep(5)

    #作废单子-费用报销单
    def delete_order_cost(self):
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_search > span.form_search_alt'
            )
        )
        time.sleep(2)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_alt_wrap > div.form_alt > span:nth-child(2)'
            )
        )
        time.sleep(1)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_alt_wrap > div.form_alt_fot > button.button.button-success'
            )
        )
        time.sleep(1)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div:nth-child(2) > div.guo_scroll_content > div.form_item_ul > div:nth-child(1) > div.form_item_amount > p.form_item_re > span'
            )
        )
        time.sleep(2)
        self.click(
            self.find_element_by_css_ykb(
                'body > div.mui-popup.mui-popup-in > div.mui-popup-buttons > span.mui-popup-button.mui-popup-button-bold'
            )
        )
        time.sleep(5)

    # 作废单子-费用报销单
    def delete_order_travel(self):
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_search > span.form_search_alt'
            )
        )
        time.sleep(2)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_alt_wrap > div.form_alt > span:nth-child(3)'
            )
        )
        time.sleep(1)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_alt_wrap > div.form_alt_fot > button.button.button-success'
            )
        )
        time.sleep(1)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div:nth-child(2) > div.guo_scroll_content > div.form_item_ul > div:nth-child(1) > div.form_item_amount > p.form_item_re > span'
            )
        )
        time.sleep(2)
        self.click(
            self.find_element_by_css_ykb(
                'body > div.mui-popup.mui-popup-in > div.mui-popup-buttons > span.mui-popup-button.mui-popup-button-bold'
            )
        )
        time.sleep(5)




