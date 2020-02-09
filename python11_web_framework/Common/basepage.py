# -*- coding:utf-8 -*-
# Author : wzb
# Data : 2020/2/3 21:53
"""
1、封装基本函数- 执行日志，异常处理、失败截图
2、所有的页面公共部分
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from datetime import datetime
from Common import dir_config
from Common.logger import MyLog
import time
class BasePage:

    def __init__(self,driver):
        self.driver=driver


    # 等待元素
    def wait_eleVisible(self,locator,timeout=30,poll_frequency=0.5,doc=""):
        """
        :param locator: 元素定位，格式为(定位类型，定位方式)
        :param timeout:查找元素超时时间
        :param poll_frequency:每隔多久查找一次元素
        :param doc:截图文件路径描述
        :return:None
        """
        MyLog().my_log("====等待元素{0}可见===".format(locator),'INFO')
        try:
            # 开始等待时间
            start_time=datetime.now()
            WebDriverWait(self.driver,timeout,poll_frequency).until(EC.visibility_of_element_located(locator))
            # 结束等待时间
            end_time = datetime.now()
            wait_times=(end_time - start_time).seconds
            MyLog().my_log("等待元素可见时长{0}".format(wait_times),'INFO')
        except:
            MyLog().my_log("等待元素可见失败",'INFO')
            # 截图
            self.save_screenShot(doc)
            raise

    # 找元素
    def get_element(self,locator,doc=""):
        MyLog().my_log("查找元素{0}".format(locator),'INFO')
        try:
            return self.driver.find_element(*locator)
        except:
            MyLog().my_log("查找元素失败",'INFO')
            # 截图
            self.save_screenShot(doc)
            raise

    # 点击操作
    def click_element(self,locator,doc=""):
        # 找元素
        ele = self.get_element(locator,doc)
        # 元素操作
        MyLog().my_log("{0}点击元素:{1}".format(doc,locator),'INFO')
        try:
            ele.click()
        except:
            MyLog().my_log("元素点击失败",'INFO')
            # 截图
            self.save_screenShot(doc)
            raise

    # 输入操作
    def input_text(self,locator,text,doc=""):
        # 找元素
        ele = self.get_element(locator, doc)
        MyLog().my_log("根据元素{0}输入：{1}".format(locator[1],text),'INFO')
        # 输入操作
        try:
            ele.send_keys(text)
        except:
            MyLog().my_log("输入失败",'INFO')
            # 截图
            self.save_screenShot(doc)
            raise

    # 获取元素文本内容
    def get_text(self,locator,doc=""):
        # 找元素
        ele = self.get_element(locator, doc)
        # 获取文本
        MyLog().my_log("根据元素{0}获取内容".format(locator),'INFO')
        try:
            return  ele.text
        except:
            MyLog().my_log("===获取元素文本失败===",'INFO')
            # 截图
            self.save_screenShot(doc)
            raise
        pass

    # 获取元素属性
    def get_element_attribute(self,locator,attr,doc=""):
        # 找元素
        ele = self.get_element(locator, doc)
        # 获取元素属性
        MyLog().my_log("根据元素{0}获取属性".format(locator),'INFO')
        try:
            return ele.get_attribute(attr)
        except:
            MyLog().my_log("===获取元素属性失败===",'INFO')
            # 截图
            self.save_screenShot(doc)
            raise

    # 截图
    def save_screenShot(self,doc):
        #图片名称：模块名字_页面名称_年/月/日_时/分/秒.png
        filePath = dir_config.screenshot_path + \
                   "\{0}_{1}.png".format(doc,time.strftime("%Y-%m-%d-%H-%M-%S"),time.localtime())

        try:
            self.driver.save_screenshot(filePath)
            MyLog().my_log("截图成功，文件路径为{0}".format(filePath),'INFO')
        except:
            MyLog().my_log("截图失败",'ERROR')

