from Common.basepage import BasePage
from pms.PageLocators.project_list_locators import ProjectListLocators as loc


class ProjectListPage(BasePage):
    """
    项目列表页面元素操作类
    """

    def enter_project_list(self):
        """
        进入项目列表页面
        :return:
        """
        self.click_element(loc.project_list_up, "点击项目列表")


if __name__ == "__main__":
    run_code = 0
