#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2018-06-04 Created by tongdg'
import os

"""
path配置
"""
BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
REPORT_PATH = os.path.abspath(os.path.join(BASE_PATH,"report"))

"""
测试数据配置
"""
# JC切换企业测试数据配置
def get_enterprise_login():
    data = []
    # 企业名称 用户名 都正确
    data.append(['测试一下下','童定国'])
    # 企业名称正确 用户名不正确
    data.append(['测试一下下','tdg'])
    # 企业名称不正确 用户名不正确
    data.append(['测试一下','tdg'])
    # 企业名称不正确 用户名正确
    data.append(['测试一下', '童定国'])
    return data

# ZS切换企业测试数据配置





