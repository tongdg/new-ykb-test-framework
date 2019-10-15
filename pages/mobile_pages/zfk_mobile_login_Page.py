#后台管理模块
import time
from pages.pc_pages.zfk_login_HouTaipage import Login_HouTaiPage
from config import zfk_config
import sys

from test_case.mobile.zfk.Approval_flow.test import highLightElement


class Mobile_login_page(Login_HouTaiPage):
    # 订单管理
    @property
    def Order_Management(self):
        return self.find_element_by_id_ykb("menu-dingdan")
    # 代客下单
    @property
    def Order_Management_Valet_order(self):
        return  self.find_element_by_css_ykb("#menu-dingdan > dd > ul > li:nth-child(6) > a")
    # 代客下单搜索框
    def Valet_order_SearchText(self):
        txtKewWords= self.find_element_by_id_ykb("txtKewWords")
        return txtKewWords
    # 代客下单搜索框查询按钮
    def Valet_order_btnSearchUserInfo(self):
        btnSearchUserInfo= self.find_element_by_id_ykb("btnSearchUserInfo")
        return btnSearchUserInfo

  #取出数组内对应字段的下标替换css样式内的child内的数字即可定位到正确的企业
    def Check_BusinessName(self):
        time.sleep(5)
        get_business="童小郭注册测试企业"
        get_business_All=self.driver.find_elements_by_xpath('//*[@id="dataTableBody"]/tr/td[4]')
        #获取所有企业名称
        lists=[]
        for i in get_business_All:
            lists.append(i.text)
        bussiness_index=lists.index('童小郭注册测试企业')
        time.sleep(2)
        self.find_element_by_xpath('//*[@id="dataTableBody"]/tr['+str(bussiness_index+1)+']/td[4]')
        time.sleep(2)
        if get_business in lists:
            print("存在该企业")
            Businese_nameIndex=lists.index(get_business)+1
            self.click(
                self.find_element_by_css_ykb(
                    "#dataTableBody > tr:nth-child("'' + str(Businese_nameIndex) + ''") > td.f-14.td-manage > a:nth-child(1)")
            )
        #取出元素的下标
        else:
           sys.exit(0)
    # 取出数组内对应字段的下标替换css样式内的child内的数字即可定位到正确的企业
    def Check_BusinessName_cashier(self):
            time.sleep(5)
            get_business = "童小郭注册测试企业"
            get_business_All = self.find_elements_by_xpath('//*[@id="dataTableBody"]/tr/td[4]')
            # 获取所有企业名称
            lists = []
            print(str(get_business_All))
            for i in get_business_All:
                lists.append(i.text)
            print(lists)
            if get_business in lists:
                print("存在该企业")
                Businese_nameIndex = lists.index(get_business) + 1
                self.click(
                    self.find_element_by_css_ykb(
                        "#dataTableBody > tr:nth-child("'' + str(
                            Businese_nameIndex) + ''") > td.f-14.td-manage > a:nth-child(2)")
                )
            # 取出元素的下标
            else:
                sys.exit(0)
   #------------------------------------------------------------
   #这里可以传入手机号及企业名称 后继的审批流程可在这里调用，这里拓展性很强
    #其他测试用例内使用角色
    def Choince_Login_god(self):
        time.sleep(2)
        handle = self.current_window_handle()
        print("代客下单句柄:" + str(handle))
        self.driver.get(zfk_config.valet_orderUrl())
        time.sleep(2)
        self.send_keys(self.Valet_order_SearchText(), '13148129351')
        time.sleep(1)
        self.click(self.Valet_order_btnSearchUserInfo())
        time.sleep(2)
        # 进入筛选后的企业里
        self.Check_BusinessName()
        handle = self.current_window_handle()
        handles = self.window_handles()
        print("云快报移动端-首页句柄" + handle)
        print(handles)
        for handle in handles:
            if handle != handles:
                self.driver.switch_to.window(handle)
        time.sleep(3)


    #普通员工-15353032451-张穷恺
    def Chionce_Login_staff(self):
        time.sleep(2)
        handle = self.current_window_handle()
        print("代客下单句柄:" + str(handle))
        self.driver.get(zfk_config.valet_orderUrl())
        time.sleep(2)
        self.send_keys(self.Valet_order_SearchText(),'15353032451')
        time.sleep(2)
        self.click(self.Valet_order_btnSearchUserInfo())
        time.sleep(2)
        # 进入筛选后的企业里
        self.Check_BusinessName()
        time.sleep(3)
        handle = self.current_window_handle()
        handles = self.window_handles()
        print("云快报移动端-首页句柄" + handle)
        print(handles)
        for handle in handles:
            if handle != handles:
                self.driver.switch_to.window(handle)
        time.sleep(3)
    #部门领导-13148129351-张富恺
    def Chionce_Login_leader(self):
        time.sleep(2)
        self.driver.get(zfk_config.valet_orderUrl())
        handle = self.current_window_handle()
        print("代客下单句柄:" + str(handle))
        time.sleep(2)
        self.send_keys(self.Valet_order_SearchText(), '13148129351')
        time.sleep(1)
        self.click(self.Valet_order_btnSearchUserInfo())
        # 进入筛选后的企业里
        self.Check_BusinessName()
        handle = self.current_window_handle()
        handles = self.window_handles()
        print("云快报移动端-首页句柄" + handle)
        print(handles)
        for handle in handles:
            if handle != handles:
                self.driver.switch_to.window(handle)
        time.sleep(3)
        self.log.info('审批领导登录-ok')
        time.sleep(2)

    #会计-15216625816-童定国
    def Chionce_Login_accountant(self):
        time.sleep(2)
        handle = self.current_window_handle()
        print("代客下单句柄:" + str(handle))
        self.driver.get(zfk_config.valet_orderUrl())
        time.sleep(2)
        self.send_keys(self.Valet_order_SearchText(), '15927555992')
        time.sleep(1)
        self.click(self.Valet_order_btnSearchUserInfo())
        # 进入筛选后的企业里
        self.Check_BusinessName()
        handle = self.current_window_handle()
        handles = self.window_handles()
        print("云快报移动端-首页句柄" + handle)
        print(handles)
        for handle in handles:
            if handle != handles:
                self.driver.switch_to.window(handle)
        time.sleep(3)

    #财务经理-13239177793-吕方方
    def Chionce_Login_manager(self):
        time.sleep(2)
        handle = self.current_window_handle()
        print("代客下单句柄:" + str(handle))
        self.driver.get(zfk_config.valet_orderUrl())
        time.sleep(2)
        self.send_keys(self.Valet_order_SearchText(), '13239177793')
        time.sleep(1)
        self.click(self.Valet_order_btnSearchUserInfo())
        # 进入筛选后的企业里
        self.Check_BusinessName()
        handle = self.current_window_handle()
        handles = self.window_handles()
        print("云快报移动端-首页句柄" + handle)
        print(handles)
        for handle in handles:
            if handle != handles:
                self.driver.switch_to.window(handle)
        time.sleep(3)
    #出纳付款-钱诚佳
    def Choince_login_cashier(self):
        time.sleep(2)
        handle = self.current_window_handle()
        print("代客下单句柄:" + str(handle))
        self.driver.get(zfk_config.valet_orderUrl())
        time.sleep(2)
        self.send_keys(self.Valet_order_SearchText(), '13818732929')
        time.sleep(1)
        self.click(self.Valet_order_btnSearchUserInfo())
        # 进入筛选后的企业里
        self.Check_BusinessName_cashier()
        handle = self.current_window_handle()
        handles = self.window_handles()
        print("云快报移动端-首页句柄" + handle)
        print(handles)
        for handle in handles:
            if handle != handles:
                self.driver.switch_to.window(handle)
        time.sleep(3)
    #获取手机端的的URL
    def Get_mobile_url(self):
         # 获取手机端的 url
         Mobile_url=self.current_url()
         Mobile_url1 = "Public/index.html"
         Mobile_url2 = "Mine/WechatIndex"
         if Mobile_url1 in Mobile_url:
           mobile_url=Mobile_url.replace(Mobile_url1,Mobile_url2)
           self.quit_chrom()
           return mobile_url

