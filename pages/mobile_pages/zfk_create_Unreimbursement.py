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

    #跳转至未报销
    def UnReimbursement(self):
        time.sleep(3)
        # 进入未报销页面
        self.click(
            self.find_element_by_css_ykb(
                "#guo > div.main.scroller > div > div.ykb_content > div.ykb_main_content > div.ykb_home_wrap > div.ykb_banner > p:nth-child(1)"
            )
        )
        # 正确未报销的URL地址
        UnReimbursement_True = "static/expenses/anyRecord.html"
        # 获取当前跳转页面的URL
        UnReimbursement_url = self.current_url()
        if UnReimbursement_True in UnReimbursement_url:
            time.sleep(2)
            self.log.info("首页“”-未报销页面跳转成功")
            time.sleep(2)
            return True
        else:
            time.sleep(2)
            self.log.info("首页-未报销-地址错误")
            return False
    #全选删除
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
    #单笔删除(默认删除第一条)
    def Only_delete(self):
     #选择复选框
         time.sleep(1)
         self.click(self.find_element_by_css_ykb("#record_list > div > dd > div > div.hasSquareCheckbox"))
         time.sleep(1)
         #点击删除
         self.click(self.find_element_by_css_ykb("#item1mobile > div:nth-child(2) > div.fixBotm > div:nth-child(2) > button:nth-child(1)"))
         #点击确定
         self.click(self.find_element_by_css_ykb("#vbody > div.mui-popup.mui-popup-in > div.mui-popup-buttons > span.mui-popup-button.mui-popup-button-bold"))
    #差旅报销单返回
    def travel_back(self):
        # 点击返回键
        time.sleep(2)
        self.click(self.find_element_by_css_ykb("#app > div > div.mui-navbar > div > button > span"))
        time.sleep(2)
        self.click(self.find_element_by_css_ykb(
            "#vbody > div.mui-popup.mui-popup-in > div.mui-popup-buttons > span.mui-popup-button.mui-popup-button-bold"))
    #费用报销单返回
    def cost_back(self):
        # 点击返回键
        time.sleep(2)
        self.click(self.find_element_by_css_ykb("#app > div > div.mui-navbar > div > button > span"))
        time.sleep(2)
        self.click(self.find_element_by_css_ykb(
            "#vbody > div.mui-popup.mui-popup-in > div.mui-popup-buttons > span.mui-popup-button.mui-popup-button-bold"))
    #单笔提交差旅(默认提交第一条)
    def Only_submit_travel(self):
         time.sleep(1)
         self.click(self.find_element_by_css_ykb("#record_list > div > dd > div > div.hasSquareCheckbox"))
         time.sleep(1)
         self.click(self.find_element_by_css_ykb("#item1mobile > div:nth-child(2) > div.fixBotm > div:nth-child(2) > button.mui-btnew.mui-btn-theme"))
         time.sleep(1)
         self.click(self.find_element_by_css_ykb("#chooseWhat > ul > li:nth-child(1)"))
    # 单笔提交费用(默认提交第一条)
    def Only_submit_cost(self):
        # 选择复选框
        time.sleep(2)
        self.click(self.find_element_by_css_ykb("#record_list > div > dd > div > div.hasSquareCheckbox"))
        time.sleep(2)
        # 点击提交报销
        self.click(self.find_element_by_css_ykb(
            "#item1mobile > div:nth-child(2) > div.fixBotm > div:nth-child(2) > button.mui-btnew.mui-btn-theme"))
        time.sleep(2)
        self.click(self.find_element_by_css_ykb("#chooseWhat > ul > li:nth-child(2)"))
    #全选提交差旅
    def All_submit_travel(self):
         time.sleep(1)
         self.click(self.find_element_by_css_ykb("#item1mobile > div:nth-child(2) > div.fixBotm > div.fixChoose > div.squareChoose"))
         time.sleep(1)
         #点击提交报销
         self.click(self.find_element_by_css_ykb("#item1mobile > div:nth-child(2) > div.fixBotm > div:nth-child(2) > button.mui-btnew.mui-btn-theme"))
         time.sleep(1)
         self.click(self.find_element_by_css_ykb("#chooseWhat > ul > li:nth-child(1)"))
    #全选提交费用
    def All_submit_cost(self):
         time.sleep(1)
         self.click(self.find_element_by_css_ykb("#item1mobile > div:nth-child(2) > div.fixBotm > div.fixChoose > div.squareChoose"))
         time.sleep(1)
         #点击提交报销
         self.click(self.find_element_by_css_ykb("#item1mobile > div:nth-child(2) > div.fixBotm > div:nth-child(2) > button.mui-btnew.mui-btn-theme"))
         time.sleep(1)
         self.click(self.find_element_by_css_ykb("#chooseWhat > ul > li:nth-child(2)"))
    #单笔提单至费用报销单
    def Only_submit_Cost(self):
        time.sleep(2)
        order_num = self.find_elements_by_xpath('//*[@id="record_list"]/div/dd/div/div[2]/span[2]')
        self.log.info("当前列表存在消费记录个数为:" + str(len(order_num)))
        if len(order_num) >0:
            time.sleep(1)
            self.Only_submit_cost()
            time.sleep(2)
            cost_url = self.current_url()
            cost_true_url = "static/expenses/ReiFormNew.html"
            if cost_true_url in cost_url:
                self.log.info("[--未报销-消费记录列表-单笔-提单至费用报销单用例成功--]")
                self.cost_back()
                return True
            else:
                self.log.info("错误差旅报销单地址为" + cost_url)
                self.log.info("[--未报销-消费记录列表-单笔-提单至费用报销单跳转失败--]")
        else:
            self.log.info("“[--未报销”“-消费记录列表:暂无消费记录-开始执行创建消费记录用例--]")
            self.circulation_list()
            time.sleep(1)
            self.Only_submit_cost()
            time.sleep(2)
            cost_url = self.current_url()
            cost_true_url = "static/expenses/ReiFormNew.html"
            if cost_true_url in cost_url:
                self.log.info("[--未报销-消费记录列表-单笔-提单至费用报销单用例成功--]")
                self.cost_back()
                return True
            else:
                self.log.info("错误费用销单地址为" + cost_url)
                self.log.info("[--未报销-消费记录列表-单笔-提单至费用报销单跳转失败--]")
    #单笔提交_差旅报销单
    def Only_submit_Travel(self):
        time.sleep(2)
        order_num = self.find_elements_by_xpath('//*[@id="record_list"]/div/dd/div/div[2]/span[2]')
        self.log.info("当前列表存在消费记录个数为:" + str(len(order_num)))
        if len(order_num)>0:
            time.sleep(2)
            self.Only_submit_travel()
            time.sleep(2)
            Travel_url = self.current_url()
            Traver_true_url = "static/expenses/TraFormNew.html"
            if Traver_true_url in Travel_url:
                self.log.info("[--未报销-消费记录列表-单笔-提单至差旅报销单用例成功--]")
                time.sleep(2)
                self.travel_back()
                return True
            else:
                self.log.info("错误差旅报销单地址为" + Travel_url)
                self.log.info("[--未报销-消费记录列表-单笔-提单至差旅报销单跳转失败--]")
        else:
            self.log.info("“[--未报销”“-消费记录列表:暂无消费记录-开始执行创建消费记录用例--]")
            self.circulation_list()
            time.sleep(1)
            self.Only_submit_travel()
            time.sleep(2)
            Travel_url = self.current_url()
            Traver_true_url = "static/expenses/TraFormNew.html"
            if Traver_true_url in Travel_url:
                self.log.info("[--未报销-消费记录列表-单笔-提单至差旅报销单用例成功--]")
                self.travel_back()
                return True
            self.log.info("错误差旅报销单地址为" + Travel_url)
            self.log.info("[--未报销-消费记录列表-单笔-提单至差旅报销单跳转失败--]")
            return False
    #全选提交至差旅
    def All_Submit_Travel(self):
        time.sleep(2)
        order_num = self.find_elements_by_xpath('//*[@id="record_list"]/div/dd/div/div[2]/span[2]')
        self.log.info("当前列表存在消费记录个数为:" + str(len(order_num)))
        if len(order_num) > 0:
            time.sleep(1)
            self.All_submit_travel()
            time.sleep(2)
            Travel_url = self.current_url()
            Traver_true_url = "static/expenses/TraFormNew.html"
            if Traver_true_url in Travel_url:
                self.log.info("[--未报销-消费记录列表-全选提单至差旅报销单用例成功--]")
                self.travel_back()
                return True
            else:
                self.log.info("错误差旅报销单地址为" + Travel_url)
                self.log.info("[--未报销-消费记录列表-全选提单至差旅报销单跳转失败--]")
        else:
            self.circulation_list()
            time.sleep(1)
            self.Only_submit_travel()
            time.sleep(2)
            Travel_url = self.current_url()
            Traver_true_url = "static/expenses/TraFormNew.html"
            if Traver_true_url in Travel_url:
                self.log.info("[--未报销-消费记录列表-单笔-提单至差旅报销单用例成功--]")
                self.travel_back()
                return True
            self.log.info("错误差旅报销单地址为" + Travel_url)
            self.log.info("[--未报销-消费记录列表-单笔-提单至差旅报销单跳转失败--]")
            return False
    #全选提交-费用报销单
    def All_Submit_Cost(self):
        time.sleep(3)
        order_num = self.find_elements_by_xpath('//*[@id="record_list"]/div/dd/div/div[2]/span[2]')
        self.log.info("当前列表存在消费记录个数为:" + str(len(order_num)))
        if len(order_num) > 0:
            time.sleep(1)
            self.All_submit_cost()
            time.sleep(2)
            cost_url = self.current_url()
            cost_true_url = "static/expenses/ReiFormNew.html"
            if cost_true_url in cost_url:
                self.log.info("[--未报销-消费记录列表-全选提单至费用报销单用例成功--]")
                self.travel_back()
                return True
            else:
                self.log.info("错误差旅报销单地址为" + cost_url)
                self.log.info("[--未报销-消费记录列表-全选提单至费用报销单跳转失败--]")
                return False
        else:
            self.log.info("[--未报销-消费记录列表-当前列表无消费记录-开始执行创建消费用例--]")
            time.sleep(1)
            self.circulation_list()
            time.sleep(2)
            self.All_submit_cost()
            time.sleep(2)
            cost_url = self.current_url()
            cost_true_url = "static/expenses/ReiFormNew.html"
            if cost_true_url in cost_url:
                self.log.info("[--未报销-消费记录列表-全选提单至费用报销单用例成功--]")
                self.travel_back()
                return True
            else:
                self.log.info("错误差旅报销单地址为" + cost_url)
                self.log.info("[--未报销-消费记录列表-全选提单至费用报销单跳转失败--]")
                return False

    #公共的出发地
    #点击记一笔,并且选择一个消费类型
    def click_paning(self):
        time.sleep(5)
        self.click(self.find_element_by_css_ykb("#anyRecordList > div > div.paning"))
    #选择消费类型
    def taxiIcon(self):
        time.sleep(5)
        self.click(self.find_element_by_id_ykb('taxiIcon'))
    #日期
    def Choince_Date(self):
        time.sleep(3)
        self.click(self.find_element_by_id_ykb("setOutDate"))
        time.sleep(2)
        self.click(self.find_element_by_css_ykb("#calendar > div:nth-child(1) > ul > li.dl.jr.cur"))
        time.sleep(1)
    #起点
    def Begin_address(self):
        time.sleep(1)
        self.send_keys(self.find_element_by_css_ykb("#fromPlace"),'测试起点')
    #终点
    def End_address(self):
        time.sleep(1)
        self.send_keys(self.find_element_by_css_ykb("#toPlace"),'测试终点')
    #打车费
    def By_car_cost(self):
        self.click(self.find_element_by_css_ykb("#calculator > ul.mui-table-view.noTB.anyrecord_g_wrap > li:nth-child(7) > span.span-lab.mui-text-right.clac3.firstShow"))
        time.sleep(1)
        self.click(self.find_element_by_css_ykb("#keybord > span:nth-child(7)"))
        time.sleep(1)
        self.click(self.find_element_by_css_ykb("#submitNumCal"))
    #其他
    def Onther(self):
        time.sleep(1)
        self.click(self.find_element_by_css_ykb("#calculator > ul.mui-table-view.noTB.anyrecord_g_wrap > li:nth-child(10) > table > tbody > tr > td.span-lab.mui-text-right.c3.ft14"))
        time.sleep(1)
        self.click(self.find_element_by_css_ykb("#keybord > span:nth-child(7)"))
        self.click(self.find_element_by_css_ykb("#submitNumCal"))
    #说明
    def explain(self):
        time.sleep(1)
        self.send_keys(self.find_element_by_css_ykb("#remarkMsg"),"测试说明")
        time.sleep(1)
    #完成
    def click_fulfill(self):
        time.sleep(2)
        self.click(self.find_element_by_css_ykb("#setting > div.mui-bar.mui-bar-tab.ab > button.mui-btn.themebgStyle.themeBtn17ab"))
    #再记一笔按钮
    def click_Again_write_button(self):
        time.sleep(1)
        self.click(self.find_element_by_css_ykb("#setting > div.mui-bar.mui-bar-tab.ab > button.mui-btn.themebgStyle.mui-pull-right.themeBtn089a"))
    #记一笔返回按钮
    def write_back(self):
        time.sleep(1)
        self.click(self.find_element_by_css_ykb("#app > div > div.mui-navbar > div > button > span"))

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
        self.Choince_Date()
        self.Begin_address()
        self.End_address()
        self.By_car_cost()
        self.Onther()
        self.explain()
        time.sleep(1)
        self.click_Again_write_button()
        self.Choince_Date()
        self.Begin_address()
        self.End_address()
        self.By_car_cost()
        self.Onther()
        self.explain()
        self.click_fulfill()
        time.sleep(1)

