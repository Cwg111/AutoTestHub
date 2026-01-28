from Common.basepage import BasePage
from taiga.PageLocators.login_page_locators import LoginPageLocators as loc
from taiga.Common.taiga_path import login_url, home_url


class LoginPage(BasePage):
    """
    登录操作
    """

    def login(self, user, pwd):
        """
        登录操作
        :return:
        """
        # 在输入账号密码前，先判断是否是登录页面
        if self.is_element_visible(loc.login_button_in_discover):
            self.click_element(
                loc.login_button_in_discover, "点击在discover页面的登录按钮"
            )
        self.input_text(loc.username, "输入用户名", user)
        self.input_text(loc.password, "输入密码", pwd)
        self.click_element(loc.login_button, "点击登录")

    def login_and_assert(self, user, pwd):
        """
        登录并断言
        :param user:
        :param pwd:
        :return:
        """
        self.login(user, pwd)
        self.wait_page_url_change(login_url)
        assert self.get_page_url() == home_url

    def logout(self):
        """
        退出登录
        :return:
        """
        self.action_move_element(loc.user_avatar, "移动到用户头像")
        self.click_element(loc.logout_button, "点击退出按钮")
