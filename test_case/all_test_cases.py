#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2018-05-31 Created by tongdg'

import unittest
import os
from common.utils import Utils
from HTMLTestRunner_cn import HTMLTestRunner
import threading
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import time
import smtplib
from BeautifulReport import BeautifulReport
from config.tdg_config import REPORT_PATH
base_dir = os.getcwd()
Utils = utils = Utils()
print(base_dir)


# 获取平台用例所在的文件夹
def get_platform_dir():
    platform_case_dir = []
    list = os.listdir(base_dir)
    for l in list:
        if os.path.isdir(os.path.join(base_dir, l)) is True:
            platform_case_dir.append(l)
    return platform_case_dir

# 获取作者用例所在的文件夹
def get_author_dir(platform_dir):
    author_case_dir = []
    base_author_dir = os.path.join(base_dir, platform_dir)
    list = os.listdir(base_author_dir)
    for l in list:
        if os.path.isdir(os.path.join(base_author_dir, l)) is True:
            author_case_dir.append(l)
    return author_case_dir

# 创建测试套件
# 参数详解：
# platform 输入想测试的平台：pc mobile pc_mobile
# author   输入你写的测试用例的文件夹：lff tdg zfk
# 四种方式： 1.platform=None,author=None 跑全部测试用例
#          2.platform=None,author不=None 跑你写的全部测试用例
#          3.platform不=None,author=None 跑你想跑的平台的测试用例
#          4.platform不=None,author不=None 跑指定平台下的你写的测试用例

def create_test_suite(platform=None,author=None):
    suite = []
    casedir = []
    platform_case_dir = get_platform_dir()
    # 1.platform=None,author=None 跑全部测试用例
    if platform is None and author is None:
        print(1)
        for platform_dir in platform_case_dir[:-1]:
            author_dirs = get_author_dir(platform_dir)
            for author_dir in author_dirs[:-1]:
                test_unit = unittest.TestSuite()
                discover = unittest.defaultTestLoader.discover(
                    start_dir=os.path.join(platform_dir,author_dir), pattern='*.py', top_level_dir=base_dir
                )
                for test_suite in discover:
                    for test_case in test_suite:
                        test_unit.addTests(test_case)
                suite.append(test_unit)
                casedir.append(os.path.join(platform_dir,author_dir))
        return suite,casedir
    # 2.platform=None,author不=None 跑你写的全部测试用例
    elif platform is not None and author is None:
        print(2)
        author_case_dir = get_author_dir(platform)
        print(author_case_dir)
        for case_dir in author_case_dir[:-1]:
            print(case_dir)
            test_unit = unittest.TestSuite()
            discover = unittest.defaultTestLoader.discover(
                start_dir=case_dir, pattern='*.py', top_level_dir=os.path.join(base_dir,platform)
            )
            for test_suite in discover:
                for test_case in test_suite:
                    test_unit.addTests(test_case)
            suite.append(test_unit)
            casedir.append(os.path.join(platform,case_dir))
        return suite,casedir
    # 3.platform不=None,author=None 跑你想跑的平台的测试用例
    elif platform is None and author is not None:
        print(3)
        for platform_dir in platform_case_dir:
            author_case_dir = get_author_dir(platform_dir)
            for author_dir in author_case_dir[:-1]:
                if author_dir == author:
                    test_unit = unittest.TestSuite()
                    discover = unittest.defaultTestLoader.discover(
                        start_dir=os.path.join(platform_dir,author), pattern='*.py', top_level_dir=base_dir
                    )
                    for test_suite in discover:
                        for test_case in test_suite:
                            test_unit.addTests(test_case)
                    suite.append(test_unit)
                    casedir.append(os.path.join(platform_dir,author))
        return suite,casedir

    else:
        print(4)
        test_unit = unittest.TestSuite()
        discover = unittest.defaultTestLoader.discover(
            start_dir=os.path.join(platform,author), pattern='*.py', top_level_dir=None
        )

        for test_suite in discover:
            for test_case in test_suite:
                test_unit.addTests(test_case)
        suite.append(test_unit)
        casedir.append(os.path.join(platform,author))
        return suite

# 多线程执行测试用例
def multi_run_case(suite):
    now = Utils.generate_time
    file_name = os.path.abspath(os.path.join(os.getcwd(),"..\\report\\"+ now +".html"))
    fp = open(file_name, 'wb')
    threads = []
    s = 0
    for i in suite:
        # 主要参数说明，retry重试次数，save_last_try最后一次的截图，verbosity=2设为2就ok了
        runner = HTMLTestRunner(
            title="ykb测试报告",
            description="ykb回归测试",
            stream=fp,
            verbosity=2, retry=0, save_last_try=True)
        t = threading.Thread(target=runner.run, args=(i,))
        threads.append(t)
        s = s + 1
        print(s)
    for t in threads:
        t.start()
    # 等待所有结束线程
    for t in threads:
        t.join()
    fp.close()

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
    # 获取所有的测试用例,返回的suite是个集合，所以要加上[0]
    # suite = create_test_suite(platform='mobile',author='tdg')[0]
    # for s in suite:
    #     print(s)
    # suite = create_test_suite(platform='mobile')[0]
    # for s in suite:
    #     print(s)
    # suite = create_test_suite(author='zfk')[0]
    # for s in suite:
    #     print(s)
    suite = create_test_suite()[0]
    for s in suite:
        print(s)
    # 获取指定的测试用例
    # suite = create_test_suite(platform=,author=)[0]
    # 执行所有测试用例
    multi_run_case(suite)
    # # 发送最新的测试报告
    send_mail(new_file(REPORT_PATH))

# print(create_test_suite())
# print(create_test_suite(platform='pc',author='tdg'))
# print(create_test_suite(author='tdg'))
# print(create_test_suite(platform='mobile'))

# 注意点：start_dir = 后跟的参数可以变
#        top_level_dir = 后跟的参数不能变动
#        所以我们要固定top_level_dir，变动start_dir,就可以了。





