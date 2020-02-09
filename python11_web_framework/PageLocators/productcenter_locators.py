# -*- coding:utf-8 -*-
# Author : wzb
# Data : 2020/2/2 21:52
from selenium.webdriver.common.by import By
class ProductCenterLocators:
    # 元素定位
    # 返回旧版按钮
    back_version_btn = (By.XPATH, '//span[text()="返回旧版"]')