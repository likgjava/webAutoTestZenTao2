

# 获取弹出框提示消息，并且关闭弹出框
def get_alert_msg_and_close(driver):
    # 获取警告框提示消息
    alert = driver.switch_to.alert
    msg = alert.text
    print("msg=", msg)
    alert.accept()
    return msg





