#该接口文件基于企业微信的移动端以及PC端流程自动化开发，这里放一些人员信息以及地址
import datetime


def returnIntegrateUrl():
        return 'http://120.132.23.147:8016'
#正式后台管理
def returnofficialUrl():
        return 'http://106.75.114.250'
#代客下单正式
def Valet_orderUrlOfficicalUrl():
        return 'http://106.75.114.250/views/AgentCreateOrder.html'
#代课下单集成
def valet_orderUrl():
        return 'http://120.132.23.147:8016/views/AgentCreateOrder.html'

#出差申请单、借款申请单、采购申请单
def Travle_dictionaries():
        receipts = {'出差申请单': 'http://test.pc.51ykb.com/Form/FormViewer/BTAForm',
                    '借款申请单': 'http://test.pc.51ykb.com/Form/FormViewer/LoanForm'
                    }
        return receipts
def Overall_text():
        date = datetime.datetime.now()
        overall_Text = {'出差事由': '出差申请单测试“测试提单日期:' + date}
        return overall_Text