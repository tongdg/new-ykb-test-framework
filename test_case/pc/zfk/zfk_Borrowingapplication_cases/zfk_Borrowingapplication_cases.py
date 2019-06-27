# 借款申请单测试用例
import unittest
from selenium import webdriver
from pages.pc_pages.zfk_Borrowingapplication_page import Borrowingapplication_Page


class Borrowing_Case(unittest.TestCase):
    def setUp(self):
        self.Borrowingapplication_Page = Borrowingapplication_Page(webdriver.Chrome())
        self.Borrowingapplication_Page.Login_Person()
        self.Borrowingapplication_Page.Chionce_enterprise()
        self.Borrowingapplication_Page.Gain_index()
        self.Borrowingapplication_Page.Borrow_order_url()  # 跳转到出差申请单

    def test_Travle_apply(self):  # 云快报首页的我的审批
        self.Travelapplication_Page.Time_over
        self.Travelapplication_Page.Chonice_go_Address
        self.Travelapplication_Page.Choinice_end_Address
        self.Travelapplication_Page.Expense_affiliation
        self.Travelapplication_Page.Choince_vehicle
        self.Travelapplication_Page.Travelreason_text
        self.Travelapplication_Page.Submit_examine
        self.Travelapplication_Page.Submint_sure