#删除-全选删除
    def UnReim_Remember_whit_Delete(self):
        time.sleep(2)
        order_num = self.find_elements_by_xpath('//*[@id="record_list"]/div/dd/div/div[2]/span[2]')
        self.log.info("当前列表存在消费记录个数为:"+str(len(order_num)))
        #判断消费列表是否为空
        if len(order_num)>0:
            time.sleep(1)
            #全选删除
            self.All_delete()
            time.sleep(3)
            order_num2 = self.find_elements_by_xpath('//*[@id="record_list"]/div/dd/div/div[2]/span[2]')
            self.log.info("当前列表存在消费记录个数为:" + str(len(order_num2)))
            #如果删除成功的话列表为空，若不为空则全选删除失败
            if len(order_num2)==0:
                self.log.info('[--未报销”“-消费记录列表：全选删除用例成功--]')
                return True
            #如果删除成功的话列表为空，若不为空则全选删除失败
            else:
                self.log.info('[--未报销”“-消费记录列表：全选删除用例失败--]')
                return False
        else:
            self.log.info("“[--未报销”“-消费记录列表:暂无消费记录-开始执行创建消费记录用例--]")
            self.circulation_list()
            time.sleep(1)
            order_num = self.find_elements_by_xpath('//*[@id="record_list"]/div/dd/div/div[2]/span[2]')
            self.log.info("当前列表存在消费记录个数为:" + str(len(order_num)))
            self.All_delete()
            time.sleep(3)
            order_num2 = self.find_elements_by_xpath('//*[@id="record_list"]/div/dd/div/div[2]/span[2]')
            self.log.info("当前列表存在消费记录个数为:" + str(len(order_num2)))
            time.sleep(1)
            if len(order_num2)==0:
                self.log.info('[--未报销”“-消费记录列表：全选删除用例成功--]')
                return True
                # 如果删除成功的话列表为空，若不为空则全选删除失败
            else:
                self.log.info('[--未报销”“-消费记录列表：全选删除用例失败--]')
                return False
