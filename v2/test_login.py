# 导包
import unittest
from selenium import webdriver
import time


# 定义测试类
class TestLogin(unittest.TestCase):

    def setUp(self):
        # 创建浏览器驱动对象
        self.driver = webdriver.Firefox()

        # 打开登录页面
        self.driver.get("http://demo.zentao.net/user-login.html")

    def tearDown(self):
        # 暂停3秒
        time.sleep(3)

        # 关闭浏览器驱动对象
        self.driver.quit()

    # 定义测试方法
    def test_login_pwd_is_empty(self):
        # 业务操作: 登录功能-密码为空
        # 输入用户名
        self.driver.find_element_by_id("account").clear()
        self.driver.find_element_by_id("account").send_keys("demo")

        # 输入密码
        self.driver.find_element_by_name("password").clear()

        # 点击登录按钮
        self.driver.find_element_by_id("submit").click()

        # 获取警告框提示消息
        alert = self.driver.switch_to.alert
        msg = alert.text
        print("msg=", msg)
        alert.accept()

    def test_login_pwd_is_error(self):
        # 业务操作: 登录功能-密码错误
        # 输入用户名
        self.driver.find_element_by_id("account").clear()
        self.driver.find_element_by_id("account").send_keys("demo")

        # 输入密码
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys("error")

        # 点击登录按钮
        self.driver.find_element_by_id("submit").click()

        # 获取警告框提示消息
        alert = self.driver.switch_to.alert
        msg = alert.text
        print("msg=", msg)
        alert.accept()

    def test_login_success(self):
        # 业务操作: 登录功能-登录成功
        # 输入用户名
        self.driver.find_element_by_id("account").clear()
        self.driver.find_element_by_id("account").send_keys("demo")

        # 输入密码
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys("123456")

        # 点击登录按钮
        self.driver.find_element_by_id("submit").click()

        # 获取页面标题
        title = self.driver.title
        print("title=", title)
