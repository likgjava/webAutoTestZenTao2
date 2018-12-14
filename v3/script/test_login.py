# 导包
import unittest
from selenium import webdriver
import time

from v3.page.login_page import LoginProxy


# 定义测试类
class TestLogin(unittest.TestCase):

    def setUp(self):
        # 创建浏览器驱动对象
        self.driver = webdriver.Chrome()

        # 打开登录页面
        self.driver.get("http://demo.zentao.net/user-login.html")

        self.login_proxy = LoginProxy(self.driver)

    def tearDown(self):
        # 暂停3秒
        time.sleep(3)

        # 关闭浏览器驱动对象
        self.driver.quit()

    # 定义测试方法
    def test_login_pwd_is_empty(self):
        # 业务操作: 登录功能-密码为空
        self.login_proxy.login("demo", "")
        time.sleep(1)

        # 获取警告框提示消息
        alert = self.driver.switch_to.alert
        msg = alert.text
        print("msg=", msg)
        alert.accept()

    def test_login_pwd_is_error(self):
        # 业务操作: 登录功能-密码错误
        self.login_proxy.login("demo", "error")
        time.sleep(1)

        # 获取警告框提示消息
        alert = self.driver.switch_to.alert
        msg = alert.text
        print("msg=", msg)
        alert.accept()

    def test_login_success(self):
        # 业务操作: 登录功能-登录成功
        self.login_proxy.login("demo", "123456")
        time.sleep(1)

        # 获取页面标题
        title = self.driver.title
        print("title=", title)