#删除-单笔删除
    def UnReim_Remember_whit_Only_Delete(self):
        time.sleep(2)
        order_num = self.find_elements_by_xpath('//*[@id="record_list"]/div/dd/div/div[2]/span[2]')
        self.log.info("当前列表存在消费记录个数为:" + str(len(order_num)))
        # 判断消费列表是否为空
        if len(order_num) > 0:
            time.sleep(1)
            # 全选删除
            self.Only_delete()
            time.sleep(1)
            order_num2 = self.find_elements_by_xpath('//*[@id="record_list"]/div/dd/div/div[2]/span[2]')
            self.log.info("当前列表存在消费记录个数为:" + str(len(order_num2)))
            # 如果删除成功的话列表为空，若不为空则全选删除失败
            if len(order_num)-len(order_num2) == 1 or len(order_num)-len(order_num2)==0:
                self.log.info('[--未报销”“-消费记录列表：单选删除用例成功--]')
                return True
            # 如果删除成功的话列表为空，若不为空则全选删除失败
            else:
                self.log.info('[--未报销”“-消费记录列表：单选删除用例失败--]')
                return False
        else:
            self.log.info("“[--未报销”“-消费记录列表:暂无消费记录-开始执行创建消费记录用例--]")
            self.circulation_list()
            time.sleep(1)
            order_num = self.find_elements_by_xpath('//*[@id="record_list"]/div/dd/div/div[2]/span[2]')
            self.log.info("当前列表存在消费记录个数为:" + str(len(order_num)))
            self.Only_delete()
            time.sleep(3)
            order_num2 = self.find_elements_by_xpath('//*[@id="record_list"]/div/dd/div/div[2]/span[2]')
            self.log.info("当前列表存在消费记录个数为:" + str(len(order_num2)))
            time.sleep(1)
            if len(order_num)-len(order_num2) == 1 or len(order_num)-len(order_num2)==0:
                time.sleep(1)
                self.log.info('[--未报销”“-消费记录列表：单选选删除用例成功--]')
                return True
                # 如果删除成功的话列表为空，若不为空则全选删除失败
            else:
                self.log.info('[--未报销”“-消费记录列表：单选删除用例失败--]')
                return False














