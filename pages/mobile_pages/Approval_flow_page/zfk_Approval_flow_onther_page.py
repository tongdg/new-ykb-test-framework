import random
import time

from config.zfk_config import Travle_dictionaries
from pages.mobile_pages.zfk_mobile_index_page import zfk_Mobile_index_page

class zfk_Approval_flow_onther_page(zfk_Mobile_index_page):
    #待审核-财务初审化解加审业务环节
    # 添加审批人员-新单据
    def Add_approval_flow_new_order(self):
        # 点击添加审批人员按钮
        self.click(
            self.find_element_by_css_ykb(
                '#spBlock > div.leader-alt-kong.leader-alt-kong2'
            )
        )
        time.sleep(2)
        # 遍历输出
        lender = self.find_elements_by_xpath('//*[@id="ul_col"]/li/a[1]/p[1]')
        leader_list = []
        for i in lender:
            leader_list.append(i.text)
        print(leader_list)
        if '童定国' in leader_list:
            lender_num = leader_list.index('童定国')
            lender_id = (lender_num+1)
            print(lender_id)
            time.sleep(2)
            self.click(
                self.find_element_by_xpath(
                    '//*[@id="ul_col"]/li['+str(2*lender_id)+']/a[1]'
                )
            )
            time.sleep(5)
            self.click(
                self.find_element_by_css_ykb(
                    '#choseReady'
                )
            )
    # 添加审批人员-新单据
    def Add_approval_flow_cost_order(self):
    # 点击添加审批人员按钮
            self.click(
                self.find_element_by_css_ykb(
                    '#spBlock > div.leader-alt-kong.leader-alt-kong2'
                )
            )
            time.sleep(2)
            # 遍历输出
            lender = self.find_elements_by_xpath('//*[@id="ul_col"]/li/a[1]/p[1]')
            leader_list = []
            for i in lender:
                leader_list.append(i.text)
            print(leader_list)
            if '童定国' in leader_list:
                lender_num = leader_list.index('童定国')
                lender_id = (lender_num + 1)
                print(lender_id)
                time.sleep(2)
                self.click(
                    self.find_element_by_xpath(
                        '//*[@id="ul_col"]/li[' + str(2 * lender_id) + ']/a[1]'
                    )
                )
                time.sleep(5)
                self.click(
                    self.find_element_by_css_ykb(
                        '#leaderlist > div > div.mui-bar.mui-bar-tab.hasBLine.ab > button'
                    )
                )
    #借款单
    def To_Approvel_borrow(self):
        time.sleep(2)
        # 点单据
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
        time.sleep(5)
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
        time.sleep(2)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_alt_wrap > div.form_alt_fot > button.button.button-success'
            )
        )
        time.sleep(2)
    #费用报销单
    def To_Approvel_cost(self):
        time.sleep(2)
        # 点单据
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div.ykb_fot > p:nth-child(2)'
            )
        )
        time.sleep(4)
        # 点审核
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-tit > div:nth-child(2)'
            )
        )
        time.sleep(5)
        #点击筛选框
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_search > span.form_search_alt'
            )
        )
        time.sleep(2)
        #选择费用报销
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_alt_wrap > div.form_alt > span:nth-child(2)'
            )
        )
        time.sleep(2)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_alt_wrap > div.form_alt_fot > button.button.button-success'
            )
        )
        time.sleep(2)
    #差旅报销单
    def To_Approvel_travel(self):
        time.sleep(2)
         #点单据
        self.click(
                self.find_element_by_css_ykb(
                    '#guo > div.main.scroller > div > div.ykb_fot > p:nth-child(2)'
                )
            )
        time.sleep(4)
        #点审核
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-tit > div:nth-child(2)'
               )
        )
        time.sleep(5)
        # 点击筛选框
        self.click(
                self.find_element_by_css_ykb(
                    '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_search > span.form_search_alt'
                )
            )
        time.sleep(2)
        # 选择差旅报销
        self.click(
                self.find_element_by_css_ykb(
                    '#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_alt_wrap > div.form_alt > span:nth-child(3)'
                )
            )
        time.sleep(2)
        self.click(
                self.find_element_by_css_ykb(
                    '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_alt_wrap > div.form_alt_fot > button.button.button-success'
                )
            )
        time.sleep(2)
    #筛选出借款申请单，点击进去
    def  add_Approvel_borrow(self):
        time.sleep(3)
        #点进借款申请单
        self.click(
            self.find_element_by_css_ykb(
            '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div:nth-child(2) > div.guo_scroll_content > div.form_item_ul > div:nth-child(1)'
            )
        )
        time.sleep(3)
        #点击加审按钮
        self.click(
            self.find_element_by_css_ykb(
                '#verifyBatch > span'
            )
        )
        time.sleep(2)
        #选择财务初审加审业务环节的审批人-童定国
        self.Add_approval_flow_new_order()
        time.sleep(2)
    #筛选出费用报销单，点击进去
    def add_Approvel_cost(self):
        time.sleep(3)
        # 点进借款申请单
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div:nth-child(2) > div.guo_scroll_content > div.form_item_ul > div:nth-child(1)'
            )
        )
        time.sleep(3)
        # 点击加审按钮
        self.click(
            self.find_element_by_css_ykb(
                '#btnLivectr'
            )
        )
        time.sleep(2)
        # 选择财务初审加审业务环节的审批人-童定国
        self.Add_approval_flow_cost_order()
        time.sleep(2)

        #筛选出费用报销单，点击进去
        def add_Approvel_cost(self):
            time.sleep(3)
            # 点进借款申请单
            self.click(
                self.find_element_by_css_ykb(
                    '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div:nth-child(2) > div.guo_scroll_content > div.form_item_ul > div:nth-child(1)'
                )
            )
            time.sleep(3)
            # 点击加审按钮
            self.click(
                self.find_element_by_css_ykb(
                    '#btnLivectr'
                )
            )
            time.sleep(2)
            # 选择财务初审加审业务环节的审批人-童定国
            self.Add_approval_flow_cost_order()
            time.sleep(2)
    #筛选出费用报销单，点击进去
    def add_Approvel_travel(self):
        time.sleep(3)
        # 点进借款申请单
        self.click(
                self.find_element_by_css_ykb(
                    '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div:nth-child(2) > div.guo_scroll_content > div.form_item_ul > div:nth-child(1)'
                )
            )
        time.sleep(3)
        #点击加审按钮
        self.click(
                self.find_element_by_css_ykb(
                    '#btnLivectr'
                )
            )
        time.sleep(2)
        #选择财务初审加审业务环节的审批人-童定国
        self.Add_approval_flow_cost_order()
        time.sleep(2)
    #提单-借款-财务初审的加审业务
    def submit_borrow_approver(self):
        time.sleep(3)
        self.click(
            self.find_element_by_css_ykb(
                '#confirmBtn'
            )
        )
    #提单-费用-财务初审的加审业务
    def submit_cost_approver(self):
        time.sleep(3)
        self.click(
            self.find_element_by_css_ykb(
                '#leader > div > div.mui-bar.mui-bar-tab.hasBLine.ab.spryanxs > button'
            )
        )
    #提单-差旅-财务初审的加审业务
    def submit_travel_approver(self):
        time.sleep(3)
        self.click(
            self.find_element_by_css_ykb(
                '#leader > div > div.mui-bar.mui-bar-tab.hasBLine.ab.spryanxs > button'
            )
        )
        time.sleep(4)

