from pages.base_page import BasePage
from pages.mobile_pages.zfk_mobile_index_page import zfk_Mobile_index_page
import time
class Bill_my_order_page(zfk_Mobile_index_page):
    #进入审批中，执行五张单子的撤回
    def In_approval_recall(self):
        #点单据
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div.ykb_fot > p:nth-child(2)'
            )
        )
        time.sleep(4)
        #点我的单据
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-tit > div:nth-child(2)'
            )
        )
        time.sleep(5)

    #撤回-借款申请单
    def widthdraw_order_borrow(self):
        #点击筛选
        self.click(
            self.find_element_by_css_ykb(
            '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_search > span.form_search_alt'
            )
        )
        time.sleep(2)
        #点击借款申请单
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_alt_wrap > div.form_alt > span:nth-child(4)'
            )
        )
        time.sleep(1)
        #点击确定按钮
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_alt_wrap > div.form_alt_fot > button.button.button-success'
            )
        )
        time.sleep(5)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div:nth-child(3) > div.guo_scroll_content > div.form_item_ul > div:nth-child(1)')
        )
        time.sleep(5)
        self.click(
            self.find_element_by_css_ykb(
            '#Retrieve'
            )
        )
        time.sleep(2)
        self.click(
            self.find_element_by_css_ykb(
                'body > div.mui-popup.mui-popup-in > div.mui-popup-buttons > span.mui-popup-button.mui-popup-button-bold'
            )
        )
    #撤回-出差申请单
    def widthdraw_order_evection(self):
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
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div:nth-child(3) > div.guo_scroll_content > div.form_item_ul > div:nth-child(1)'
            )
        )
        time.sleep(5)
        self.click(
            self.find_element_by_css_ykb(
                '#Retrieve'
            )
        )
        time.sleep(2)
        self.click(
            self.find_element_by_css_ykb(
                'body > div.mui-popup.mui-popup-in > div.mui-popup-buttons > span.mui-popup-button.mui-popup-button-bold'
            )
        )
        time.sleep(5)

    #撤回-费用报销单
    def widthdraw_order_cost(self):
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_search > span.form_search_alt'
            )
        )
        time.sleep(2)
        #选择筛选条件-费用报销单
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
        time.sleep(3)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div:nth-child(3) > div.guo_scroll_content > div.form_item_ul > div:nth-child(1)'
            )
        )
        time.sleep(5)
        self.click(
            self.find_element_by_css_ykb(
                '#reiForm > div > div.mui-bar.mui-bar-tab.ab.hasBLine > button'
            )
        )
        time.sleep(5)

# 撤回单子-差旅报销单
    def widthdraw_order_travel(self):
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
        time.sleep(6)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div:nth-child(3) > div.guo_scroll_content > div.form_item_ul > div:nth-child(1)'
            )
        )
        time.sleep(3)
        self.click(
            self.find_element_by_css_ykb(
                '#traForm > div > div.mui-bar.mui-bar-tab.ab.hasBLine > button'
            )
        )
        time.sleep(5)