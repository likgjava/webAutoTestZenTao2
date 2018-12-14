# 导包
from selenium import webdriver
import time

# 创建浏览器驱动对象
driver = webdriver.Firefox()

# 打开登录页面
driver.get("http://demo.zentao.net/user-login.html")

# 业务操作: 登录功能-登录成功
# 输入用户名
driver.find_element_by_id("account").clear()
driver.find_element_by_id("account").send_keys("demo")

# 输入密码
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("123456")

# 点击登录按钮
driver.find_element_by_id("submit").click()

# 获取页面标题
title = driver.title
print("title=", title)

# 暂停3秒
time.sleep(3)

# 关闭浏览器驱动对象
driver.quit()
