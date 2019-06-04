#后台管理模块
import time
from pages.base_page import BasePage
class Valet_orderPage(BasePage):
    # 订单管理
    @property
    def Order_Management(self):
        return (self.find_element_by_class_name_ykb("menu-list"))#订单管理
    @property
    def Order_Management_Valet_order(self):
        return  (self.find_element_by_link_text_ykb("AgentCreateOrder.html"))#代客下单
    @property
    def Valet_order_SearchText(self):
        return (self.find_element_by_id_ykb("txtKewWords"))#代客下单搜索框
    @property
    def Valet_order_btnSearchUserInfo(self):
        return (self.find_element_by_id_ykb("btnSearchUserInfo"))#代客下单搜索框查询按钮

    # -------------------------------------Cut-Off Rule-----------------------------------------------------------
   #这里可以传入手机号及企业名称 后继的审批流程可在这里调用，这里拓展性很强
    def Chionce_enterprise(self):
        self.click(self.Order_Management)
        time.sleep(1)
        self.click(self.Order_Management_Valet_order)
        time.sleep(1)
        self.send_keys(self.Valet_order_SearchText,'15353032451')
        self.click(self.Valet_order_btnSearchUserInfo)
