#五张单据的提单操作
import time
import random
from pages.mobile_pages.zfk_mobile_index_page import zfk_Mobile_index_page
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException


class MAKEORDER_PAGE(zfk_Mobile_index_page):
#---------------------------------出差申请单-Evection_order--------------------------
    #开始日期-BeginTime
    def BeginTime(self):
         print('-我暂时没用-')
    #这里使用出差申请单的默认值
    #结束日期-EndTime
    def EndTime(self):
        time.sleep(2)
        self.click(
            self.find_element_by_css_ykb(
                "#applyTable > div > div.mui-scroll-wrapper.bottom50 > div.mui-scroll.mui-content > div.bookingTip.chuchaiTop > div > ul > li:nth-child(2) > a"
            )
        )
        time.sleep(2)
        self.click(
            self.find_element_by_css_ykb(
                '#calendar > div:nth-child(1) > ul > li.dl.jr.cur'
            )
        )
    #出发地-BeginAddress
    def BeginAddress(self):
        time.sleep(3)
        self.click(
            self.find_element_by_css_ykb(
                "#applyTable > div > div.mui-scroll-wrapper.bottom50 > div.mui-scroll.mui-content > div.bookingTip.chuchaiTop > div > ul > li:nth-child(3) > a"
            )
        )
        time.sleep(3)
        self.click(
            self.find_element_by_css_ykb(
                "#ul_city > li:nth-child(2)"
            )
        )
        time.sleep(1)
    #目的地-EndAddress
    def EndAddress(self):
        time.sleep(1)
        self.click(
            self.find_element_by_css_ykb(
                "#applyTable > div > div.mui-scroll-wrapper.bottom50 > div.mui-scroll.mui-content > div.bookingTip.chuchaiTop > div > ul > li:nth-child(4) > a"
            )
        )
        time.sleep(1)
        self.click(
            self.find_element_by_css_ykb(
                "#ul_city > li:nth-child(15)"
            )
        )
        time.sleep(1)
    #出差事由-Evection_reason
    def Evection_reason(self):
        time.sleep(1)
        self.send_keys(self.find_element_by_css_ykb("#desc"),'用于自动化测试的流程的测试')
        time.sleep(1)
    #进入出差申请单
    def enter_evaction(self):
        self.click(
            self.find_element_by_css_ykb(
            '#guo > div.main.scroller > div > div.ykb_content > div.ykb_main_content > div.ykb_main > p:nth-child(2)'
            )
        )
        time.sleep(5)
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller.main1 > div > div:nth-child(6)'
            )
        )
    #点击保存
    def save(self):
        self.click(
            self.find_element_by_css_ykb(
                '#saveForm'
            )
        )
    time.sleep(2)
    #返回
    def back_index(self):
        self.click(
            self.find_element_by_css_ykb(
                '#spBack'
            )
        )
    time.sleep(3)
    #点击首页
    def click_index(self):
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div.ykb_fot > p:nth-child(1)'
            )
        )

    def make_evaction(self):
        time.sleep(2)
        self.enter_evaction()
        time.sleep(2)
        self.EndTime()
        time.sleep(2)
        self.BeginAddress()
        time.sleep(2)
        self.EndAddress()
        time.sleep(2)
        time.sleep(2)
        self.Evection_reason()
        time.sleep(2)
        self.save()
        time.sleep(4)
        self.back()
        self.back()
        time.sleep(2)
        self.click_index()

#------------------借款申请单---------------------------------------
    #借款金额 Amount
    #借款事由 Borrowing_reason
    #保存    save
    #提交审批 Submit_approve
    #借款金额
    def Amount(self):
        time.sleep(2)
        self.send_keys(self.find_element_by_css_ykb('#amount'),500)
    #借款事由
    def Borrowing_reason(self):
        time.sleep(2)
        self.send_keys(
            self.find_element_by_css_ykb(
                '#memo'),'测试借款事由'
        )
    #提交审批
    def Submint_approve(self):
        time.sleep(2)
        self.click(
            self.find_element_by_css_ykb(
                '#SubmitLoan'
            )
        )
        time.sleep(2)
        self.click(self.find_element_by_css_ykb('#confirmBtn'))
        true_url=self.current_url()
        Borrowing_true_url='Public/index.html'
        if Borrowing_true_url in true_url:
            return True
        else:
            return False
    def Borrowing_order(self):
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
        #借款金额
        self.Amount()
        #借款事由
        self.Borrowing_reason()
        #点击保存
        time.sleep(3)
        self.click(self.find_element_by_css_ykb('#SaveLoan'))
        time.sleep(3)
        self.back()
        time.sleep(2)
        self.back()
        time.sleep(5)

