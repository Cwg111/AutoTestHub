from Common.basepage import BasePage
from taiga.PageLocators.member_page_locator import MemberPageLocators as loc



class MemberPage(BasePage):
    """
    成员页面操作，前置操作已进入指定项目的设置界面了
    """

    def enter_member_page(self):
        """
        进入成员页面
        """
        self.action_chains_click(loc.member_list_locator, "进入成员列表")

    def input_email(self, user_email: str):
        """
        添加成员
        :param user_email: 成员邮箱
        :return:
        """
        self.click_element(loc.member_add_button, "点击添加成员按钮")
        self.input_text(loc.member_add_input, "输入成员邮箱", user_email)

    def is_valid_user_email(self) -> bool:
        """
        判断输入的邮箱是否为已存在的用户邮箱
        通过判断添加成员确认按钮是否存在来确定
        :return: bool-True表示邮箱有效（用户存在），False表示邮箱无效
        """
        return self.is_element_visible(loc.member_add_confirm_button)

    def check_email_validity(self, user_email: str) -> bool:
        """
        检查邮箱是否有效（用户是否存在），即添加成员失败
        :param user_email: 要检查的邮箱
        :return: bool-True表示邮箱有效（用户存在），False表示邮箱无效
        """
        self.input_email(user_email)
        return self.is_valid_user_email()
    
    def cancel_invite(self):
        """
        取消邀请成员
        :return:
        """
        self.click_element(loc.member_invite_cancel_button, "点击取消邀请按钮")
    
    def get_member_count(self) -> int:
        """
        获取当前成功邀请的项目成员数量
        :return: 成员数量
        """
        # 注意再添加成功成员后，页面不会立马显示出来，需要刷新页面
        self.refresh_page()
        return len(self.get_elements(loc.member_active_user, "获取邀请成功的用户数量"))
    
    def get_all_member_count(self) -> int:
        """
        获取所有成员数量，包括邀请失败的成员
        :return: 所有成员数量
        """
        # 注意删除后需要刷新页面
        self.refresh_page()
        return len(self.get_elements(loc.member_delete_button_count, "获取删除按钮数量"))
    
    def add_member(self,user_email: str,user_role: str,invite_text: str):
        """
        添加成员
        :param user_email: 要检查的邮箱
        :param user_role: 要添加的成员角色
        :param invite_text: 邀请成员时的提示文本
        :return:
        """
        if self.check_email_validity(user_email):
            self.click_element(loc.member_add_confirm_button, "点击添加成员确认按钮")
            self.select_option_by_text(loc.member_role_select, "选择成员角色",user_role)
            self.input_text(loc.member_invite_input, "输入邀请成员提示文本", invite_text)
            self.click_element(loc.member_invite_button, "点击邀请成员发送按钮")
        else:
            self.logger.error(f"邮箱{user_email}无效（用户不存在）")
    
    def delete_members(self):
        """
        删除除第一个成员外的所有成员，包括邀请失败的成员
        :return:
        """
        while self.get_all_member_count() > 1:
            self.click_element(loc.member_delete_second_button, "点击删除成员按钮")
            self.click_element(loc.member_delete_confirm_button, "点击删除成员确认按钮")


