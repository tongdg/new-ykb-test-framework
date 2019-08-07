# -*- coding: utf-8 -*-
#create by Zhangfukai date:2019 6/20
from config.zfk_config import Travle_dictionaries
from pages.pc_pages.zfk_Travelapplication_page import Travelapplication_Page

import datetime
class Borrowingapplication_Page(Travelapplication_Page):
 #借款申请单内所需要操作的元素:
    #         申请日期     Applyfor
    #      借款申请单号     Submint_number
    #         借款金额     Loan_Amounts
    #         借款事由     Loan_reason
    #         提交审批     Submit_examine
    #         审批领导     Approval_lead
    #      确定提交按钮     Submint_sure
    #         上传附件     Postattachperm
    #            保存     Save_button
    #            打印     Print_button
    #切换句柄，定位到云快报首页
    def Gain_index(self):
            Gain_index=Travelapplication_Page.Gain_index()
    #利用接口跳转，跳转到借款申请单
    def Borrow_order_url(self):
        self.driver.get(Travle_dictionaries().get("借款申请单"))
        Get_url = Travle_dictionaries().get("借款申请单")
        print(Get_url)
        if Get_url == "http://test.pc.51ykb.com/Form/FormViewer/BTAForm":
            self.log.info("出差申请单跳转成功")
            return True
        else:
            self.log.info("出差申请单跳转失败")
            return False

    #借款金额
    def Loan_Amounts(self):
        self.send_keys(
            self.find_element_by_class_name_ykb(
                "#tbinfo > tbody > tr.row-1 > td.td-amount.cell-value > input",
                '500'
            )
        )
    #借款事由
    def Loan_reason(self):
        # 获取当前提单日期
        date = str(
            datetime.datetime.now().strftime(
                '%Y-%m-%d'
            )
        )
        self.send_keys(self.find_element_by_css_ykb("#tb > tbody > tr.row-3 > td.cell-value > textarea"),
                       '企业微信自动化测试-借款申请单-测试提单日期:"' + date + '"')
    #提交审批
    def Submit_examine(self):
        self.click(
            self.find_element_by_class_name_ykb("#fixedFoot > button.eui-btn.eui-btn-blue.btn-commit")
        )
    #确定提交按钮
    def Submint_sure(self):
        self.click(
            self.find_element_by_class_name_ykb(
                "#mainform > div > div.e7cc-form-parts-footer-confirm > button.eui-btn.eui-btn-blue.btn-commit-confirm"
            )
        )





