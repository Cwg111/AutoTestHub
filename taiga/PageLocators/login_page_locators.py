from selenium.webdriver.common.by import By


class LoginPageLocators:
    """
    登录页面元素定位
    """
    # 用户名输入框
    username = [By.XPATH, "//input[contains(@placeholder,'Username')]"]
    # 密码输入框
    password = [By.XPATH, "//input[contains(@placeholder,'Password')]"]
    # 登录按钮
    login_button = [By.XPATH, "//button[@title='Login']"]
    # 只有账号或密码错误时该元素才会可见
    message = [By.XPATH, "//p[contains(text(),'are incorrect')]"]
    # 账号头像框
    user_avatar= [By.XPATH, "//a[@class='user-avatar']//img"]
    # 退出登录按钮
    logout_button = [By.XPATH, "//a[@title='Logout']"]
