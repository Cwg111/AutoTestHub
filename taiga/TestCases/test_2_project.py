import pytest
from taiga.TestCases.conftest import login_page
from taiga.PageObjects.project_page import ProjectPage
from taiga.Common.taiga_log import logger
from taiga.Common.taiga_path import screenshot_dir
from taiga.Common.taiga_db import get_latest_project_name


class TestProject:
    project_page: ProjectPage = None
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
        self.project_page = ProjectPage(logger, screenshot_dir, login_page)

    def test_create_project(self):
        """
        测试创建项目
        :return:
        """
        create_project_name = self.project_page.create_project()
        page_first_project_name = self.project_page.get_first_project_name()
        assert create_project_name == page_first_project_name, \
            f"页面显示断言失败，创建项目名：{create_project_name}，页面显示项目名：{page_first_project_name}"
        db_latest_project_name = get_latest_project_name()
        assert create_project_name == db_latest_project_name, \
            f"数据库断言失败，创建项目名：{create_project_name}，数据库最新项目名：{db_latest_project_name}"


if __name__ == "__main__":
    run_code = 0
