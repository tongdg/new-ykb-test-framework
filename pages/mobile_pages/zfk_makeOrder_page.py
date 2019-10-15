#五张单据的提单操作
import time
import random
from pages.mobile_pages.zfk_mobile_index_page import zfk_Mobile_index_page
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException
class zfk_makeOrder_page(zfk_Mobile_index_page):
#---------------------------------出差申请单-Evection_order--------------------------
    #开始日期-BeginTime
    def BeginTime(self):
         print('-我暂时没用-')
    #这里使用出差申请单的默认值
    #结束日期-EndTime
    def EndTime(self):
        time.sleep(2)
        self.click(self.find_element_by_css_ykb("#setInDate"))
        time.sleep(2)
        self.click(self.find_element_by_css_ykb('#calendar > div:nth-child(1) > ul > li:nth-child(19)'))
    #出发地-BeginAddress
    def BeginAddress(self):
        time.sleep(2)
        self.click(self.find_element_by_css_ykb("#setOutPlace"))
        time.sleep(3)
        self.click(self.find_element_by_css_ykb("#ul_city > li:nth-child(2)"))
        time.sleep(1)
    #目的地-EndAddress
    def EndAddress(self):
        time.sleep(1)
        self.click(self.find_element_by_id_ykb("setInPlace"))
        time.sleep(1)
        self.click(self.find_element_by_css_ykb("#ul_city > li:nth-child(15)"))
        time.sleep(1)
    # 新版机票的出发地选择
    def New_plan_BeginAddress(self):
        self.click(
            self.find_element_by_css_ykb(
                '#container > div > div.index-content > div:nth-child(3) > div.city-select > div.departure-city > div')
        )
        time.sleep(2)
        self.click(
            self.find_element_by_xpath(
                '//*[@id="container"]/div/div[1]/div[3]/div[2]/div[1]/div/div[2]/section[3]/ul/li[1]')
        )
        time.sleep(1)
        # 新版机票的终点选择
    # 新版机票的目的地选择
    def New_play_EndAddress(self):
        time.sleep(2)
        self.click(
            self.find_element_by_css_ykb(
                '#container > div > div.index-content > div:nth-child(3) > div.city-select > div.arrival-city > div'
            )
        )
        time.sleep(2)
        self.click(
            self.find_element_by_xpath(
                '//*[@id="container"]/div/div[1]/div[3]/div[2]/div[1]/div/div[2]/section[3]/ul/li[17]')
        )
    #出差事由-Evection_reason
    def Evection_reason(self):
        time.sleep(1)
        self.send_keys(self.find_element_by_css_ykb("#desc"),'用于自动化测试的流程的测试')
        time.sleep(1)
    #选择火车Choince_train
    def Choice_train(self):
        time.sleep(2)
        self.click(
            self.find_element_by_css_ykb(
                "#goToTrain > div > span.apply_type_txt"
            )
        )
        time.sleep(8)
        #出发地
        self.click(
            self.find_element_by_css_ykb(
                '#container > div.index-content > div:nth-child(3) > div.city-select > div.departure-city'
            )
        )
        time.sleep(2)
        self.click(
            self.find_element_by_css_ykb(
                '#container > div.index-content > div:nth-child(3) > div.ykb-city-picker > div.mint-popup.mint-popup-right > div > div.body > div > section.dd > ul > li:nth-child(1)'
            )
        )
        time.sleep(2)
        #目的地
        self.click(
            self.find_element_by_css_ykb(
                '#container > div.index-content > div:nth-child(3) > div.city-select > div.arrival-city'
            )
        )
        time.sleep(2)
        self.click(
            self.find_element_by_css_ykb(
                '#container > div.index-content > div:nth-child(3) > div.ykb-city-picker > div.mint-popup.mint-popup-right > div > div.body > div > section.dd > ul > li:nth-child(2)'
            )
        )
        time.sleep(2)
        # 后期判断拓展
        Evection_standard = self.find_element_by_css_ykb("#container > div.index-content > div.travel-standard > div.right").text
        print("测试企业的火车标准为" + Evection_standard)

        self.click(self.find_element_by_css_ykb("#container > div.index-content > button"))
        # 火车票查询较慢，时间给足
        time.sleep(10)
        #选择大于今天的火车票-保证前六个有票
        self.click(self.find_element_by_css_ykb(
            '#container > div.train-list-container > div.datepicker-next-previous > div.next-button'))
        time.sleep(2)
        #拿到状态有票的火车班次
        train_Have = self.find_elements_by_xpath('//*[@id="container"]/div[1]/div[2]/article/ul/li/div[1]/div[4]/em')
        train_random = []
        for i in train_Have:
            train_random.append(str(i.text )+ '元')
        print(train_random)
        self.log.info("当前列表存在可预订的火车班次有" + str(len(train_Have)))
        #生成随机数
        train=0
        while train<20:
            try:
                time.sleep(2)
                self.click(self.find_element_by_xpath('//*[@id="container"]/div[1]/div[2]/article/ul/li['+str(train)+']/div[1]/div[4]/em'))
                break
            except NoSuchElementException as nsee:
                train = train + 1
        time.sleep(8)
        train_sate=self.find_elements_by_xpath('//*[@id="container"]/div/div[3]/div/span[4]/button')
        self.log.info("当前列表存在可预订的坐席有"+str(len(train_sate)))
        train_sate_list=[]
        for i in train_sate:
            train_sate_list.append(i.text)
        print(train_sate_list)
        #随机座位级
        train_sate_num = random.randrange(1,len(train_sate_list))
        time.sleep(2)
        self.log.info("随机选取座位级:"+str(train_sate_num))
        if '售完' in train_sate_list:
            train_hanve=train_sate_list.index('购票')+1
            self.click(
                self.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[' + str(train_hanve) + ']/span[4]/button')
            )
        else:
            self.click(
                self.find_element_by_xpath('//*[@id="container"]/div/div[3]/div['+str(train_sate_num)+']/span[4]')
            )
            time.sleep(4)
        self.click(
            self.find_element_by_css_ykb('#container > div.train-order-content > div.footer > span.booking')
        )
        time.sleep(5)
        self.Evection_reason()
        time.sleep(2)
        self.click(
            self.find_element_by_css_ykb('#submitApply')
        )
        time.sleep(2)
        self.log.info("我要制单-出差申请单-提单火车票成功")
        time.sleep(2)
        self.click(
            self.find_element_by_css_ykb('#confirmBtn')
        )
        time.sleep(2)
        true_button=self.find_element_by_css_ykb('body > div.mui-popup.mui-popup-in > div.mui-popup-buttons > span.mui-popup-button.mui-popup-button-bold')
        if true_button is not False:
            time.sleep(3)
            self.click(
                self.find_element_by_css_ykb('body > div.mui-popup.mui-popup-in > div.mui-popup-buttons > span.mui-popup-button.mui-popup-button-bold')
            )
            time.sleep(2)
            self.click(
                self.find_element_by_css_ykb('#header > em')
            )
            self.log.info('我要制单-出差申请单-火车提单成功')
        else:
            self.log.info('我要制单-出差申请单-火车提单失败')
            return False
    #选择酒店Choince_hotel
    def Choince_hotel(self):
        #选择酒店icon
        self.click(
            self.find_element_by_css_ykb(
                "#goToHotel > div > span.apply_type_txt"
            )
        )
        time.sleep(8)
        self.click(
            self.find_element_by_css_ykb(
            "#container > div.index-content > div:nth-child(1) > div.city-select > div.departure-city > div > p")
        )
        time.sleep(2)
        #选择入住地点
        self.click(
            self.find_element_by_css_ykb(
            "#container > div.index-content > div:nth-child(1) > div.ykb-city-picker > div.mint-popup.mint-popup-right > div > div.body > div:nth-child(1) > section.dd > ul > li:nth-child(1)")
        )
        time.sleep(2)
        # 后期判断拓展
        Evection_standard = self.find_element_by_css_ykb(
            "#container > div.index-content > div.travel-standard > div.right > p").text
        print("测试企业的住宿准为" + Evection_standard)
        time.sleep(3)
        #点击查询按钮
        self.click(
            self.find_element_by_css_ykb(
                "#container > div.index-content > button"
            )
        )
        # 酒店查询较慢，时间给足
        time.sleep(20)
        #为保证可以预订成功不出现个人预付的情况，筛选公司统付类型的酒店
        self.click(
            self.find_element_by_css_ykb(
                '#container > div.ykb-filter-bar > div.mint-tabbar > a:nth-child(3)'
            )
        )
        time.sleep(1)
        #选择筛选条件类型
        self.click(
            self.find_element_by_css_ykb(
                '#container > div.ykb-filter-bar > div.mint-popup.filter-popup.mint-popup-bottom > ul > li > div'
            )
        )
        time.sleep(12)
        room_num=1
        while room_num<10:
            try:
                self.click(self.find_element_by_xpath(
                    '//*[@id="container"]/div[1]/div[2]/article/ul/li[' + str(room_num) + ']')
                )
                time.sleep(5)
                full=self.find_element_by_css_ykb('body > div.mint-toast.is-placebottom > span')
                if full is True:
                    self.click(
                        self.find_element_by_css_ykb('#app > div > header > div.mint-header-button.is-left > button')
                    )
                    self.log.info('当前酒店已暂无房源，回退重选')
                else:
                    self.click(self.find_element_by_xpath(
                        '//*[@id="app"]/div/div/div/div/div[6]/div/div[' + str(room_num) + ']/section/div[2]/div/p/em'))
                break
            except NoSuchElementException as ne:
                room_num = room_num + 1
        time.sleep(15)
        room_num_true=1
        while room_num_true<10:
            try:
                self.click(
                    self.find_element_by_css_ykb('#app > div > div > div > div > div:nth-child(6) > div > div:nth-child(1) > ul > li:nth-child('+str(room_num_true)+') > div > div.cell-bd-r > div.hotel-btn-mod',3))
                break
            except NoSuchElementException as te:
                room_num_true =  room_num_true + 1
        time.sleep(3)
        self.click(
            self.find_element_by_css_ykb(
                "#container > footer > div > div > span.booking > button")
        )
        time.sleep(10)
        self.BeginAddress()
        time.sleep(3)
        self.Evection_reason()
        time.sleep(2)
        self.click(self.find_element_by_css_ykb('#submitApply'))
        time.sleep(2)
        self.click(self.find_element_by_css_ykb('#confirmBtn'))
        time.sleep(1)
        self.click(self.find_element_by_css_ykb('body > div.mui-popup.mui-popup-in > div.mui-popup-buttons > span.mui-popup-button.mui-popup-button-bold'))
        time.sleep(2)
    #选择机票Choince_plan
    def Choince_plan(self):
        self.BeginAddress()
        self.EndAddress()
        #填写出差事由
        self.Evection_reason()
        time.sleep(2)
        self.click(self.find_element_by_css_ykb("#goToPlane > div > span.apply_type_txt"))
        time.sleep(4)
        #后期判断拓展
        Evection_standard=self.find_element_by_css_ykb("#container > div > div.index-content > div.travel-standard > div.right").text
        print("测试企业的机票标准为"+Evection_standard)
        time.sleep(2)
        self.click(self.find_element_by_css_ykb("#container > div > div.index-content > button"))
        time.sleep(2)
        #机票查询较慢，时间给足
        time.sleep(10)
        #为保证成功订单，选择大于当天的机票
        self.click(
            self.find_element_by_css_ykb(
                '#container > div > div.flight-list-container > div.flight-datepicker-next-previous > div.next-button'
            )
        )
        time.sleep(15)
        #拿到刷出机票列表的机票信息
        plan_num=self.find_elements_by_xpath('//*[@id="container"]/div/div[1]/div[2]/article/div')
        time.sleep(3)
        self.log.info("当前列表存在航班信息:" + str(len(plan_num)))
        choince_plan=random.randrange(1,5)
        print('随机航班列:'+str(choince_plan))
        self.click(
            self.find_element_by_xpath(
                '//*[@id="container"]/div/div[1]/div[2]/article/div['+str(choince_plan)+']'
            )
        )
        time.sleep(4)
        #随机选一张价位飞机坐
        plan_level=self.find_elements_by_xpath('//*[@id="container"]/div/div[1]/div[2]/article/div[3]/ul/li/div[2]')
        self.log.info("当前对应航班信息下存在的舱级个数有:"+str(len(plan_level)))
        plan_seat=random.randrange(1,5)
        print('随机仓位'+str(plan_seat))
        time.sleep(5)
        self.click(
            self.find_element_by_xpath(
            '//*[@id="container"]/div/div[1]/div[2]/article/div['+str(choince_plan)+']/ul/li['+str(plan_seat)+']/div[2]'

            )
        )
        time.sleep(4)
        # 点击提交按钮
        self.click(
            self.find_element_by_css_ykb(
                "#container > div > div.footer > span.booking > button"
            )
        )
        time.sleep(10)
        #点击提交申请按钮
        self.click(
            self.find_element_by_css_ykb(
                '#submitApply'
            )
        )
        self.click(
            self.find_element_by_css_ykb(
                '#confirmBtn'
            )
        )
        time.sleep(3)
        display_window = self.find_element_by_class_name_ykb('mui-popup-inner')
        print(display_window)
        if display_window is not False:
            time.sleep(4)
            self.click(
                self.find_element_by_css_ykb(
                    "body > div.mui-popup.mui-popup-in > div.mui-popup-buttons > span.mui-popup-button.mui-popup-button-bold"
                )
            )
            time.sleep(5)
        else:
            return False
    #出差申请单-机票
    def Make_Evection_order_plan(self):
        time.sleep(3)
    #进入我要制单
        self.click(
            self.find_element_by_css_ykb(
                "#guo > div.main.scroller > div > div.ykb_content > div.ykb_main_content > div.ykb_main > p:nth-child(2)"
            )
        )
        time.sleep(2)
        self.log.info("首页-我要制单-出差申请单")
        self.click(self.find_element_by_css_ykb("#guo > div.main.scroller.main1 > div > div:nth-child(6)"))
        time.sleep(2)
        evection_url = self.current_url()
        evection_true_url = "FeeBelong/Apply"
        if evection_true_url in evection_url:
            self.log.info("首页-我要制单-出差申请单跳转成功")
            if self.Choince_plan() is not False:
                self.log.info("出差申请单-机票提单成功")
                return True
            else:
                self.log.info("出差申请单-机票提单错误-重复下单")
                return False
        else:
            if evection_true_url not in evection_url:
                self.log.info('出差申请单-机票地址跳转错误'+evection_url)
    #出差申请单-火车 #如果前六个为无票，那么操作鼠标滚轮向下获取到有票信息
    def Make_Evection_order_train(self):
        time.sleep(3)
        # 进入我要制单
        self.click(
            self.find_element_by_css_ykb(
                "#guo > div.main.scroller > div > div.ykb_content > div.ykb_main_content > div.ykb_main > p:nth-child(2)"
            )
        )
        time.sleep(2)
        self.log.info("首页-我要制单-出差申请单")
        self.click(self.find_element_by_css_ykb("#guo > div.main.scroller.main1 > div > div:nth-child(6)"))
        time.sleep(2)
        evection_url = self.current_url()
        evection_true_url = "FeeBelong/Apply"
        if evection_true_url in evection_url:
            self.log.info("首页-我要制单-出差申请单跳转成功")
            if self.Choice_train() is not False:
                return True
            else:
                return False
        else:
            err_borrow_url = self.current_url()
            print("首页-我要制单-借款申请单单跳转失败-错误地址为" + err_borrow_url)
            return False
    #出差申请单-酒店
    def Make_Evection_order_hotel(self):
        time.sleep(3)
        # 进入我要制单
        self.click(
            self.find_element_by_css_ykb(
                "#guo > div.main.scroller > div > div.ykb_content > div.ykb_main_content > div.ykb_main > p:nth-child(2)"
            )
        )
        time.sleep(2)
        self.log.info("首页-我要制单-出差申请单")
        self.click(self.find_element_by_css_ykb("#guo > div.main.scroller.main1 > div > div:nth-child(6)"))
        time.sleep(2)
        evection_url = self.current_url()
        evection_true_url = "FeeBelong/Apply"
        if evection_true_url in evection_url:
            self.log.info("首页-我要制单-出差申请单跳转成功")
            if self.Choince_hotel() is not  False:
                self.log.info('首页-我要制单-出差申请单-酒店-提单成功')
                return True
            else:
                self.log.info('首页-我要制单-出差申请单-酒店-提单失败')
                return False
        else:
            err_borrow_url = self.current_url()
            print("首页-我要制单-酒店跳转失败-错误地址为" + err_borrow_url)
            return  False

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
        #提交审批
        if self.Submint_approve() is not False:
            self.click(self.find_element_by_css_ykb('#header > em'))
            return True
        else:
            return False
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
            self.click(self.find_element_by_css_ykb('#commitBtr'))
            time.sleep(2)
            self.click(
                self.find_element_by_css_ykb(
                    '#leader > div > div.mui-bar.mui-bar-tab.hasBLine.ab.spryanxs > button')
            )
            time.sleep(2)
            url=self.current_url()
            true_url='Public/index.html'
            if true_url in url:
                return True
            else:
                return False
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
            self.click(self.find_element_by_css_ykb('#commitBtr'))
            time.sleep(2)
            self.click(
                self.find_element_by_css_ykb(
                    '#leader > div > div.mui-bar.mui-bar-tab.hasBLine.ab.spryanxs > button')
            )
            url = self.current_url()
            true_url = 'Public/index.html'
            if true_url in url:
                return True
            else:
                return False
