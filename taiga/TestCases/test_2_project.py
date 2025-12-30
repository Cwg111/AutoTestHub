import time
import pytest
from pms.TestCases.conftest import login_page
from pms.PageObjects.home_page import HomePage
from pms.PageObjects.project_list_page import ProjectListPage
from pms.TestDatas import home_datas as hd
from pms.Common.pms_log import logger
from pms.Common.pms_path import screenshot_dir


class TestHome:
    """
    首页的测试用例
    """
    """
    @pytest.fixture(autouse=True) 是让 Fixture「自动生效」的开关，
    注释后 Fixture 不会自动注入，导致依赖它的方法因缺少参数报错。
    后面的测试方法会因为缺少login_page参数而报错
    """
    @pytest.fixture(autouse=True)
    def setup(self, login_page):
        """
        初始化
        :return:
        """
        self.home_page = HomePage(logger, screenshot_dir, login_page)
        self.project_list_page = ProjectListPage(logger, screenshot_dir, login_page)

    def test_go_my_todo_process(self):
        """
        测试跳转到我的待办
        :return:
        """
        self.home_page.go_my_todo_process()
        self.home_page.wait_page_url_change(hd.home_url)
        assert self.home_page.get_page_url() == hd.my_todo_process_url

    def test_return_home(self):
        """
        测试从项目列表页面返回首页
        :return:
        """
        self.project_list_page.enter_project_list()
        self.home_page.return_home()
        assert self.home_page.get_page_url() == hd.home_url

    def test_go_project_list(self):
        """
        测试前往项目列表
        """
        self.home_page.go_project_list()
        assert self.home_page.get_page_url() == hd.project_list_url

    def teardown(self):
        """
        每个测试用例执行完毕，都要回到首页，不影响到其它用例
        :return:
        """
        self.home_page.return_home()


if __name__ == "__main__":
    run_code = 0
