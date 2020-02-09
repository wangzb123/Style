# -*- coding:utf-8 -*-
# Author : wzb
# Data : 2020/2/2 16:32
# 正常场景-测试数据
success_data={"user":"13002566103","password":"wzb970608"}

# 异常测试用例(①用户名错误、②密码错误、③用户名&密码都错误、④用户名为空、⑤密码为空)
phone_data=[{"user":"1300256610","password":"wzb970608","check":"用户名或密码不正确"},
            {"user":"13002566103","password":"wzb97060","check":"用户名或密码不正确"},
            {"user":"1300256610","password":"wzb97060","check":"用户名或密码不正确"},
            {"user":"","password":"wzb970608","check":"请输入账号"},
            {"user":"13002566103","password":"","check":"请输入密码"},
            ]

