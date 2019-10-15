from pages.base_page import BasePage
from pages.mobile_pages.zfk_mobile_index_page import zfk_Mobile_index_page
import time
class zfk_bills_MyBills(zfk_Mobile_index_page):
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
#为了让流程衔接起来: 未报销提过来的差旅报销单，以及费用报销单，需要在我的单据里，进行，撤回 和作废操作
# 顺带隐藏了的完成了,提差旅及费用报销单的撤回提单及作废，回归了差旅及费用报销单的提单操作，
# 下一个步骤走财务审核的步骤 到财务复核再到PC的出纳，两张报销单就算回归完成
#进入我的审批列表
    def Entrance_My_bills(self):
        time.sleep(3)
        self.click(
            self.find_element_by_css_ykb(
                "#guo > div.main.scroller > div > div.ykb_fot > p:nth-child(2)"
            )
        )
        time.sleep(3)
        self.click(
            self.find_element_by_css_ykb(
                "#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-tit > div:nth-child(4)"
            )
        )
#进入审批中,执行撤回操作
    def In_approval_recall(self):
        time.sleep(2)
        self.click(
            self.find_element_by_css_ykb(
                "#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_search > span.form_search_txt")
        )
        time.sleep(3)
        self.click(
            self.find_element_by_css_ykb(
                "#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_status_wrap > p:nth-child(2)")
        )
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
                  self.click(
                      self.find_element_by_css_ykb(
                          "#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div:nth-child(3) > div.guo_scroll_content > div.form_item_ul > div:nth-child(1) > div.form_item_amount > p.form_item_re > span")
                  )
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
        time.sleep(3)
        self.click(self.find_element_by_css_ykb("#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_search > span.form_search_txt"))
        time.sleep(5)
        self.click(self.find_element_by_css_ykb(
            "#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_status_wrap > p:nth-child(1)"))
        time.sleep(3)

#作废单子
    def delete_order(self):
        time.sleep(2)
        #差旅或费用的卡片标识
        CL = self.find_element_by_css_ykb(
            "#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div:nth-child(2) > div.guo_scroll_content > div.form_item_ul > div:nth-child(1) > div.form_item_main > span.form_item_icon.form_item_icon_12",3)
        if CL is not False:
            #判断待提交页面是否有单据
            To_submit_button = self.find_element_by_css_ykb(
                "#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div:nth-child(2) > div.guo_scroll_content > div.form_item_ul > div:nth-child(1)",
                3)
            if To_submit_button is not False:
                #点击作废按钮
                self.click(self.find_element_by_css_ykb(
                "#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div:nth-child(2) > div.guo_scroll_content > div.form_item_ul > div:nth-child(1) > div.form_item_amount > p.form_item_re > span",
                3))
                time.sleep(2)
                #点击作废按钮的确定
                self.click(self.find_element_by_css_ykb(
                    "body > div.mui-popup.mui-popup-in > div.mui-popup-buttons > span.mui-popup-button.mui-popup-button-bold"))
                time.sleep(2)
                print("我的单据-待提交-费用报销单作废成功")
        else:
            # 点击作废按钮
            self.click(self.find_element_by_css_ykb(
                "#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div:nth-child(2) > div.guo_scroll_content > div.form_item_ul > div:nth-child(1) > div.form_item_amount > p.form_item_re > span",
                3))
            time.sleep(2)
            # 点击作废按钮的确定
            self.click(self.find_element_by_css_ykb(
                "body > div.mui-popup.mui-popup-in > div.mui-popup-buttons > span.mui-popup-button.mui-popup-button-bold"))
            time.sleep(2)
            print("我的单据-待提交-差用报销单作废成功")



