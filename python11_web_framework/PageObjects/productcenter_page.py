# -*- coding:utf-8 -*-
# Author : wzb
# Data : 2020/2/2 21:58
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.productcenter_locators import ProductCenterLocators as poc
from Common.basepage import BasePage
class ProductCenterPage(BasePage):

    def isExist_backVersion_ele(self):
        try:
            self.wait_eleVisible(poc.back_version_btn)
            return True
        except:
            return False