# #提交-单笔提交，多笔提交（差旅报销单）
#     def UnReim_Remember_whit_Submit_Travel(self):
#         # 判断消费列表是否为空
#         Record_list = self.find_element_by_css_ykb("#record_list > div > dd", 3)
#         # 若找到返回的值肯定是True
#         if Record_list is not False:
#             #全选提交
#             time.sleep(2)
#             self.All_Submit_travel()
#             print("“未报销”“-消费记录列表：全选提交至差旅报销单成功")
#             self.circulation_list()
#             time.sleep(3)
#             self.UnReimbursement()
#             time.sleep(2)
#             self.Only_submit_travel()
#             print("未报销-消费记录-单笔提单至差旅报销单成功")
#         else:
#             self.circulation_list()
#             # 全选提交
#             time.sleep(3)
#             self.All_Submit_travel()
#             print("“未报销”“-消费记录列表：全选提交至差旅报销单成功")
#             self.circulation_list()
#             # 提交单笔消费记录
#             self.Only_submit_travel()
#             print("未报销-消费记录-单笔提单至差旅报销单成功")
#
# # 提交-单笔提交，多笔提交（费用报销单）
#     def UnReim_Remember_whit_Submit_Cost(self):
#          # 判断消费列表是否为空
#          Record_list = self.find_element_by_css_ykb("#record_list > div > dd", 3)
#          # 若找到返回的值肯定是True
#          if Record_list is not False:
#              #全选提交
#              time.sleep(2)
#              self.All_Submit_cost()
#              print("未报销-消费记录列表：全选提交至费用报销单成功")
#              time.sleep(3)
#              self.circulation_list()
#              time.sleep(5)
#              self.UnReimbursement()
#              time.sleep(5)
#              self.Only_Submit_cost()
#              print("未报销-消费记录-单笔提单至费用报销单成功")
#              time.sleep(3)
#          else:
#              # 全选提交
#              time.sleep(3)
#              self.circulation_list()
#              self.All_Submit_cost()
#              print("“未报销”“-消费记录列表：全选提交至费用报销单成功")
#              self.circulation_list()
#              self.UnReimbursement()
#              # 删除新建的单笔消费记录
#              self.Only_Submit_cost()
#              print("未报销-消费记录-单笔提单至费用报销单成功")
#              time.sleep(3)



