from pages.base_page import BasePage
from pages.mobile_pages.zfk_mobile_index_page import zfk_Mobile_index_page
import time
class out_side_1_page(zfk_Mobile_index_page):
    # 进入我审批的-待审批-借款申请单
    def To_approval_return_borrow(self):
        # 点单据
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div.ykb_fot > p:nth-child(2)'
            )
        )
        time.sleep(4)
        #筛选借款申请单
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_search > span.form_search_alt'
            )
        )
        time.sleep(3)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_alt_wrap > div.form_alt > span:nth-child(4)'
            )
        )
        time.sleep(2)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_alt_wrap > div.form_alt_fot > button.button.button-success'
            )
        )
    # 外层退回单子-借款申请单
    def return_order_borrow(self):
        time.sleep(2)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div:nth-child(2) > div.guo_scroll_content > div.form_item_ul > div:nth-child(1) > span'
            )
        )
        time.sleep(2)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_total_btn > div.form_item_agree.clearfix > button:nth-child(1)'
            )
        )
        time.sleep(2)
        self.send_keys(
            self.find_element_by_css_ykb(
                'body > div.mui-popup.mui-popup-in > div.mui-popup-inner > div.mui-popup-text > textarea'), '测试借款单-领导退回'
        )
        time.sleep(4)
        self.click(
            self.find_element_by_css_ykb(
                'body > div.mui-popup.mui-popup-in > div.mui-popup-buttons > span.mui-popup-button.mui-popup-button-bold'
            )
        )

    # 进入我审批的-待审批-费用报销单
    def To_approval_return_cost(self):
        # 点单据
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div.ykb_fot > p:nth-child(2)'
            )
        )
        time.sleep(4)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_search > span.form_search_alt'
            )
        )
        time.sleep(3)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_alt_wrap > div.form_alt > span:nth-child(2)'
            )
        )
        time.sleep(2)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_alt_wrap > div.form_alt_fot > button.button.button-success'
            )
        )
    # 外层退回单子-费用报销单
    def return_order_cost(self):
        time.sleep(2)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div:nth-child(2) > div.guo_scroll_content > div.form_item_ul > div:nth-child(1) > span'
            )
        )
        time.sleep(2)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_total_btn > div.form_item_agree.clearfix > button:nth-child(1)'
            )
        )
        time.sleep(2)
        self.send_keys(
            self.find_element_by_css_ykb(
                'body > div.mui-popup.mui-popup-in > div.mui-popup-inner > div.mui-popup-text > textarea'),
            '测试费用报销单-领导退回'
        )
        time.sleep(4)
        self.click(
            self.find_element_by_css_ykb(
                'body > div.mui-popup.mui-popup-in > div.mui-popup-buttons > span.mui-popup-button.mui-popup-button-bold'
            )
        )
        time.sleep(4)

    #进入我审批的-待审批-差旅报销单
    def To_approval_return_travel(self):
        # 点单据
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div.ykb_fot > p:nth-child(2)'
            )
        )
        time.sleep(4)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_search > span.form_search_alt'
            )
        )
        time.sleep(3)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_alt_wrap > div.form_alt > span:nth-child(3)'
            )
        )
        time.sleep(2)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_alt_wrap > div.form_alt_fot > button.button.button-success'
            )
        )
    #外层退回单子-差旅报销单
    def return_order_travel(self):
        time.sleep(2)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div:nth-child(2) > div.guo_scroll_content > div.form_item_ul > div:nth-child(1) > span'
            )
        )
        time.sleep(2)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_total_btn > div.form_item_agree.clearfix > button:nth-child(1)'
            )
        )
        time.sleep(2)
        self.send_keys(
            self.find_element_by_css_ykb(
                'body > div.mui-popup.mui-popup-in > div.mui-popup-inner > div.mui-popup-text > textarea'),
            '测试差旅报销单-领导退回'
        )
        time.sleep(4)
        self.click(
            self.find_element_by_css_ykb(
                'body > div.mui-popup.mui-popup-in > div.mui-popup-buttons > span.mui-popup-button.mui-popup-button-bold'
            )
        )
        time.sleep(4)

    #进入我审批的-待审批-出差申请单
    def To_approval_return_evection(self):
        # 点单据
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div.ykb_fot > p:nth-child(2)'
            )
        )
        time.sleep(4)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_search > span.form_search_alt'
            )
        )
        time.sleep(3)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_alt_wrap > div.form_alt > span:nth-child(5)'
            )
        )
        time.sleep(2)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_alt_wrap > div.form_alt_fot > button.button.button-success'
            )
        )
    #外层退回单子-出差申请单
    def return_order_evection(self):
        time.sleep(2)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div:nth-child(2) > div.guo_scroll_content > div.form_item_ul > div:nth-child(1) > span'
            )
        )
        time.sleep(2)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_total_btn > div.form_item_agree.clearfix > button:nth-child(1)'
            )
        )
        time.sleep(2)
        self.send_keys(
            self.find_element_by_css_ykb(
                'body > div.mui-popup.mui-popup-in > div.mui-popup-inner > div.mui-popup-text > textarea'),
            '测试出差申请单-领导退回'
        )
        time.sleep(4)
        self.click(
            self.find_element_by_css_ykb(
                'body > div.mui-popup.mui-popup-in > div.mui-popup-buttons > span.mui-popup-button.mui-popup-button-bold'
            )
        )
        time.sleep(4)