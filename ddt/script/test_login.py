# 导包
import unittest
from selenium import webdriver
import time
from parameterized import parameterized
import json
from v3.page.login_page import LoginProxy
from ddt import utils


# def build_data():
#     return [
#         ("dev1", "", "登录失败，请检查您的用户名或密码是否填写正确", False),
#         ("dev1", "error", "登录失败，请检查您的用户名或密码是否填写正确", False),
#         ("demo", "123456", "我的地盘", True),
#     ]

def build_data():
    result = []
    with open("../data/login.json", encoding="utf-8") as f:
        data = json.load(f)
        data_list = data.values()
        # print("data_list=", data_list)
        for obj in data_list:
            # print("username=", obj.get("username"))
            result.append((obj.get("username"), obj.get("pwd"), obj.get("expect"), obj.get("is_success")))
    return result


# 定义测试类
class TestLogin(unittest.TestCase):

    def setUp(self):
        # 创建浏览器驱动对象
        self.driver = webdriver.Chrome()
        # 浏览器窗口最大化
        self.driver.maximize_window()
        # 设置元素等待
        self.driver.implicitly_wait(30)

        # 打开登录页面
        self.driver.get("http://demo.zentao.net/user-login.html")

        self.login_proxy = LoginProxy(self.driver)

    def tearDown(self):
        # 暂停3秒
        time.sleep(3)

        # 关闭浏览器驱动对象
        self.driver.quit()

    @parameterized.expand(build_data)
    def test_login(self, username, pwd, expect, is_success):
        self.login_proxy.login(username, pwd)

        # 登录成功
        if is_success:
            # 获取页面标题
            title = self.driver.title
            print("title=", title)

            # 断言
            self.assertIn(expect, title)
        else:
            # 获取警告框提示消息
            msg = utils.get_alert_msg_and_close(self.driver)

            # 断言
            self.assertIn(expect, msg)

    # # 定义测试方法
    # def test_login_pwd_is_empty(self):
    #     # 业务操作: 登录功能-密码为空
    #     self.login_proxy.login("demo", "")
    #     time.sleep(1)
    #
    #     # 获取警告框提示消息
    #     alert = self.driver.switch_to.alert
    #     msg = alert.text
    #     print("msg=", msg)
    #     alert.accept()
    #
    #     # 断言
    #     self.assertIn("登录失败，请检查您的用户名或密码是否填写正确", msg)
    #
    # def test_login_pwd_is_error(self):
    #     # 业务操作: 登录功能-密码错误
    #     self.login_proxy.login("demo", "error")
    #     time.sleep(1)
    #
    #     # 获取警告框提示消息
    #     alert = self.driver.switch_to.alert
    #     msg = alert.text
    #     print("msg=", msg)
    #     alert.accept()
    #
    #     # 断言
    #     self.assertIn("登录失败，请检查您的用户名或密码是否填写正确", msg)
    #
    # def test_login_success(self):
    #     # 业务操作: 登录功能-登录成功
    #     self.login_proxy.login("demo", "123456")
    #     time.sleep(1)
    #
    #     # 获取页面标题
    #     title = self.driver.title
    #     print("title=", title)
    #
    #     # 断言
    #     self.assertIn("我的地盘", title)
