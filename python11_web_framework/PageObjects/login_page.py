# -*- coding:utf-8 -*-
# Author : wzb
# Data : 2020/2/1 22:11


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.loginpage_locators import LoginPageLocators as loc
from Common.basepage import BasePage
class LoginPage(BasePage):
    """
    :param username: 用户名
    :param password: 密码
    :return:
    """
    # 登录功能
    def login(self,username,password):
        # 输入用户名
        # 输入密码
        # 点击登录
        doc = "登录页面_登录功能"
        self.wait_eleVisible(loc.user_name_text,doc=doc)
        self.input_text(loc.user_name_text,username, doc=doc)
        self.input_text(loc.password_text, password, doc=doc)
        self.click_element(loc.login_btn, doc)

    # 注册功能
    def register_enter(self):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.register_btn))
        self.driver.find_element(*loc.register_btn).click()

    # 获取错误提示信息
    def get_errorMessage(self):
        doc = "登录页面_获取登录页面错误提示功能"
        self.wait_eleVisible(loc.error_message, doc=doc)
        return self.get_text(loc.error_message, doc=doc)



