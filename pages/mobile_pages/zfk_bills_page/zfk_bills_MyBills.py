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
        self.click(self.find_element_by_css_ykb("#guo > div.main.scroller > div > div.ykb_fot > p:nth-child(2)"))
        time.sleep(1)
        self.click(self.find_element_by_css_ykb("#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-tit > div:nth-child(4)"))
#进入审批中,执行撤回操作
    def In_approval_recall(self):
        time.sleep(3)
        self.click(self.find_element_by_css_ykb("#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_search > span.form_search_txt"))
        time.sleep(10)
        self.click(self.find_element_by_css_ykb("#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_status_wrap > p:nth-child(2)"))
        time.sleep(5)
#循环作废单据
    for i in range(0,10):
        def cycly_delete(self):
            self.click(self.find_element_by_css_ykb("#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div:nth-child(3) > div.guo_scroll_content > div.form_item_ul > div:nth-child(5) > div.form_item_amount > p.form_item_re"))