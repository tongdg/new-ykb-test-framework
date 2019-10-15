import random
from config.zfk_config import Travle_dictionaries
from pages.mobile_pages.zfk_mobile_index_page import zfk_Mobile_index_page
import time
from selenium.webdriver.common.keys import Keys
from  config import zfk_config
class zfk_Approval_2_page(zfk_Mobile_index_page):
#借款申请单-普通员工-提单- 审批领导-批单  会计-批单  财务经理批单- 出纳批单
#普通员工登录-制单（存取唯一数据,后继审批领导根据这个数据去查找）-选择审批领导-提单
#审批领导登录-我的审批-找到普通员工提交的单据-审批通过-结束


#Approval_flow_1需要定位的元素
    # 借款金额
    def Amount(self):
        time.sleep(2)
        self.send_keys(self.find_element_by_css_ykb('#amount'), 500)
    # 借款事由
    def Borrowing_reason(self):
        time.sleep(2)
        self.send_keys(
            self.find_element_by_css_ykb(
                '#memo'), '测试借款事由'
        )

    # 提交审批
    def Submint_approve(self):
        time.sleep(2)
        self.click(
            self.find_element_by_css_ykb(
                '#SubmitLoan'
            )
        )
        self.Add_approval_flow()
        time.sleep(2)
        self.click(
            self.find_element_by_css_ykb(
                '#confirmBtn'
            )
        )
        time.sleep(5)
        true_url = self.current_url()
        Borrowing_true_url = 'Public/index.html'
        if Borrowing_true_url in true_url:
            return True
        else:
            return False
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
        if '张富恺' in leader_list:
            lender_num=leader_list.index('张富恺')
            lender_id=(2*(lender_num+1))
            print(lender_id)
            time.sleep(2)
            self.click(self.find_element_by_css_ykb('#ul_col > li:nth-child('+str(lender_id)+')'))
            time.sleep(2)
            self.click(self.find_element_by_css_ykb('#choseReady'))
            time.sleep(2)
        return  True
    #存取单据号
    def save_order_num(self):
        order= self.find_element_by_id_ykb('djhId')
        global num
        num =order.text
        print(num)
    #借款申请单
    def Staff_Borrowing_order(self):
        time.sleep(2)
        #首页我要制单
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div.ykb_content > div.ykb_main_content > div.ykb_main > p:nth-child(2)'
            )
        )
        #借款申请单
        time.sleep(3)
        self.click(
            self.find_element_by_css_ykb(
            '#guo > div.main.scroller.main1 > div > div:nth-child(5)'
            )
        )
        time.sleep(5)
        #存取单据号
        self.save_order_num()
        #借款金额
        time.sleep(1)
        self.Amount()
        time.sleep(1)
        #借款事由
        self.Borrowing_reason()
        #提交审批
        if self.Submint_approve() is not False:
            self.log.info('[--普通员工-提单借款申请单-至审批领导--成功--]')
            return True
        else:
            self.log.info('[--普通员工-提单借款申请单-至审批领导--失败--]')
            return False
    #借款申请单-审批领导-批单
    def leader_approvel(self):
        print("待审核的单据号为"+str(num))
        time.sleep(3)
        #点击-首页-单据
        self.click(
            self.find_element_by_css_ykb('#guo > div.main.scroller > div > div.ykb_fot > p:nth-child(2)')
        )
        time.sleep(3)
        #点击-我的审批
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-tit > div:nth-child(1)'
            )
        )
        time.sleep(3)
        #点击-输入框
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_search > form > input[type=search]'
            )
        )
        #将普通员工提单的单据号-传入搜索框内
        self.send_keys(
            self.find_element_by_css_ykb('#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_search > form > input[type=search]'),num
        )
        time.sleep(3)
        #输入回车
        self.find_element_by_css_ykb(
            '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_search > form > input[type=search]').send_keys(Keys.ENTER)
        time.sleep(8)
        approval_order=self.find_element_by_css_ykb('#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div:nth-child(2) > div.guo_scroll_content > div.form_item_ul > div')
        if approval_order is not  False:
            self.log.info('[--普通员提单至审批领导-成功--]')
            self.log.info('[--审批领导审批开始--]')
            self.click(
                self.find_element_by_css_ykb(
                    '#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div:nth-child(2) > div.guo_scroll_content > div.form_item_ul > div'
                )
            )
            time.sleep(5)
            self.click(
                self.find_element_by_css_ykb(
                    '#commit'
                )
            )
            time.sleep(2)
            self.click(
                self.find_element_by_css_ykb(
                    '#confirmBtn'
                )
            )
            time.sleep(2)
            self.log.info('[-审批领导-审批提单-成功]')
            time.sleep(3)
            return True
        else:
            self.log.info('[--失败--]')
            time.sleep(3)
            return False
    #判断流程-审批流程
    #借款申请单-会计-批单
    def accountant(self):
        # print("待审批的单据号为" + str(num))
        time.sleep(3)
        # 点击-首页-单据
        self.click(
            self.find_element_by_css_ykb('#guo > div.main.scroller > div > div.ykb_fot > p:nth-child(2)')
        )
        time.sleep(5)
        # 点击-审核
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-tit > div:nth-child(1)'
            )
        )
        time.sleep(3)
        # 点击-输入框
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_search > form > input[type=search]'
            )
        )
        #将审批中的单据号-传入搜索框内
        self.send_keys(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_search > form > input[type=search]'),
            num
        )
        time.sleep(3)
        # 输入回车
        self.find_element_by_css_ykb(
            '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_search > form > input[type=search]').send_keys(
            Keys.ENTER)
        time.sleep(3)

        #点击待审核的单据
        self.click(self.find_element_by_css_ykb(
            '#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div:nth-child(2) > div.guo_scroll_content > div.form_item_ul > div:nth-child(1)'
            )
        )
        time.sleep(3)
        self.log.info('[--审批领导-批单-流转至-会计成功--]')
        self.log.info('[--财务审批-财务初审-开始--]')
        time.sleep(3)
        self.click(
        self.find_element_by_css_ykb(
             '#commit'
                )
            )
        time.sleep(2)
        self.click(
            self.find_element_by_css_ykb(
                'body > div.mui-popup.mui-popup-in > div.mui-popup-buttons > span.mui-popup-button.mui-popup-button-bold'
                )
            )
        time.sleep(4)
        self.log.info('借款申请单-财务初审环节-审批成功')
        time.sleep(2)
        return True
    #借款申请单-复核-批单
    def manager_account(self):
        print("待复核的单据号为" + str(num))
        time.sleep(3)
        #点击-首页-单据
        self.click(
            self.find_element_by_css_ykb('#guo > div.main.scroller > div > div.ykb_fot > p:nth-child(2)')
        )
        time.sleep(3)
        # 点击-复核
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-tit > div:nth-child(1)'
            )
        )
        time.sleep(2)
        # 将审批中的单据号-传入搜索框内
        self.send_keys(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_search > form > input[type=search]'),
            num
        )
        time.sleep(3)
        # 输入回车
        self.find_element_by_css_ykb(
            '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_search > form > input[type=search]').send_keys(
            Keys.ENTER)
        time.sleep(3)
        approval_order = self.find_element_by_css_ykb(
            '#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div:nth-child(2) > div.guo_scroll_content > div.form_item_ul > div')
        if approval_order is not False:
            self.log.info('[--审批领导-批单-流转至-会计成功--]')
            self.log.info('[--财务审批-财务初审-开始--]')
            self.click(
                self.find_element_by_css_ykb(
                    '#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div:nth-child(2) > div.guo_scroll_content > div.form_item_ul > div'
                )
            )
            time.sleep(5)
            self.click(
                self.find_element_by_css_ykb(
                    '#commit'
                )
            )
            time.sleep(4)
            self.click(
                self.find_element_by_css_ykb(
                    '#confirmBtn'
                )
            )
            self.log.info('借款申请单-财务复核环节-审批成功')
            time.sleep(2)
        return True
    #借款申请单-出纳-付款
    def cashier(self):
        print('待付款的单据号为'+str(num))
        time.sleep(5)
        self.driver.get(Travle_dictionaries().get("出纳付款"))
        time.sleep(5)
        self.send_keys(
            self.find_element_by_css_ykb(
                '#testApp > div.main > div > div.header > ul > li.searcher > div > input.condition'
            ),num
        )
        time.sleep(2)
        self.find_element_by_css_ykb(
            '#testApp > div.main > div > div.header > ul > li.searcher > div > input.condition').send_keys(Keys.ENTER)
        time.sleep(3)
        self.click(
            self.find_element_by_css_ykb(
                '#myPaymentTask > tr:nth-child(1) > td:nth-child(7)'
            )
        )
        time.sleep(3)
        self.click(
            self.find_element_by_css_ykb(
                '#fixedFoot > button.eui-btn.eui-btn-blue.btn-direct-agree'
            )
        )
        time.sleep(5)
        self.log.info("出纳付款成功")
        return True


