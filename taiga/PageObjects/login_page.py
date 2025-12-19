from Common.basepage import BasePage
from Common.verify_code import get_data_url_code
from pms.PageLocators.login_page_locators import LoginPageLocators as loc
from pms.PageLocators.home_page_locators import HomePageLocators as loc_home
from pms.Common import pms_path
from Common.data import clear_img


class LoginPage(BasePage):
    """
    登录操作
    """

    def login(self, user, pwd):
        """
        登录操作
        :return:
        """
        self.input_text(loc.username, "输入用户名", user)
        self.input_text(loc.password, "输入密码", pwd)
        url_img = self.get_attribute(loc.verify_code_img, "验证码图片地址", "src")
        code = get_data_url_code(url_img, pms_path.verify_code_dir)
        clear_img(pms_path.verify_code_dir, is_all=True)  # 获取完成验证码后，清除所有图片
        self.input_text(loc.verify_code, "输入验证码", code)
        self.click_element(loc.login_buton, "点击登录")
        self.click_element_if_exists(loc.login_confirm, "点击确认")

    def logout(self):
        """
        退出登录
        :return:
        """
        self.click_element(loc_home.username, "点击用户名框")
        self.click_element(loc_home.logout, "点击退出按钮")
        self.click_element(loc_home.logout_confirm, "点击退出确定按钮")
