from pages.base_page import BasePage
from pages.mobile_pages.zfk_mobile_index_page import zfk_Mobile_index_page
import time
class Bill_my_order_page(zfk_Mobile_index_page):
#单据-我的审批内需定位的元素
#单据       Index_receipts
#我的单据    My_bills
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
    #添加审批人员
    def Add_approval_flow(self):
        #点击添加审批人员按钮
        self.click(
            self.find_element_by_css_ykb(
                '#linkSP'
            )
        )
        time.sleep(2)
        #遍历输出
        lender=self.find_elements_by_xpath('//*[@id="ul_col"]/li/a[1]/p[1]')
        leader_list=[]
        for i in lender:
            leader_list.append(i.text)
        print(leader_list)
        if '李妍' in leader_list:
            lender_num=leader_list.index('李妍')
            lender_id=(2*(lender_num+1))
            print(lender_id)
        #// *[ @ id = "ul_col"] / li['+2(lender_id+1)+'] / a[1] / p[1]
            time.sleep(2)
            self.click(self.find_element_by_css_ykb('#ul_col > li:nth-child('+str(lender_id)+')'))
            time.sleep(2)
            self.click(self.find_element_by_css_ykb('#choseReady'))
            time.sleep(2)
        self.click(
            self.find_element_by_css_ykb(
                '#confirmBtn'
            )

        )
    #添加审批人员-新单据
    def Add_approval_flow_new_order(self):
        #点击添加审批人员按钮
        self.click(
            self.find_element_by_css_ykb(
                '#spBlock > div.leader-alt-kong.leader-alt-kong2'
            )
        )
        time.sleep(2)
        #遍历输出
        lender=self.find_elements_by_xpath('//*[@id="ul_col"]/li/a[1]/p[1]')
        leader_list=[]
        for i in lender:
            leader_list.append(i.text)
        print(leader_list)
        if '李妍' in leader_list:
            lender_num=leader_list.index('李妍')
            lender_id=(lender_num)
            print(lender_id)
            time.sleep(2)
            self.click(self.find_element_by_css_ykb('#ul_col > li:nth-child(9) > a.mui-pull-left.ablock'))
            time.sleep(2)
            self.click(self.find_element_by_css_ykb('#leaderlist > div > div.mui-bar.mui-bar-tab.hasBLine.ab > button'))
            time.sleep(2)
            self.click(self.find_element_by_css_ykb(
                '#leader > div > div.mui-bar.mui-bar-tab.hasBLine.ab.spryanxs > button'
            )
         )

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

    #进入待提交，执行提交操作
    def To_submit(self):
        #点单据
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div.ykb_fot > p:nth-child(2)'
            )
        )
        time.sleep(10)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-tit > div:nth-child(2)'
            )
        )
        time.sleep(10)
        self.click(
            self.find_element_by_css_ykb(
                "#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_search > span.form_search_txt"
            )
        )
        time.sleep(10)
        self.click(
            self.find_element_by_css_ykb(
            "#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_status_wrap > p:nth-child(1)"
            )
        )
        time.sleep(10)

    #提交-借款申请单
    def submit_order_borrow(self):
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
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div:nth-child(2) > div.guo_scroll_content > div.form_item_ul > div:nth-child(1)'
            )
        )
        time.sleep(5)
        self.click(
            self.find_element_by_css_ykb(
                '#SubmitLoan'
            )
        )
        self.Add_approval_flow()
        time.sleep(5)

    #提交-出差申请单
    def submit_order_evection(self):
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_search > span.form_search_alt'
            )
        )
        time.sleep(2)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_alt_wrap > div.form_alt > span:nth-child(5)'
            )
        )
        time.sleep(1)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_alt_wrap > div.form_alt_fot > button.button.button-success'
            )
        )
        time.sleep(5)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div:nth-child(2) > div.guo_scroll_content > div.form_item_ul > div:nth-child(1)'
            )
        )
        time.sleep(5)
        self.click(
            self.find_element_by_css_ykb(
                '#submitApply'
            )
        )
        self.Add_approval_flow()

        time.sleep(5)

#提交单子-费用报销单
    def submit_order_cost(self):
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
        time.sleep(1)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div:nth-child(2) > div.guo_scroll_content > div.form_item_ul > div:nth-child(1)'
            )
        )
        time.sleep(5)
        self.click(
            self.find_element_by_css_ykb(
                '#commitBtr'
            )
        )
        self.Add_approval_flow_new_order()

        time.sleep(5)

# 提交单子-差旅报销单
    def submit_order_travel(self):
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




