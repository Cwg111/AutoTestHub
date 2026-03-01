import pytest
from taiga.PageObjects.member_page import MemberPage
from taiga.Common.taiga_path import screenshot_dir
from taiga.Common.taiga_log import logger


class TestMember:
    member_page: MemberPage = None  # type: ignore
    """
    成员管理的测试用例
    """
    """
    @pytest.fixture(autouse=True) 是让 Fixture「自动生效」的开关，
    当设置为 True 时，所有测试用例都将自动调用该 Fixture。
    """

    @pytest.fixture(autouse=True)
    def setup(self, enter_test_project):
        self.member_page = MemberPage(logger, screenshot_dir, enter_test_project)

    def test_add_non_existent_member(self):
        """
        测试添加不存在的成员
        """
        non_existent_email = "nonexistent@example.com"
        assert self.member_page.check_email_validity(non_existent_email) is False, (
            f"邮箱{non_existent_email}无效（用户不存在）"
        )
