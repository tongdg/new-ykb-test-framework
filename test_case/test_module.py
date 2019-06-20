import unittest
import os
base_dir = os.getcwd()
from HTMLTestRunner_cn import HTMLTestRunner


def createtestsuite():
    suite=[]
    #改变路径到测试路径到testcase并筛选
    case_dir = os.listdir(os.getcwd())
    test_unit = unittest.TestSuite()
    #测试套件
    discover_suites = unittest.defaultTestLoader.discover(base_dir, pattern='*.py')
    for testsuite in discover_suites:
        for testcase in testsuite:
            if test_unit not in testcase:
                suite.append(test_unit)
    return suite

print(createtestsuite())