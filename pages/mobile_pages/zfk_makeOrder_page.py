#五张单据的提单操作
import time
import random
from pages.mobile_pages.zfk_mobile_index_page import zfk_Mobile_index_page
from selenium.common.exceptions import NoSuchElementException,TimeoutException
class zfk_makeOrder_page(zfk_Mobile_index_page):
#费用报销单-Cost_order
#差旅报销单-Travel_order
#借款申请单-Borrowing_order
#出差申请单-Evection_order
    #开始日期-BeginTime
    def BeginTime(self):
     pass
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
    #出差事由-Evection_reason
    def Evection_reason(self):
        time.sleep(1)
        self.send_keys(self.find_element_by_css_ykb("#desc"),'用于自动化测试的流程的测试')
        time.sleep(1)

    #选择航班Choince_plan
    def Choince_plan(self):
        time.sleep(2)
        self.click(self.find_element_by_css_ykb("#goToPlane > div > span.apply_type_txt"))
        time.sleep(4)
        self.BeginAddress()
        self.EndAddress()
        #后期判断拓展
        Evection_standard=self.find_element_by_css_ykb("#fBiaozhun").text
        print("测试企业的机票标准为"+Evection_standard)
        self.click(self.find_element_by_css_ykb("#searchTicket"))
        #机票查询较慢，时间给足
        time.sleep(10)
        #拿到刷出机票列表的机票信息
        plan_num=self.find_elements_by_xpath('//*[@id="ticketList"]/li')
        time.sleep(3)
        self.log.info("当前列表存在航班信息:" + str(len(plan_num)))
        #生成一个小于plan_num的随机数
        #choince_plan=random.randrange(len(plan_num))
        choince_plan=random.randrange(1,5)
        print('随机航班列:'+str(choince_plan))
        time.sleep(2)
        self.click(self.find_element_by_xpath('// *[ @ id = "ticketList"] / li['+str(choince_plan)+']'))
        time.sleep(3)
        #随机选一张价位飞机坐
        plan_level=self.find_elements_by_xpath('//*[@id="ticketList"]/li[1]/div/div[2]/div/div/div[2]')
        self.log.info("当前对应航班信息下存在的舱级个数有:"+str(len(plan_level)))
        plan_seat=random.randrange((len(plan_level)))
        print('随机仓位'+str(plan_seat))
        time.sleep(5)
        self.click(self.find_element_by_xpath('//*[@id="ticketList"]/li['+str(choince_plan)+']/div/div[2]/div['+str(plan_seat+1)+']/div/div[2]'))
        time.sleep(4)
        #点击提交按钮
        self.click(self.find_element_by_css_ykb("#tOrder > div > nav > div.money-btnpd"))
        time.sleep(4)
        self.Evection_reason()        #点击提交申请
        self.click(self.find_element_by_css_ykb("#submitApply"))
        time.sleep(4)
        self.click(self.find_element_by_css_ykb("#confirmBtn"))
        time.sleep(4)
        self.click(
            self.find_element_by_css_ykb(
                "body > div.mui-popup.mui-popup-in > div.mui-popup-buttons > span.mui-popup-button.mui-popup-button-bold")
        )
        time.sleep(4)
        self.log.info("我要制单-出差申请单-提单机票成功")
        time.sleep(4)
        self.click(self.find_element_by_css_ykb('#header > em'))

    #选择火车Choince_train
    def Choice_train(self):
        time.sleep(2)
        self.click(self.find_element_by_css_ykb("#goToTrain > div > span.apply_type_txt"))
        time.sleep(8)
        # 后期判断拓展
        Evection_standard = self.find_element_by_css_ykb("#container > div.index-content > div.travel-standard > div.right").text
        print("测试企业的火车标准为" + Evection_standard)
        self.click(self.find_element_by_css_ykb("#container > div.index-content > button"))
        # 火车票查询较慢，时间给足
        time.sleep(10)
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
        #//*[@id="container"]/div[1]/div[2]/article/ul/li[13]/div[1]/div[4]/em
        #//*[@id="container"]/div[1]/div[2]/article/ul/li[14]/div[1]/div[4]/em


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
        train_sate_num = random.randrange(1,len(train_sate_list+1))
        time.sleep(2)
        self.log.info("随机选取座位级:"+str(train_sate_num))
        if '售完' in train_sate_list:
            train_hanve=train_sate_list.index('购票')+1
            self.click(self.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[' + str(train_hanve) + ']/span[4]/button'))
            time.sleep(4)
        self.click(self.find_element_by_css_ykb('#container > div.train-order-content > div.footer > span.booking > button'))
        time.sleep(5)
        self.click(self.find_element_by_css_ykb('#submitApply'))
        time.sleep(3)
        self.click(self.find_element_by_css_ykb('#confirmBtn'))
        time.sleep(2)
        self.log.info("我要制单-出差申请单-提单火车票成功")
        time.sleep(2)
        self.click(self.find_element_by_css_ykb('#header > em'))


    #选择酒店Choince_hotel
    def Choince_hotel(self):
        self.click(self.find_element_by_css_ykb("#goToHotel > div > span.apply_type_txt"))
        time.sleep(8)
        self.click(self.find_element_by_css_ykb(
            "#container > div.index-content > div:nth-child(1) > div.city-select > div.departure-city > div > p"))
        time.sleep(2)
        self.click(self.find_element_by_css_ykb(
            "#container > div.index-content > div:nth-child(1) > div.ykb-city-picker > div.mint-popup.mint-popup-right > div > div.body > div:nth-child(1) > section.dd > ul > li:nth-child(1)"))
        time.sleep(2)
        # 后期判断拓展
        Evection_standard = self.find_element_by_css_ykb(
            "#container > div.index-content > div.travel-standard > div.right > p").text
        print("测试企业的住宿准为" + Evection_standard)
        time.sleep(3)
        self.click(self.find_element_by_css_ykb("#container > div.index-content > button"))
        # 酒店查询较慢，时间给足
        time.sleep(20)
        #随机生成一个随机数
        hotel_range = random.randrange(1,5)
        self.click(self.find_element_by_xpath('//*[@id="container"]/div[1]/div[2]/article/ul/li['+str(hotel_range)+']'))
        time.sleep(8)
        room_num=1
        while room_num<10:
            try:
                self.click(self.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[6]/div/div['+str(room_num)+']/section/div[2]/div/p/em'))
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
        self.click(self.find_element_by_css_ykb("#container > footer > div > div > span.booking > button"))
        time.sleep(5)


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
            self.Choince_plan()
        else:
            err_borrow_url = self.current_url()
            print("首页-我要制单-借款申请单单跳转失败-错误地址为" + err_borrow_url)

    #出差申请单-火车
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
            time.sleep(3)
            self.EndTime()
            time.sleep(1)
            self.BeginAddress()
            time.sleep(1)
            self.EndAddress()
            time.sleep(1)
            self.Evection_reason()
            time.sleep(1)
            self.Choice_train()
        else:
            err_borrow_url = self.current_url()
            print("首页-我要制单-借款申请单单跳转失败-错误地址为" + err_borrow_url)

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
            self.Choince_hotel()
            self.BeginAddress()
            self.Evection_reason()
            self.click(self.find_element_by_css_ykb("#submitApply"))
            time.sleep(2)
            self.click(self.find_element_by_css_ykb('#confirmBtn'))
            time.sleep(2)
        else:
            err_borrow_url = self.current_url()
            print("首页-我要制单-借款申请单单跳转失败-错误地址为" + err_borrow_url)

