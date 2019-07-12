#后台管理模块
import time
from pages.pc_pages.zfk_login_HouTaipage import Login_HouTaiPage
from config import zfk_config
import sys
class Valet_orderPage(Login_HouTaiPage):
    # 订单管理
    @property
    def Order_Management(self):
        return self.find_element_by_id_ykb("menu-dingdan")
    # 代客下单
    @property
    def Order_Management_Valet_order(self):
        return  self.find_element_by_css_ykb("#menu-dingdan > dd > ul > li:nth-child(6) > a")
    # 代客下单搜索框
    @property
    def Valet_order_SearchText(self):
        return self.find_element_by_id_ykb("txtKewWords")
    # 代客下单搜索框查询按钮
    @property
    def Valet_order_btnSearchUserInfo(self):
        return self.find_element_by_id_ykb("btnSearchUserInfo")

     #取出数组内对应字段的下标替换css样式内的child内的数字即可定位到正确的企业
    def Check_BusinessName(self):
        get_business="童小郭注册企业"
        get_business_All=self.find_elements_by_xpath('//*[@id="dataTableBody"]/tr/td[4]')
        #获取所有企业名称
        lists=[]
        print(str(get_business_All))
        for i in get_business_All:
            lists.append(i.text)
        print(lists)
        if get_business in lists:
            print("存在该企业")
            Businese_nameIndex=lists.index(get_business)+1
            self.click(
                self.find_element_by_css_ykb(
                    "#dataTableBody > tr:nth-child("'' + str(Businese_nameIndex) + ''") > td.f-14.td-manage > a:nth-child(2)")
            )
        #取出元素的下标
        else:
           sys.exit(0)
    # -------------------------------------Cut-Off Rule-----------------------------------------------------------
   #这里可以传入手机号及企业名称 后继的审批流程可在这里调用，这里拓展性很强
    def Chionce_enterprise(self):
        handle=self.current_window_handle()
        print("代客下单句柄:"+str(handle))
        self.driver.get(zfk_config.valet_orderUrl())
        time.sleep(2)
        self.send_keys(self.Valet_order_SearchText,'15353032451')
        time.sleep(2)
        self.click(self.Valet_order_btnSearchUserInfo)
        time.sleep(10)
        #进入筛选后的企业里
        self.Check_BusinessName()
        time.sleep(10)




