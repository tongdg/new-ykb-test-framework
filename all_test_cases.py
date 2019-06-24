#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2018-05-31 Created by tongdg'

import unittest
import os
from common.utils import Utils
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import time
import smtplib
import threading
# BeautifulReport
from BeautifulReport import BeautifulReport
from config.tdg_config import REPORT_PATH
from tomorrow import threads
base_dir = os.path.join(os.getcwd(),'test_case')
Utils = utils = Utils()
print(base_dir)


def create_test_suite():
    suite = []
    test_unit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(
        start_dir=base_dir, pattern='*.py', top_level_dir=None
    )
    for test_suite in discover:
        for test_case in test_suite:
            test_unit.addTests(test_case)
    suite.append(test_unit)
    return suite

@threads(5)
def run(test_suit):
    result = BeautifulReport(test_suit)
    result.report(description='测试deafult报告', log_path='report')

# 获取最新生成报告的路径
def new_file(test_dir):
    # 列举test_dir目录下的所有文件，结果以列表形式返回。
    lists = os.listdir(test_dir)
    # sort按key的关键字进行排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间
    # 最后对lists元素，按文件修改时间大小从小到大排序。
    # def f(fn):  fn 传入的是lists里面的值
    #   returen os.path.getmtime(test_dir + '\\' + fn))
    lists.sort(key=lambda fn: os.path.getmtime(test_dir + '\\' + fn))
    # 获取最新文件的绝对路径
    file_path = os.path.join(test_dir, lists[-1])
    return file_path

# 定义发送邮件
def send_mail(file_new):
    # 发信邮箱
    mail_from = 'tdg1994@126.com'
    # 收信邮箱
    # mail_to = ['1968230653@qq.com','892431872@qq.com','lf1997f@163.com','zhangfk@yuanian.com']
    mail_to = '892431872@qq.com'
    # 定义正文
    f = open(file_new, 'rb')
    mail_bady = f.read()
    f.close()
    # 创建一个带附件的实例
    msg = MIMEMultipart()
    msg.attach(MIMEText(mail_bady, _subtype = 'html', _charset = 'utf-8'))
    # 通过附件的方式，发送测试报告
    att1 = MIMEText(open(file_new, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename=' + file_new
    msg.attach(att1)
    # rcejqplpfavmbbbc  qq邮箱  892431872@qq.com
    # 定义标题
    msg['Subject'] = Header(u'云快报自动化测试报告', 'utf-8')
    # 定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
    msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    msg['From'] = mail_from
    msg['to'] = ','.join(mail_to)

    username = 'tdg1994@126.com'
    password = '11a2s3d4q5ww6e'

    # 连接 SMTP 服务器，此处用的126的 SMTP 服务器
    smtp = smtplib.SMTP()
    smtp.connect('smtp.126.com')
    smtp.login(username, password)
    smtp.sendmail(mail_from, mail_to, msg.as_string())
    smtp.quit()

if __name__ == '__main__':
    test_suite = create_test_suite()[0]
    for ts in test_suite:
        run(ts)
    # for s in suite:
    #     run(s)
    # 执行所有测试用例
    # # 发送最新的测试报告
    # send_mail(new_file(REPORT_PATH))

# print(create_test_suite())
# print(create_test_suite(platform='pc',author='tdg'))
# print(create_test_suite(author='tdg'))
# print(create_test_suite(platform='mobile'))

# 注意点：start_dir = 后跟的参数可以变
#        top_level_dir = 后跟的参数不能变动
#        所以我们要固定top_level_dir，变动start_dir,就可以了。