#------------------费用报销单---------------------------------------
    # 为保证流程速度提单审批只保证必填项
    # 导入消费记录 To_lend_record
    # 制造消费记录 make_list
    def cost_list(self):
        time.sleep(1)
        #点击新建消费记录
        self.click(
            self.find_element_by_css_ykb(
                '#listChooseNe > div > div.mui-bar.mui-bar-tab.fpay.ab > div:nth-child(2) > button.mui-btn.themebgStyle.themeBtn17ab'
            )
        )
        time.sleep(2)
        #选择其他费用
        self.click(
            self.find_element_by_id_ykb(
                'otherIcon')
        )
        time.sleep(1)
        #日期
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
        self.send_keys( self.find_element_by_css_ykb('#remarkMsg'),'费用报销单测试说明')
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
        cost_random = random.randrange(10, 16)
        time.sleep(3)
        self.click(self.find_element_by_xpath('//*[@id="avaFeeClassList"]/div/div[2]/div[1]/ul/li[' + str(cost_random) + ']'))
        time.sleep(2)
    def cost_order(self):
        #我要制单
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller > div > div.ykb_content > div.ykb_main_content > div.ykb_main > p:nth-child(2)'
            )
        )
        time.sleep(2)
        #费用报销单
        self.click(
            self.find_element_by_css_ykb(
                '#guo > div.main.scroller.main1 > div > div:nth-child(2)'
            )
        )
        time.sleep(4)
        #点击导入消费记录
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
            time.sleep(2)
            self.click(self.find_element_by_css_ykb('#commitBtr'))
            time.sleep(2)
            self.click(
                self.find_element_by_css_ykb(
                    '#leader > div > div.mui-bar.mui-bar-tab.hasBLine.ab.spryanxs > button')
            )
            time.sleep(2)
            url=self.current_url()
            true_url='Public/index.html'
            if true_url in url:
                return True
            else:
                return False
        else:
            time.sleep(1)
            #点击消费记录列表内的全选键
            self.click(
                self.find_element_by_css_ykb(
                    '#listChooseNe > div > div.mui-bar.mui-bar-tab.fpay.ab > div.fixChoose > div.squareChoose')
            )
            #点击提交报销
            self.click(
                self.find_element_by_css_ykb(
                    '#listChooseNe > div > div.mui-bar.mui-bar-tab.fpay.ab > div:nth-child(2) > button.mui-btn.themebgStyle.mui-pull-right.themeBtn089a'
                )
            )
            time.sleep(2)
            #选取费用名称
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
            self.click(self.find_element_by_css_ykb('#commitBtr'))
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