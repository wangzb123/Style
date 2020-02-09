# -*- coding:utf-8 -*-
# Author : wzb
# Data : 2020/2/2 20:57

from selenium.webdriver.common.by import By

class LoginPageLocators:
    # 元素定位
    # 用户名输入框
    user_name_text = (By.XPATH, '//input[@id="username"]')
    # 密码输入框
    password_text = (By.XPATH, '//input[@id="pwd"]')
    # 登录按钮
    login_btn = (By.XPATH, '//input[@id="login-button"]')
    # 立即注册按钮
    register_btn = (By.XPATH, '//a[text()="立即注册"]')
    # 错误信息提示框
    error_message = (By.XPATH, '//span[@class="error-con"]')