#------------------差旅报销单---------------------------------------
    #为保证流程速度提单审批只保证必填项
    #行程说明 Travel_explain
    #其他费用 Onther_cost
    #导入消费记录 To_lend_record
    #制造消费记录 make_list
    def choince_list(self):
        time.sleep(1)
        self.click(
            self.find_element_by_css_ykb(
                '#listChooseNe > div > div.mui-bar.mui-bar-tab.fpay.ab > div:nth-child(2) > button.mui-btn.themebgStyle.themeBtn17ab'
            )
        )
        time.sleep(2)
        self.click(
            self.find_element_by_id_ykb(
                'otherIcon')
        )
        time.sleep(1)
        self.click(
            self.find_element_by_id_ykb(
                "setOutDate")
        )
        time.sleep(1)
        self.click(
            self.find_element_by_css_ykb(
                "#calendar > div:nth-child(1) > ul > li.dl.jr.cur")
        )
        time.sleep(2)
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
        time.sleep(1)
        self.send_keys(self.find_element_by_css_ykb(
            '#remarkMsg'
        ),'测试说明'
        )
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

    def Travel_order(self):
        #我要制单
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div.ykb_content > div.ykb_main_content > div.ykb_main > p:nth-child(2)'
            )
        )
        time.sleep(2)
        #差旅报销
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller.main1 > div > div:nth-child(3)'
            )
        )
        time.sleep(4)
        self.click(
            self.find_element_by_css_ykb(
                '#traForm > div > div.mui-bar.mui-bar-tab.ab > button.mui-btn.themebgStyle.themeBtn17ab'
            )
        )
        time.sleep(3)
        list_num = self.find_elements_by_xpath('//*[@id="status_list"]/div[2]/dd')
        self.log.info("当前列表存在消费记录个数为:" + str(len(list_num)))
        if len(list_num) == 0:
            self.choince_list()
            time.sleep(1)
            self.send_keys(
                self.find_element_by_css_ykb(
                    '#traForm > div > div.mui-scroll-wrapper.bottom50 > div.mui-scroll > div:nth-child(3) > ul > li.mui-table-view-cell.xcsmwc > textarea'
                ), '测试行程说明'
            )
            time.sleep(2)
            self.click(
                self.find_element_by_id_ykb(
                    'saveFormBtn'
                )
            )
            time.sleep(2)
            self.back()
            time.sleep(2)
            self.back()
            time.sleep(2)
        else:
            time.sleep(1)
            self.click(
                self.find_element_by_css_ykb(
                    '#listChooseNe > div > div.mui-bar.mui-bar-tab.fpay.ab > div.fixChoose > div.squareChoose')
            )
            self.click(
                self.find_element_by_css_ykb(
                    '#listChooseNe > div > div.mui-bar.mui-bar-tab.fpay.ab > div:nth-child(2) > button.mui-btn.themebgStyle.mui-pull-right.themeBtn089a'
                )
            )
            self.send_keys(
                self.find_element_by_css_ykb(
                    '#traForm > div > div.mui-scroll-wrapper.bottom50 > div.mui-scroll > div:nth-child(3) > ul > li.mui-table-view-cell.xcsmwc > textarea'
                ),'测试行程说明'
            )
            time.sleep(2)
            self.click(
                self.find_element_by_id_ykb(
                    'saveFormBtn'
                )
            )
            self.back()
            time.sleep(2)
            self.back()
            time.sleep(3)
