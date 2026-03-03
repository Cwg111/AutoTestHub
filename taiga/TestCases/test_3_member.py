import pytest
from taiga.PageObjects.member_page import MemberPage
from taiga.Common.taiga_path import screenshot_dir
from taiga.Common.taiga_log import logger
from Common.data import read_json_data
from taiga.Common.taiga_path import member_data_dir
from taiga.Common.taiga_db import get_project_member_count, get_all_member_count


class TestMember:
    member_page: MemberPage = None  # type: ignore
    """
    成员管理的测试用例
    """
    """
    @pytest.fixture(autouse=True) 是让 Fixture「自动生效」的开关，
    当设置为 True 时，所有测试用例都将自动调用该 Fixture。
    """
    member_data = read_json_data(member_data_dir)
    project_name = member_data["project_name"]
    not_exist_email = member_data["notexist_email"]
    exist_email = member_data["exist_email"]

    @pytest.fixture(autouse=True)
    def setup(self, enter_member_page):
        self.member_page = MemberPage(logger, screenshot_dir, enter_member_page)

    def test_add_non_existent_member(self):
        """
        测试添加不存在的成员
        """
        old_member_count = self.member_page.get_member_count()
        old_member_count_db = get_project_member_count(self.project_name)
        self.member_page.add_member(
            self.not_exist_email["email"],
            self.not_exist_email["role"],
            self.not_exist_email["invite_text"],
        )
        new_member_count = self.member_page.get_member_count()
        new_member_count_db = get_project_member_count(self.project_name)

        # 先判断并记录日志
        if (
            new_member_count != old_member_count
            or new_member_count_db != old_member_count_db
        ):
            logger.error(
                f"添加不存在的成员{self.not_exist_email['email']}失败，"
                f"页面成员数量：期望{old_member_count}，实际{new_member_count}，"
                f"数据库成员数量：期望{old_member_count_db}，实际{new_member_count_db}"
            )

        # 再断言
        assert new_member_count == old_member_count, (
            f"页面角度下，添加不存在的元成员失败，期望{old_member_count}，实际{new_member_count}"
        )
        assert new_member_count_db == old_member_count_db, (
            f"数据库角度下，添加不存在的元成员失败，期望{old_member_count_db}，实际{new_member_count_db}"
        )

    def test_add_member_success(self):
        """
        测试添加成员成功
        """
        old_member_count = self.member_page.get_member_count()
        old_member_count_db = get_project_member_count(self.project_name)
        self.member_page.add_member(
            self.exist_email["email"],
            self.exist_email["role"],
            self.exist_email["invite_text"],
        )
        self.member_page.refresh_page()
        new_member_count = self.member_page.get_member_count()
        new_member_count_db = get_project_member_count(self.project_name)

        # 先判断并记录日志
        if (
            new_member_count == old_member_count + 1
            and new_member_count_db == old_member_count_db + 1
        ):
            logger.info(
                f"添加成员{self.exist_email['email']}成功，"
                f"页面成员数量：期望{old_member_count + 1}，实际{new_member_count}，"
                f"数据库成员数量：期望{old_member_count_db + 1}，实际{new_member_count_db}"
            )
        else:
            logger.error(
                f"添加存在的成员{self.exist_email['email']}失败，"
                f"页面成员数量：期望{old_member_count + 1}，实际{new_member_count}，"
                f"数据库成员数量：期望{old_member_count_db + 1}，实际{new_member_count_db}"
            )

        # 再断言
        assert new_member_count == old_member_count + 1, (
            f"页面角度下，添加存在的元成员失败，期望{old_member_count + 1}，实际{new_member_count}"
        )
        assert new_member_count_db == old_member_count_db + 1, (
            f"数据库角度下，添加存在的元成员失败，期望{old_member_count_db + 1}，实际{new_member_count_db}"
        )

    def test_delete_members_success(self):
        """
        测试删除除第一个成员外的所有成员，包括邀请失败的成员
        """
        old_member_count = self.member_page.get_all_member_count()
        old_member_count_db = get_all_member_count(self.project_name)

        # 前置检查：如果当前成员数只有1个，无法删除
        if old_member_count == 1:
            logger.error(
                f"当前项目只有1个成员（项目创建者），无法删除其他成员，"
                f"页面成员数量：{old_member_count}，"
                f"数据库成员数量：{old_member_count_db}"
            )
            pytest.skip("当前项目只有1个成员，跳过删除测试")

        self.member_page.delete_members()
        new_member_count = self.member_page.get_all_member_count()
        new_member_count_db = get_all_member_count(self.project_name)

        # 先判断并记录日志
        if new_member_count == 1 and new_member_count_db == 1:
            logger.info(
                f"删除除第一个成员外的所有成员成功，"
                f"页面成员数量：期望：1，实际{new_member_count}，"
                f"数据库成员数量：期望：1，实际{new_member_count_db}"
            )
        else:
            logger.error(
                f"删除除第一个成员外的所有成员失败，"
                f"页面成员数量：期望：1，实际{new_member_count}，"
                f"数据库成员数量：期望：1，实际{new_member_count_db}"
            )
        # 再断言
        assert new_member_count == 1, (
            f"页面角度下，删除除第一个成员外的所有成员失败，期望：1，实际{new_member_count}"
        )
        assert new_member_count_db == 1, (
            f"数据库角度下，删除除第一个成员外的所有成员失败，期望：1，实际{new_member_count_db}"
        )
