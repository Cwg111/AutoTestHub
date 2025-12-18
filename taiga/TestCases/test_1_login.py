# @Create Date: 2025/6/18
# @Author: ganlu
import time

import pytest
from pms.TestDatas import login_datas as gd
from pms.PageLocators.login_page_locators import LoginPageLocators as loc
from pms.PageObjects.login_page import LoginPage
from pms.Common.pms_log import logger
from pms.Common.pms_path import screenshot_dir


class TestLogin:
    login_page: LoginPage = None
    """
    登录测试类
    """

    @pytest.fixture(autouse=True)
    def setup_class(self, init_pms):
        """
        初始化
        :return:
        """
        self.login_page = LoginPage(logger, screenshot_dir, init_pms)

    @pytest.mark.parametrize("user_no", gd.login_not_input)
    def test_login_not_input(self, user_no):
        """
        测试用户名或密码为空
        :param user_no: 这里实际上指的是依次取login_no_input这个列表中的元素，而每个元素都是一个字典，此时通过字典的key值来取值就行
        :return:
        """
        self.login_page.login(user_no["username"], user_no["password"])
        assert self.login_page.get_text(loc.no_message, "未输入用户名或密码登录报错") == user_no["message"]
        self.login_page.refresh_page()  # 注意在每次执行完之后要刷新页面，否则实际输入的账号密码并没有被清除

    @pytest.mark.parametrize("user_error", gd.login_error_input)
    def test_login_error(self, user_error):
        """
        测试用户名或密码错误
        :param user_error: 错误的账号名或密码
        :return:
        """
        self.login_page.login(user_error["username"], user_error["password"])
        assert user_error["message"] in self.login_page.get_text(loc.message, "用户名或密码错误登录报错")

    def test_login_success(self):
        self.login_page.login(gd.login_success["username"], gd.login_success["password"])
        self.login_page.wait_page_url_change(gd.login_url)
        assert self.login_page.get_page_url() == gd.home_url

    def test_login_out(self):
        self.login_page.logout()
        self.login_page.wait_page_url_change(gd.home_url)
        assert self.login_page.get_page_url() == gd.login_url
