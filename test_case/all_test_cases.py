#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2018-05-31 Created by tongdg'

import unittest
import os

base_dir = os.getcwd()

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
    platform_case_dir = get_platform_dir()
    suite=[]
    test_unit = unittest.TestSuite()
    if platform is None and author is None:
        for case_dir in platform_case_dir:
            discover = unittest.defaultTestLoader.discover(
                start_dir=case_dir, pattern='*.py', top_level_dir=base_dir
            )
            for test_suite in discover:
                for test_case in test_suite:
                    test_unit.addTests(test_case)
                    suite.append(test_unit)
        return suite

    elif platform is not None and author is None:
        author_case_dir = get_author_dir(platform)
        for case_dir in author_case_dir[:-1]:
            discover = unittest.defaultTestLoader.discover(
                start_dir=case_dir, pattern='*.py', top_level_dir=os.path.join(base_dir,platform)
            )
            for test_suite in discover:
                for test_case in test_suite:
                    test_unit.addTests(test_case)
                    suite.append(test_unit)
        return suite

    elif platform is None and author is not None:
        for platform_dir in platform_case_dir:
            author_case_dir = get_author_dir(platform_dir)
            for author_case in author_case_dir[:-1]:
                if author_case == author:
                    discover = unittest.defaultTestLoader.discover(
                        start_dir=os.path.join(platform_dir,author), pattern='*.py', top_level_dir=base_dir
                    )
                    for test_suite in discover:
                        for test_case in test_suite:
                            test_unit.addTests(test_case)
                            suite.append(test_unit)
        return suite

    else:
        discover = unittest.defaultTestLoader.discover(
            start_dir=platform, pattern='*.py', top_level_dir=platform
        )

        for test_suite in discover:
            for test_case in test_suite:
                test_unit.addTests(test_case)
        suite.append(test_unit)
        return suite

print(create_test_suite(author='mobile'))



# 注意点：start_dir = 后跟的参数可以变
#        top_level_dir = 后跟的参数不能变动
#        所以我们要固定top_level_dir，变动start_dir,就可以了。





