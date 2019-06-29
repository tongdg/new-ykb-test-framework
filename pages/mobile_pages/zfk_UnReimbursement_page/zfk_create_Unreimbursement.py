from pages.mobile_pages.zfk_mobile_index_page import zfk_Mobile_index_page
import time
class zfk_create_Unreimbursement(zfk_Mobile_index_page):
#记一笔需要定位的元素
    #记一笔     Remember_whit
    #未报销     UnReimbursement
    #全选按钮    All_choince_button
    #删除按钮    Delete_Button
    #弹出页面的取消以及确定按钮  Choince_button
    #提交报销按钮  Submint_button
    #暂时定义一个其他费用可以同时提交到两张单据的消费类型
#确定未报销功能完成
#报销内公共
#1.全选删除
    def All_delete(self):
        # 勾选全选按钮
        self.click(self.find_element_by_css_ykb(
            "#item1mobile > div:nth-child(2) > div.fixBotm > div.fixChoose > div.squareChoose"))
        time.sleep(3)
        # 点击删除按钮
        self.click(self.find_element_by_css_ykb(
            "#item1mobile > div:nth-child(2) > div.fixBotm > div:nth-child(2) > button:nth-child(1)"))
        time.sleep(3)
        self.click(self.find_element_by_css_ykb(
            "#vbody > div.mui-popup.mui-popup-in > div.mui-popup-buttons > span:nth-child(2)"))
    #单笔删除
    #默认删除第一条
    def Only_delete(self):
        #点击一笔的复选框
        self.click(self.find_element_by_xpath('//*[@id="record_list"]/div/dd/div/div[1]'))

    #单笔提交_差旅报销单
    def Only_submit_travel(self):
     #选择复选框
     time.sleep(2)
     self.click(self.find_element_by_css_ykb("#record_list > div > dd > div > div.hasSquareCheckbox"))
     #提交审批按钮
     time.sleep(2)
     self.click(self.find_element_by_css_ykb("#item1mobile > div:nth-child(2) > div.fixBotm > div:nth-child(2) > button.mui-btnew.mui-btn-theme"))
     #提交至差旅
     self.click(self.find_element_by_css_ykb("#chooseWhat > ul > li:nth-child(1)"))
     time.sleep(2)
     # 添加行程说明
     self.send_keys(self.find_element_by_css_ykb(
         "#traForm > div > div.mui-scroll-wrapper.bottom50 > div.mui-scroll > div:nth-child(3) > ul > li.mui-table-view-cell.xcsmwc > textarea"),
         '测试行程说明')
     # 提交审批按钮
     self.click(self.find_element_by_css_ykb("#commitBtr"))
     time.sleep(2)
     # 确定按钮
     self.click(self.find_element_by_css_ykb("#leader > div > div.mui-bar.mui-bar-tab.hasBLine.ab.spryanxs > button"))
     time.sleep(2)

    #全选提交-差旅报销单
    def All_Submit_travel(self):
        # 勾选全选按钮
        time.sleep(2)
        self.click(self.find_element_by_css_ykb(
            "#item1mobile > div:nth-child(2) > div.fixBotm > div.fixChoose > div.squareChoose"))
        #点击提交报销按钮
        time.sleep(2)
        self.click(self.find_element_by_css_ykb(
            "#item1mobile > div:nth-child(2) > div.fixBotm > div:nth-child(2) > button:nth-child(2)"))
        Travel_url = "http://test.m.51ykb.com/static/expenses/TraFormNew.html?anyFirst=true"
        #提交至差旅
        time.sleep(2)
        self.click(self.find_element_by_css_ykb("#chooseWhat > ul > li:nth-child(1)"))
        Trav_test_url = self.current_url()
        print("当前测试环节差旅报销单URL地址"+Trav_test_url)
        if Trav_test_url == Travel_url:
            print("未报销-消费记录列表-全选-提单至差旅报销单成功")
        time.sleep(3)
        self.send_keys(self.find_element_by_css_ykb("#traForm > div > div.mui-scroll-wrapper.bottom50 > div.mui-scroll > div:nth-child(3) > ul > li.mui-table-view-cell.xcsmwc > textarea"),"测试行程说明")
        #提交审批按钮
        self.click(self.find_element_by_css_ykb("#commitBtr"))
        time.sleep(3)
        #确定按钮
        self.click(self.find_element_by_css_ykb("#leader > div > div.mui-bar.mui-bar-tab.hasBLine.ab.spryanxs > button"))
        time.sleep(3)
        #返回成功
        # time.sleep(2)
        # self.click(self.find_element_by_css_ykb("#app > div > div.mui-navbar > div > button > span"))
        # time.sleep(1)
        # self.click(self.find_element_by_css_ykb("#vbody > div.mui-popup.mui-popup-in > div.mui-popup-buttons > span.mui-popup-button.mui-popup-button-bold"))


    #单笔提交至费用报销单
    def Only_Submit_cost(self):
        # 选择复选框
        time.sleep(2)
        self.click(self.find_element_by_css_ykb("#record_list > div > dd > div > div.hasSquareCheckbox"))
        # 提交审批按钮
        time.sleep(2)
        self.click(self.find_element_by_css_ykb(
            "#item1mobile > div:nth-child(2) > div.fixBotm > div:nth-child(2) > button.mui-btnew.mui-btn-theme"))
        # 提交至费用报销单
        time.sleep(2)
        self.click(self.find_element_by_css_ykb("#chooseWhat > ul > li:nth-child(2)"))
        cost_url = "http://test.m.51ykb.com/static/expenses/ReiFormNew.html?anyFirst=true"
        cost_test_url = self.current_url()
        print("当前测试环节差旅报销单URL地址" + cost_url)
        if cost_test_url == cost_url:
            print("未报销-消费记录列表-全选-提单至费用销单成功")
        time.sleep(3)
        self.click(self.find_element_by_css_ykb("#commitBtr"))
        time.sleep(2)
        self.click(self.find_element_by_css_ykb("#leader > div > div.mui-bar.mui-bar-tab.hasBLine.ab.spryanxs > button"))
        time.sleep(2)

    #全选提交-费用报销单
    def All_Submit_cost(self):
        # 勾选全选按钮
        self.click(self.find_element_by_css_ykb(
            "#item1mobile > div:nth-child(2) > div.fixBotm > div.fixChoose > div.squareChoose"))
        time.sleep(2)
        # 点击提交报销按钮
        self.click(self.find_element_by_css_ykb(
            "#item1mobile > div:nth-child(2) > div.fixBotm > div:nth-child(2) > button:nth-child(2)"))
        time.sleep(2)
        self.click(self.find_element_by_css_ykb("#chooseWhat > ul > li:nth-child(2)"))
        cost_url = "http://test.m.51ykb.com/static/expenses/ReiFormNew.html?anyFirst=true"
        cost_test_url = self.current_url()
        print("当前测试环节差旅报销单URL地址" + cost_url)
        if cost_test_url == cost_url:
            print("未报销-消费记录列表-全选-提单至费用销单成功")
        time.sleep(3)
        self.click(self.find_element_by_css_ykb("#commitBtr"))
        time.sleep(3)
        self.click(self.find_element_by_css_ykb("#leader > div > div.mui-bar.mui-bar-tab.hasBLine.ab.spryanxs > button"))
        time.sleep(2)


