# -*- coding:utf-8 -*-
# Author : wzb
# Data : 2020/2/5 13:37
import pytest
from selenium import webdriver
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from TestDatas import Common_Datas as CD
import allure

driver = None
# 声明它是一个fixture
@pytest.fixture(scope="class")
def access_web():
    global driver
    # 前置 访问登录页面
    driver = webdriver.Chrome()
    driver.get(CD.web_login_url)
    driver.maximize_window()
    lg = LoginPage(driver)
    IndexPage(driver).isExist_indexLogin_ele()
    IndexPage(driver).click_indexLogin()
    # 后置条件
    yield (driver,lg)
    driver.quit()

@pytest.fixture
def refresh_page():
    global driver
    # 前置条件
    yield
    # 后置条件
    driver.refresh()
