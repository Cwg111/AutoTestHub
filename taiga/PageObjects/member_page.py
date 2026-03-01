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
        self.input_text(loc.member_add_input, user_email, "输入成员邮箱")

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
        self.enter_member_page()
        self.input_email(user_email)
        return self.is_valid_user_email()
