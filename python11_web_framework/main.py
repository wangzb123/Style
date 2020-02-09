# -*- coding:utf-8 -*-
# Author : wzb
# Data : 2020/2/5 10:53
import unittest
from Common.dir_config import *
from  HTMLTestRunnerNew import HTMLTestRunner

# 实例化套件对象
s = unittest.TestSuite()
# TestLoader用法
# 1、实例化TestLoader对象
# 2、使用discover去收集目录下所有用例
loader=unittest.TestLoader()
s.addTest(loader.discover(testcases_path))
# 运行
# runner = unittest.TextTestRunner()
# runner.run(s)

with open(test_report_path,'wb') as file:
    runner=HTMLTestRunner(
                stream=file,
                verbosity=2,
                title='单元测试报告',
                description='单元测试报告',
                tester='WZB')
    runner.run(s)