#------------------费用报销单---------------------------------------
    # 为保证流程速度提单审批只保证必填项
    # 导入消费记录 To_lend_record
    # 制造消费记录 make_list
    def cost_list(self):
        time.sleep(1)
        self.click(
            self.find_element_by_css_ykb(
                '#listChooseNe > div > div.mui-bar.mui-bar-tab.fpay.ab > div:nth-child(2) > button.mui-btn.themebgStyle.themeBtn17ab'
            )
        )
        time.sleep(2)
        self.click(
            self.find_element_by_id_ykb(
                'otherIcon')
        )
        time.sleep(1)
        self.click(
            self.find_element_by_id_ykb(
                "setOutDate")
        )
        time.sleep(1)
        self.click(
            self.find_element_by_css_ykb(
                "#calendar > div:nth-child(1) > ul > li.dl.jr.cur")
        )
        time.sleep(2)
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
        time.sleep(1)
        self.send_keys(self.find_element_by_css_ykb(
            '#remarkMsg'
        ), '测试说明'
        )
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

    def cost_order(self):
        time.sleep(3)
        # 我要制单
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div.ykb_content > div.ykb_main_content > div.ykb_main > p:nth-child(2)'
            )
        )
        time.sleep(2)
        # 费用报销单
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller.main1 > div > div:nth-child(2)'
            )
        )
        time.sleep(4)
        # 点击导入消费记录
        self.click(
            self.find_element_by_css_ykb(
                '#reiForm > div > div.mui-bar.mui-bar-tab.ab > button.mui-btn.themebgStyle.themeBtn17ab'
            )
        )
        time.sleep(3)
        list_num = self.find_elements_by_xpath('//*[@id="status_list"]/div[2]/dd')
        self.log.info("当前列表存在消费记录个数为:" + str(len(list_num)))
        if len(list_num) == 0:
            self.cost_list()
            time.sleep(5)
            self.click(
                self.find_element_by_css_ykb(
                    '#reiForm > div > div.mui-scroll-wrapper.bottom50 > div.mui-scroll > div:nth-child(3) > ul > li:nth-child(1) > a'
                )
            )
            time.sleep(4)
            # 随机选取一个费用名称
            cost_random = random.randrange(10, 16)
            time.sleep(3)
            self.click(
                self.find_element_by_xpath(
                    '//*[@id="avaFeeClassList"]/div/div[2]/div[1]/ul/li[' + str(cost_random) + ']'))
            time.sleep(2)
            self.click(
                self.find_element_by_css_ykb(
                    '#saveFormBtn'
                )
            )
            time.sleep(3)
            self.click(
                self.find_element_by_css_ykb(
                    '#app > div > div.mui-navbar > div > button > span'
                )
            )
            time.sleep(3)
            self.click(
                self.find_element_by_css_ykb(
                    '#header > em'
                )
            )
        else:
            time.sleep(2)
            # 点击消费记录列表内的全选键
            self.click(
                self.find_element_by_css_ykb(
                    '#listChooseNe > div > div.mui-bar.mui-bar-tab.fpay.ab > div.fixChoose > div.squareChoose')
            )
            time.sleep(1)
            # 点击提交报销
            self.click(
                self.find_element_by_css_ykb(
                    '#listChooseNe > div > div.mui-bar.mui-bar-tab.fpay.ab > div:nth-child(2) > button.mui-btn.themebgStyle.mui-pull-right.themeBtn089a'
                )
            )
            time.sleep(4)
            # 选取费用名称
            self.click(
                self.find_element_by_css_ykb(
                    '#reiForm > div > div.mui-scroll-wrapper.bottom50 > div.mui-scroll > div:nth-child(3) > ul > li:nth-child(1) > a')
            )
            time.sleep(2)
            # 随机选取一个费用名称
            cost_random = random.randrange(10, 16)
            self.click(
                self.find_element_by_xpath('//*[@id="avaFeeClassList"]/div/div[2]/div[1]/ul/li[' + str(cost_random) + ']'))
            time.sleep(2)
            self.click(self.find_element_by_css_ykb('#saveFormBtn'))
            time.sleep(3)
            self.click(
                self.find_element_by_css_ykb(
                    '#app > div > div.mui-navbar > div > button > span'
                )
            )
            time.sleep(3)
            self.click(
                self.find_element_by_css_ykb(
                    '#header > em'
                )
            )