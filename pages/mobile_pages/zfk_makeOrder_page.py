#五张单据的提单操作
import time
import random
from pages.mobile_pages.zfk_mobile_index_page import zfk_Mobile_index_page
class zfk_makeOrder_page(zfk_Mobile_index_page):
#费用报销单  Cost_order
#差旅报销单  Travel_order
#借款申请单  Borrowing_order
#出差申请单  Evection_order
    #开始日期  BeginTime
    def BeginTime(self):
    #这里使用出差申请单的默认值
     pass
    #结束日期  EndTime
    def EndTime(self):
        time.sleep(1)
        self.click(self.find_element_by_css_ykb("#setInDate"))
        time.sleep(1)
        self.click(self.find_element_by_css_ykb("#calendar > div:nth-child(1) > ul > li:nth-child(13)"))
    #出发地    BeginAddress
    def BeginAddress(self):
        time.sleep(1)
        self.click(self.find_element_by_id_ykb("setOutPlace"))
        time.sleep(1)
        self.click(self.find_element_by_css_ykb("#ul_city > li:nth-child(2)"))
        time.sleep(1)
    #目的地      EndAddress
    def EndAddress(self):
        time.sleep(1)
        self.click(self.find_element_by_id_ykb("setInPlace"))
        time.sleep(1)
        self.click(self.find_element_by_css_ykb("#ul_city > li:nth-child(15)"))
        time.sleep(1)
    #出差事由    Evection_reason
    def Evection_reason(self):
        time.sleep(1)
        self.send_keys(self.find_element_by_css_ykb("#desc"),'用于自动化测试的流程的测试')
        time.sleep(1)
    #选择航班    Choince_plan
    def Choince_plan(self):
        time.sleep(2)
        self.click(self.find_element_by_css_ykb("#goToPlane > div > span.apply_type_txt"))
        time.sleep(4)
        #后期判断拓展
        Evection_standard=self.find_element_by_css_ykb("#fBiaozhun").text
        print("测试企业的机票标准为"+Evection_standard)
        self.click(self.find_element_by_css_ykb("#searchTicket"))
        #机票查询较慢，时间给足
        time.sleep(15)
        #拿到刷出机票列表的机票信息
        plan_num=self.find_elements_by_xpath('//*[@id="ticketList"]/li')
        self.log.info("当前列表存在航班信息:" + str(len(plan_num)))
        #生成一个小于plan_num的随机数
        choince_plan=random.randrange(len(plan_num)+1)
        print(choince_plan)
        time.sleep(2)
        self.click(self.find_element_by_xpath('//*[@id="ticketList"]/li['+str(choince_plan)+']'))
        time.sleep(50)
    #选择火车    Choince_train

    #选择酒店    Choince_hotel

#采购申请单  Shope_order
    def Make_Evection_order(self):
        time.sleep(3)
    #进入我要制单
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
            self.Choince_plan()

        else:
            err_borrow_url = self.current_url()
            print("首页-我要制单-借款申请单单跳转失败-错误地址为" + err_borrow_url)

