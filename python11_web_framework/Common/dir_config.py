# -*- coding:utf-8 -*-
# Author : wzb
# Data : 2020/2/4 20:19
import os

"""
专门读取路径的值
"""
# 顶层框架目录
project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

# 测试报告的路径
test_report_path=os.path.join(project_path,'OutPuts','reports','/autoTest_report.html')

# 截图路径
screenshot_path=os.path.join(project_path, 'OutPuts','screenshots')

# log路径
logs_path = os.path.join(project_path, 'OutPuts','logs')

# 测试数据路径
testdatas_path= os.path.join(project_path, 'TestDatas')

# 测试用例路径
testcases_path = os.path.join(project_path, 'TestCases')