# -*- coding:utf-8 -*-
# Author : wzb
# Data : 2020/2/1 22:11
from PageLocators.indexpage_locators import IndexPageLocators as ioc
from Common.basepage import BasePage

class IndexPage(BasePage):
    def isExist_indexLogin_ele(self):
        # 查看页面是否存在退出按钮，等待10秒 元素有没有出现
        # 如果存在返回True，不存在返回False
        doc = "主页_是否存在首页按钮功能"
        try:
            self.wait_eleVisible(ioc.login_btn,doc=doc)
            return True
        except:
            return False

    def click_indexLogin(self):
        # 点击首页 登录按钮
        doc = "主页_点击首页按钮功能"
        try:
            self.click_element(ioc.login_btn,doc=doc)
            return True
        except:
            return False

