# 对象库层：封装页面元素的定位
class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def find_username(self):
        return self.driver.find_element_by_id("account")

    def find_pwd(self):
        return self.driver.find_element_by_name("password")

    def find_login_btn(self):
        return self.driver.find_element_by_id("submit")


# 操作层: 封装元素的操作方法
class LoginHandle:

    def __init__(self, driver):
        self.login_page = LoginPage(driver)

    def input_username(self, username):
        self.login_page.find_username().clear()
        self.login_page.find_username().send_keys(username)

    def input_pwd(self, pwd):
        self.login_page.find_pwd().clear()
        self.login_page.find_pwd().send_keys(pwd)

    def click_login_btn(self):
        self.login_page.find_login_btn().click()


# 业务层:将一个或者多个元素操作组合成一个功能
class LoginProxy:

    def __init__(self, driver):
        self.login_handle = LoginHandle(driver)

    def login(self, username, pwd):
        self.login_handle.input_username(username)
        self.login_handle.input_pwd(pwd)
        self.login_handle.click_login_btn()
