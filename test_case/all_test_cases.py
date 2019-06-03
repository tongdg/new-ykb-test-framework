#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2018-05-31 Created by tongdg'

import unittest
import os
from common.utils import Utils
from HTMLTestRunner_cn import HTMLTestRunner
import threading
base_dir = os.getcwd()
Utils = utils = Utils()
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
    test_unit = unittest.TestSuite()
    if platform is None and author is None:
        for case_dir in platform_case_dir:
            discover = unittest.defaultTestLoader.discover(
                start_dir=case_dir, pattern='*.py', top_level_dir=base_dir
            )
            for test_suite in discover:
                for test_case in test_suite:
                    test_unit.addTests(test_case)
                    if test_unit not in suite:
                        suite.append(test_unit)
            casedir.append(case_dir)
        return suite,casedir


    elif platform is not None and author is None:
        author_case_dir = get_author_dir(platform)
        for case_dir in author_case_dir[:-1]:
            discover = unittest.defaultTestLoader.discover(
                start_dir=case_dir, pattern='*.py', top_level_dir=os.path.join(base_dir,platform)
            )
            for test_suite in discover:
                for test_case in test_suite:
                    test_unit.addTests(test_case)
                    if test_unit not in suite:
                        suite.append(test_unit)
            casedir.append(os.path.join(platform,case_dir))
        return suite,casedir


    elif platform is None and author is not None:
        for platform_dir in platform_case_dir:
            author_case_dir = get_author_dir(platform_dir)
            for author_dir in author_case_dir[:-1]:
                if author_dir == author:
                    discover = unittest.defaultTestLoader.discover(
                        start_dir=os.path.join(platform_dir,author), pattern='*.py', top_level_dir=base_dir
                    )
                    for test_suite in discover:
                        for test_case in test_suite:
                            test_unit.addTests(test_case)
                            if test_unit not in suite:
                                suite.append(test_unit)
                    casedir.append(os.path.join(platform_dir,author))
        return suite,casedir


    else:
        discover = unittest.defaultTestLoader.discover(
            start_dir=platform, pattern='*.py', top_level_dir=platform
        )

        for test_suite in discover:
            for test_case in test_suite:
                if test_unit not in suite:
                    test_unit.addTests(test_case)
        suite.append(test_unit)
        casedir.append(os.path.join(platform,author))
        return suite

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
    for t in threads:
        t.start()
    # 等待所有结束线程
    for t in threads:
        t.join()


if __name__ == '__main__':
    # 获取所有的测试用例
    suite = create_test_suite()[0]
    # # 获取指定的测试用例
    # suite = create_test_suite(platform=,author=)[0]

    # 执行所有测试用例
    multi_run_case(suite)
    # 执行










# print(create_test_suite())
# print(create_test_suite(platform='pc',author='tdg'))
# print(create_test_suite(author='tdg'))
# print(create_test_suite(platform='mobile'))


# 注意点：start_dir = 后跟的参数可以变
#        top_level_dir = 后跟的参数不能变动
#        所以我们要固定top_level_dir，变动start_dir,就可以了。





