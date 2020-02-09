# -*- coding:utf-8 -*-
# Author : wzb
# Data : 2020/2/2 21:30
from selenium.webdriver.common.by import By
class IndexPageLocators:
    # 元素定位
    # 登录按钮
    login_btn = (By.XPATH, '//a[text()="登录/注册"]')