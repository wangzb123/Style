# -*- coding:utf-8 -*-
# Author : wzb
# Data : 2020/2/4 20:17
import logging
from Common.dir_config import *
class MyLog:
    def my_log(self,msg,level):
        #定义一个日志收集器 my_longger
        my_logger=logging.getLogger('python11')

        # 设置级别
        my_logger.setLevel(level)

        # 设置输出格式
        formatter = logging.Formatter(u"%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")

        # 创建一个输出渠道
        ch=logging.StreamHandler()
        ch.setLevel(level)
        ch.setFormatter(formatter)

        fh=logging.FileHandler(logs_path + "/log.txt" ,encoding='utf-8')
        fh.setLevel(level)
        fh.setFormatter(formatter)

        # 对接,指定输出渠道
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        # 收集日志
        if level == "DEBUG":
            my_logger.debug(msg)
        elif level == "INFO":
            my_logger.info(msg)
        elif level == "ERROR":
            my_logger.error(msg)
        elif level == "WARNING":
            my_logger.warning(msg)
        elif level == "CRITICAL":
            my_logger.critical(msg)

        # 关闭渠道
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)


    def debug(self,msg):
        self.my_log(msg,'DEBUG')

    def info(self,msg):
        self.my_log(msg,'INFO')

    def error(self, msg):
        self.my_log(msg, 'ERROR')