#record_list > div > dd > div > div.hasSquareCheckbox
    #单笔删除
    def Only_delete(self):
        #选择复选框
     self.click(self.find_element_by_css_ykb("#record_list > div > dd > div > div.hasSquareCheckbox"))
     time.sleep(3)
        #点击删除
     self.click(self.find_element_by_css_ykb("#item1mobile > div:nth-child(2) > div.fixBotm > div:nth-child(2) > button:nth-child(1)"))
        #点击确定
     self.click(self.find_element_by_css_ykb("#vbody > div.mui-popup.mui-popup-in > div.mui-popup-buttons > span.mui-popup-button.mui-popup-button-bold"))


    #公共的出发地
    #点击记一笔,并且选择一个消费类型
    def click_paning(self):
        time.sleep(2)
        self.click(self.find_element_by_css_ykb("#anyRecordList > div > div.paning"))
    #选择消费类型
    def taxiIcon(self):
        time.sleep(3)
        return self.click(self.find_element_by_css_ykb("#taxiIcon"))
    #日期
    def Choince_Date(self):
        time.sleep(2)
        self.click(self.find_element_by_id_ykb("setOutDate"))
        time.sleep(2)
        self.click(self.find_element_by_css_ykb("#calendar > div:nth-child(1) > ul > li.dl.jr.cur"))
        time.sleep(1)
    #起点
    def Begin_address(self):
        time.sleep(2)
        self.send_keys(self.find_element_by_css_ykb("#fromPlace"),'测试起点')
    #终点
    def End_address(self):
        time.sleep(2)
        self.send_keys(self.find_element_by_css_ykb("#toPlace"),'测试终点')
    #打车费
    def By_car_cost(self):
        self.click(self.find_element_by_css_ykb("#calculator > ul.mui-table-view.noTB.anyrecord_g_wrap > li:nth-child(7) > span.span-lab.mui-text-right.clac3.firstShow"))
        time.sleep(2)
        self.click(self.find_element_by_css_ykb("#keybord > span:nth-child(7)"))
        self.click(self.find_element_by_css_ykb("#submitNumCal"))
    #其他
    def Onther(self):
        time.sleep(2)
        self.click(self.find_element_by_css_ykb("#calculator > ul.mui-table-view.noTB.anyrecord_g_wrap > li:nth-child(10) > table > tbody > tr > td.span-lab.mui-text-right.c3.ft14"))
        time.sleep(2)
        self.click(self.find_element_by_css_ykb("#keybord > span:nth-child(7)"))
        self.click(self.find_element_by_css_ykb("#submitNumCal"))
    #说明
    def explain(self):
        time.sleep(2)
        self.send_keys(self.find_element_by_css_ykb("#remarkMsg"),"测试说明")
    #完成
    def click_fulfill(self):
        time.sleep(2)
        self.click(self.find_element_by_css_ykb("#setting > div.mui-bar.mui-bar-tab.ab > button.mui-btn.themebgStyle.themeBtn17ab"))
    #再记一笔按钮
    def click_Again_write_button(self):
        return self.click(self.find_element_by_css_ykb("#setting > div.mui-bar.mui-bar-tab.ab > button.mui-btn.themebgStyle.mui-pull-right.themeBtn089a"))


