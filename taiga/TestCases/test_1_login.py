import pytest
from taiga.PageLocators.login_page_locators import LoginPageLocators as loc
from taiga.PageObjects.login_page import LoginPage
from taiga.Common.taiga_log import logger
from taiga.Common.taiga_path import *
from Common.data import read_json_data


class TestLogin:
    login_page: LoginPage = None
    login_data = read_json_data(login_data_dir)  # 读取登录数据
    """
    登录测试类
    """

    @pytest.fixture(autouse=True)
    def setup_class(self, init_taiga):
        """
        初始化
        :return:
        """
        self.login_page = LoginPage(logger, screenshot_dir, init_taiga)

    @pytest.mark.parametrize("user_error", login_data["login_error_input"])
    def test_login_error(self, user_error):
        """
        测试用户名或密码错误
        :param user_error: 错误的账号名或密码
        :return:
        """
        self.login_page.login(user_error["username"], user_error["password"])
        assert user_error["message"] in self.login_page.get_text(loc.message, "用户名或密码错误登录报错")
        self.login_page.wait_ele_not_visible(loc.message, "等待消息提示框消失")  # 消息提示框不消失会影响其它元素操作

    def test_login_no_input(self):
        """
        测试用户名为空
        :return:
        """
        self.login_page.login(self.login_data["login_no_input"]["username"],
                              self.login_data["login_no_input"]["password"])
        assert self.login_data["login_no_input"]["message"] in self.login_page.get_attribute(loc.username,
                                                                                             "用户名为空登录报错",
                                                                                             "validationMessage")

    def test_login_success(self):
        self.login_page.login(self.login_data["login_admin_success"]["username"],
                              self.login_data["login_admin_success"]["password"])
        self.login_page.wait_page_url_change(login_url)
        assert self.login_page.get_page_url() == home_url

    def test_login_out(self):
        self.login_page.logout()
        self.login_page.wait_page_url_change(base_url)
        assert self.login_page.get_page_url() == discover_url
