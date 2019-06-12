#后台管理模块
import time
from pages.pc_pages.zfk_login_HouTaipage import Login_HouTaiPage
from config import zfk_config
class Valet_orderPage(Login_HouTaiPage):
    # 订单管理
    @property
    def Order_Management(self):
        return self.find_element_by_id_ykb("menu-dingdan")#订单管理
    @property
    def Order_Management_Valet_order(self):
        return  self.find_element_by_css_ykb("#menu-dingdan > dd > ul > li:nth-child(6) > a")#代客下单
    @property
    def Valet_order_SearchText(self):
        return self.find_element_by_id_ykb("txtKewWords")#代客下单搜索框
    @property
    def Valet_order_btnSearchUserInfo(self):
        return self.find_element_by_id_ykb("btnSearchUserInfo")#代客下单搜索框查询按钮
    @property
    def Valet_order_Enterprise(self):
        return self.find_element_by_css_ykb("#dataTableBody > tr:nth-child(2) > td.f-14.td-manage > a:nth-child(2)")#PC端
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
        self.click(self.Valet_order_Enterprise)
        time.sleep(2)





