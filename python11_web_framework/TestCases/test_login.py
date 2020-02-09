# -*- coding:utf-8 -*-
# Author : wzb
# Data : 2020/2/2 10:46
from selenium import webdriver
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from PageObjects.productcenter_page import ProductCenterPage
from TestDatas import Common_Datas as CD
from TestDatas import Login_Datas as LD
from PageLocators.indexpage_locators import IndexPageLocators as ioc
import pytest
import allure

@pytest.mark.usefixtures("access_web") # 执行conftest.py中access_web函数
@pytest.mark.usefixtures("refresh_page")
class TestLogin:
    # @classmethod
    # def setUpClass(cls):
    #     # 前置 访问登录页面
    #     cls.driver = webdriver.Chrome()
    #     cls.driver.get(CD.web_login_url)
    #     cls.driver.maximize_window()
    #     cls.lg = LoginPage(cls.driver)
    #     cls.ig = IndexPage(cls.driver).isExist_login_ele()
    #     cls.driver.find_element(*ioc.login_btn).click()
    # @classmethod
    # def tearDownClass(cls):
    #     # 所有用例执行完，后置条件
    #     #cls.driver.quit()
    #     pass
    #
    # def setUp(self):
    #     pass
    #
    # def tearDown(self):
    #     self.driver.refresh()

    # 异常登录用例(①用户名错误、②密码错误、③用户名&密码都错误、④用户名为空、⑤密码为空)
    # @pytest.mark.parametrize("参数名",列表数据 )
    @pytest.mark.parametrize("data",LD.phone_data)
    def test_login_1_wrong(self, data,access_web):
        # 步骤 输入用户名、密码,点击登录
        access_web[1].login(data["user"], data["password"])
        # 断言 登录页面提示：用户名或密码不正确
        # 登录页面中获取提示框的文本内容
        # 对比文本内容与期望的值 是否相等
        assert access_web[1].get_errorMessage(), data["check"]

    # 正常登录用例--登录成功
    # fixture的函数名称，用来接收它的返回值
    @pytest.mark.demo()
    def test_login_2_success(self,access_web):
        # 步骤 输入用户名、密码,点击登录
        access_web[1].login(LD.success_data["user"],LD.success_data["password"])
        # 断言 首页当中-是否找到退出这个元素
        assert ProductCenterPage(access_web[0]).isExist_backVersion_ele()

