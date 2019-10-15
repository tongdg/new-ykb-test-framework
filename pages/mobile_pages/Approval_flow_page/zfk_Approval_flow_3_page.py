import random
from config.zfk_config import Travle_dictionaries
from pages.mobile_pages.zfk_mobile_index_page import zfk_Mobile_index_page
import time
from selenium.webdriver.common.keys import Keys
from  config import zfk_config
class zfk_Approval_3_page(zfk_Mobile_index_page):
#费用报销单-普通员工-提单- 审批领导-批单  会计-批单  财务经理批单- 出纳批单
    #存取单据号
    def save_order_num(self):
        order= self.find_element_by_class_name_ykb('djh-text')
        global num
        num =order.text
        print(num)
    #添加审批人员
    def Add_approval_flow(self):
        time.sleep(3)
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
        if '张富恺' in leader_list:
            lender_num=leader_list.index('张富恺')
            lender_id=(2*(lender_num+1))
            print(lender_id)
            time.sleep(2)
            self.click(self.find_element_by_css_ykb('#ul_col > li:nth-child('+str(lender_id)+')'))
            time.sleep(2)
            self.click(
                self.find_element_by_css_ykb(
                '#leaderlist > div > div.mui-bar.mui-bar-tab.hasBLine.ab > button'
                )
            )
            time.sleep(2)
        return  True
    #创建费用报销单的提单消费记录
    def cost_list(self):
        time.sleep(1)
        # 点击新建消费记录
        self.click(
            self.find_element_by_css_ykb(
                '#listChooseNe > div > div.mui-bar.mui-bar-tab.fpay.ab > div:nth-child(2) > button.mui-btn.themebgStyle.themeBtn17ab'
            )
        )
        time.sleep(2)
        # 选择其他费用
        self.click(
            self.find_element_by_id_ykb(
                'otherIcon')
        )
        time.sleep(1)
        # 日期
        self.click(
            self.find_element_by_id_ykb(
                "setOutDate")
        )
        time.sleep(1)
        self.click(
            self.find_element_by_css_ykb(
                "#calendar > div:nth-child(1) > ul > li.dl.jr.cur")
        )
        time.sleep(1)
        self.click(
            self.find_element_by_css_ykb(
                '#calculator > ul.mui-table-view.noTB.anyrecord_g_wrap > li:nth-child(13) > span.span-lab1.clac2.firstShow.ca9')
        )
        time.sleep(1)
        self.click(
            self.find_element_by_css_ykb(
                '#keybord > span:nth-child(7)'
            )
        )
        self.click(
            self.find_element_by_css_ykb(
                '#submitNumCal')
        )
        time.sleep(3)
        self.send_keys(self.find_element_by_css_ykb('#remarkMsg'), '费用报销单测试说明')
        time.sleep(2)
        self.click(
            self.find_element_by_css_ykb(
                '#setting > div.mui-bar.mui-bar-tab.ab > button.mui-btn.themebgStyle.themeBtn17ab')
        )
        time.sleep(2)
        self.click(
            self.find_element_by_css_ykb(
                '#listChooseNe > div > div.mui-bar.mui-bar-tab.fpay.ab > div:nth-child(2) > button.mui-btn.themebgStyle.mui-pull-right.themeBtn089a'
            )
        )
        time.sleep(3)
        # 选取费用名称
        self.click(
            self.find_element_by_css_ykb(
                '#reiForm > div > div.mui-scroll-wrapper.bottom50 > div.mui-scroll > div:nth-child(3) > ul > li:nth-child(1) > a')
        )
        time.sleep(2)
        # 随机选取一个费用名称
        cost_random = random.randrange(11, 16)
        time.sleep(3)
        self.click(
            self.find_element_by_xpath('//*[@id="avaFeeClassList"]/div/div[2]/div[1]/ul/li[' + str(cost_random) + ']'))
        time.sleep(2)
    #普通员工-提单-审批领导
    def approval_cost_order(self):
        # 我要制单
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div.ykb_content > div.ykb_main_content > div.ykb_main > p:nth-child(2)'
            )
        )
        time.sleep(2)
        #进入费用报销单
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller.main1 > div > div:nth-child(2)'
            )
        )
        time.sleep(4)
        #存取提单的单据号
        self.save_order_num()
        # 点击导入消费记录
        self.click(
            self.find_element_by_css_ykb(
                '#reiForm > div > div.mui-bar.mui-bar-tab.ab > button.mui-btn.themebgStyle.themeBtn17ab'
            )
        )
        time.sleep(3)
        list_num = self.find_elements_by_xpath('//*[@id="status_list"]/div[2]/dd')
        self.log.info("当前列表存在消费记录个数为:" + str(len(list_num)))
        #检验消费记录列表个数
        if len(list_num) == 0:
            #创建消费记录
            self.cost_list()
            time.sleep(2)
            self.click(
                self.find_element_by_css_ykb(
                    '#commitBtr'
                )
            )
            time.sleep(2)
            #选择审批领导
            self.Add_approval_flow()
            #提交单据
            self.click(
                self.find_element_by_css_ykb(
                    '#leader > div > div.mui-bar.mui-bar-tab.hasBLine.ab.spryanxs > button')
            )
            time.sleep(5)
            url = self.current_url()
            true_url = 'Public/index.html'
            if true_url in url:
                return True
            else:
                return False
        else:
            time.sleep(1)
            list_num = self.find_elements_by_xpath('//*[@id="status_list"]/div[2]/dd')
            self.log.info("当前列表存在消费记录个数为:" + str(len(list_num)))
            #点击消费记录列表内的默认第一个-避免出现消费记录不一样导致费用名称不可同步的情况
            self.click(
                self.find_element_by_css_ykb(
                    '#status_list > div:nth-child(2) > dd > div > div.hasSquareCheckbox')
            )
            # 点击提交报销
            self.click(
                self.find_element_by_css_ykb(
                    '#listChooseNe > div > div.mui-bar.mui-bar-tab.fpay.ab > div:nth-child(2) > button.mui-btn.themebgStyle.mui-pull-right.themeBtn089a'
                )
            )
            time.sleep(2)
            # 选取费用名称
            self.click(
                self.find_element_by_css_ykb(
                    '#reiForm > div > div.mui-scroll-wrapper.bottom50 > div.mui-scroll > div:nth-child(3) > ul > li:nth-child(1) > a')
            )
            time.sleep(2)
            # 随机选取一个费用名称
            cost_random = random.randrange(11, 16)
            self.click(
                self.find_element_by_xpath('//*[@id="avaFeeClassList"]/div/div[2]/div[1]/ul/li[' + str(cost_random) + ']'))
            time.sleep(2)
            self.click(
                self.find_element_by_css_ykb(
                    '#commitBtr')
            )
            #添加审批领导
            self.Add_approval_flow()
            time.sleep(2)
            self.click(
                self.find_element_by_css_ykb(
                    '#leader > div > div.mui-bar.mui-bar-tab.hasBLine.ab.spryanxs > button')
            )
            time.sleep(5)
            url = self.current_url()
            true_url = 'Public/index.html'
            if true_url in url:
                return True
            else:
                return False
    #审批领导-批单-会计
    def cost_leader_approvel(self):
        print("待审批的单据号为" + str(num))
        time.sleep(3)
        # 点击-首页-单据
        self.click(
            self.find_element_by_css_ykb('#guo > div.main.scroller > div > div.ykb_fot > p:nth-child(2)')
        )
        time.sleep(3)
        # 点击-我的审批
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-tit > div:nth-child(1)'
            )
        )
        time.sleep(3)
        # 点击-输入框
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-main > div.tab-item.tabs-active > div > div.form_item_search > div.form_search > form > input[type=search]'
            )
        )
        # 将普通员工提单的单据号-传入搜索框内
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
        time.sleep(5)
        time.sleep(8)
        approval_order=self.find_element_by_css_ykb('#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div:nth-child(2) > div.guo_scroll_content > div.form_item_ul > div')
        if approval_order is not  False:
            self.log.info('[--普通员提单至审批领导-成功--]')
            self.log.info('[--审批领导审批开始--]')
            self.click(
                self.find_element_by_css_ykb(
                    '#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div:nth-child(2) > div.guo_scroll_content > div.form_item_ul > div:nth-child(1)'
                )
            )
            time.sleep(5)
            self.click(
                self.find_element_by_css_ykb(
                    '#reiForm > div > div.mui-bar.mui-bar-tab.ab > button.mui-btn.themebgStyle.mui-pull-right.themeBtn089a'
                )
            )
            time.sleep(2)
            self.log.info('[费用报销单-审批领导-审批提单-成功]')
            time.sleep(3)
            self.click(
                self.find_element_by_css_ykb(
                    '#leader > div > div.mui-bar.mui-bar-tab.hasBLine.ab.spryanxs > button'
                )
            )
            time.sleep(3)
            return True
        else:
            self.log.info('[--失败--]')
            time.sleep(3)
            return False
    #会计批单-财务经理
    def cost_accountant(self):
        print("待审核的单据号为" + str(num))
        time.sleep(3)
        # 点击-首页-单据
        self.click(
            self.find_element_by_css_ykb('#guo > div.main.scroller > div > div.ykb_fot > p:nth-child(2)')
        )
        time.sleep(5)
        #点击-审核
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-tit > div:nth-child(1)'
            )
        )
        time.sleep(3)
        #点击-输入框
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
        self.log.info('[--财务审批-财务初审-开始--]')
        time.sleep(3)
        self.click(
        self.find_element_by_css_ykb(
             '#reiForm > div > div.mui-bar.mui-bar-tab.ab > button.mui-btn.themebgStyle.mui-pull-right.themeBtn089a'
                )
            )
        time.sleep(2)
        self.click(
            self.find_element_by_css_ykb(
                '#vbody > div.mui-popup.mui-popup-in > div.mui-popup-buttons > span.mui-popup-button.mui-popup-button-bold'
                )
            )
        time.sleep(4)
        self.log.info('借款申请单-财务初审环节-审批成功')
        time.sleep(2)
        return True
    #财务经理批单-出纳
    def cost_manager_account(self):
        print("待复核的单据号为" + str(num))
        time.sleep(3)
        # 点击-首页-单据
        self.click(
            self.find_element_by_css_ykb('#guo > div.main.scroller > div > div.ykb_fot > p:nth-child(2)')
        )
        time.sleep(5)
        #点击-复核
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div:nth-child(2) > div > div.tab-tit > div:nth-child(1)'
            )
        )
        time.sleep(3)
        #点击-输入框
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
        #点击待复核的单据
        self.click(self.find_element_by_css_ykb(
            '#guo > div.main.scroller > div > div.ykb_content > div > div.tab-main > div.tab-item.tabs-active > div > div:nth-child(2) > div.guo_scroll_content > div.form_item_ul > div'
            )
        )
        time.sleep(3)
        self.log.info('[--财务审批-财务复核-开始--]')
        time.sleep(3)
        self.click(
        self.find_element_by_css_ykb(
             '#reiForm > div > div.mui-bar.mui-bar-tab.ab > button.mui-btn.themebgStyle.mui-pull-right.themeBtn089a'
                )
            )
        time.sleep(2)
        self.click(
            self.find_element_by_css_ykb(
                '#leader > div > div.mui-bar.mui-bar-tab.hasBLine.ab.spryanxs > button'
                )
            )
        time.sleep(4)
        self.log.info('费用报销单-财务复核环节-审批成功')
        time.sleep(2)
        return True
    #费用报销单-出纳-付款
    def cost_cashier(self):
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
        time.sleep(5)
        #默认从第一个ifame开始
        self.switch_to_frame(0)
        time.sleep(2)
        self.click(
           self.find_element_by_id_ykb(
               'zhifuBtr'
           )
        )
        time.sleep(5)
        self.log.info("出纳付款成功")
        return True
