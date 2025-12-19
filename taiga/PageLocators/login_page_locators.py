from selenium.webdriver.common.by import By


class LoginPageLocators:
    """
    登录页面元素定位
    """
    # 用户名
    username = [By.XPATH, "//input[@placeholder='用户名']"]
    # 密码
    password = [By.XPATH, "//input[@placeholder='密码']"]
    # 验证码输入框
    verify_code = [By.XPATH, "//input[@placeholder='验证码']"]
    # 验证码图片
    verify_code_img = [By.CLASS_NAME, "el-image__inner"]
    # 登录
    login_buton = [By.XPATH, "//span[text()='登 录']/parent::button"]
    # 账号在其他设备登录，确定登录
    login_confirm = [By.XPATH, "//span[text()='确定']/parent::button"]
    # 未输入用户名或密码提示
    no_message = [By.XPATH, "//div[contains(@class,'el-form-item__error')]"]
    # 提示信息框
    message = [By.XPATH, "//p[@class='el-message__content']"]