#7. 循环造消费记录
    def circulation_list(self):
        self.click_paning()
        self.taxiIcon()
        self.Choince_Date()
        self.Begin_address()
        self.End_address()
        self.By_car_cost()
        self.Onther()
        self.explain()
        self.click_Again_write_button()
        self.click_Again_write()
        time.sleep(3)
    #再记一笔
    def click_Again_write(self):
        time.sleep(2)
        self.Choince_Date()
        self.Begin_address()
        self.End_address()
        self.By_car_cost()
        self.Onther()
        self.explain()
        self.click_Again_write_button()
        self.Choince_Date()
        self.Begin_address()
        self.End_address()
        self.By_car_cost()
        self.Onther()
        self.explain()
        self.click_fulfill()

#删除-单笔删除 多笔删除
    def UnReim_Remember_whit_Delete(self):
        # 判断消费列表是否为空
        Record_list = self.find_element_by_css_ykb("#record_list > div > dd",3)
        # 若找到返回的值肯定是True
        if Record_list is not False:
            #全选删除
            time.sleep(3)
            self.All_delete()
            print("“未报销”“-消费记录列表：全选删除成功")
            #新建消费记录
            self.circulation_list()
            print("未报销-消费记录列表：新建消费记录成功")
            #删除新建的单笔消费记录
            self.Only_delete()
            print("未报销-单笔消费记录删除成功")
            print("未报销-消费记录删除测试结束")
        else:
            self.circulation_list()
            self.Only_delete()
#提交-单笔提交，多笔提交（差旅报销单）
    def UnReim_Remember_whit_Submit_Travel(self):
        # 判断消费列表是否为空
        Record_list = self.find_element_by_css_ykb("#record_list > div > dd", 3)
        # 若找到返回的值肯定是True
        if Record_list is not False:
            #全选提交
            time.sleep(2)
            self.All_Submit_travel()
            print("“未报销”“-消费记录列表：全选提交至差旅报销单成功")
            self.circulation_list()
            time.sleep(5)
            self.UnReimbursement
            self.Only_submit_travel()
            print("未报销-消费记录-单笔提单至差旅报销单成功")
        else:
            self.circulation_list()
            # 全选提交
            time.sleep(3)
            self.All_Submit_travel()
            print("“未报销”“-消费记录列表：全选提交至差旅报销单成功")
            self.circulation_list()
            # 删除新建的单笔消费记录
            self.Only_submit_travel()
            print("未报销-消费记录-单笔提单至差旅报销单成功")

# 提交-单笔提交，多笔提交（费用报销单）
    def UnReim_Remember_whit_Submit_Cost(self):
         # 判断消费列表是否为空
         Record_list = self.find_element_by_css_ykb("#record_list > div > dd", 3)
         # 若找到返回的值肯定是True
         if Record_list is not False:
             # 全选提交
             time.sleep(2)
             self.All_Submit_cost()
             print("未报销-消费记录列表：全选提交至费用报销单成功")
             time.sleep(3)
             self.circulation_list()
             time.sleep(5)
             self.UnReimbursement
             time.sleep(2)
             self.Only_Submit_cost()
             print("未报销-消费记录-单笔提单至费用报销单成功")
         else:
             # 全选提交
             time.sleep(3)
             self.circulation_list()
             self.All_Submit_cost()
             print("“未报销”“-消费记录列表：全选提交至费用报销单成功")
             self.circulation_list()
             self.UnReimbursement
             # 删除新建的单笔消费记录
             self.Only_Submit_cost()
             print("未报销-消费记录-单笔提单至费用报销单成功")



