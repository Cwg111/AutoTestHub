from Common.basepage import BasePage
from taiga.PageLocators.project_page_locators import ProjectPageLocators as loc
import time


class ProjectListPage(BasePage):
    """
    项目列表页面元素操作类
    """

    def create_project(self) -> str:
        """
        创建公共的SCRUM项目，并返回项目名称
        :return: str-生成的项目名称
        """
        self.action_move_element(loc.project_list_locator, "新建项目入口")
        self.click_element(loc.new_project_button, "新建项目按钮")
        # 当该账号第一次创建项目时，会弹窗，需要快速判断元素存在且可见，然后点击不要再次询问，保存设置
        if self.is_element_visible(loc.ask_question_button):
            self.click_element(loc.ask_question_button, "不要再次询问")
            self.click_element(loc.save_button, "保存设置")
        # 点击SCRUM类型的项目进行创建
        self.click_element(loc.scrum_project_type, "SCRUM项目")
        current_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        project_name = "Test_" + current_time
        self.input_text(loc.project_name_input, project_name, "项目名输入框")
        project_description = "创建" + project_name + "项目"
        self.input_text(loc.project_description_input, project_description, "项目描述输入框")
        self.click_element(loc.project_type_public, "项目类型为公共")
        self.click_element(loc.create_project_button, "创建项目按钮")
        return project_name

    def get_first_project_name(self) -> str:
        """
        获取第一个项目名大，当前项目列表至少有一个项目
        :return: str-第一个项目名
        """
        self.click_element(loc.view_all_projects_button, "查看所有项目按钮")
        # 定位项目名元素时会定到多个，只取第一个
        first_project_ele= self.get_elements(loc.first_project_locator, "第一个项目名")[0]
        # 这个元素alt属性的值就是项目名
        return self.get_attribute(first_project_ele, "第一个项目名","alt")


if __name__ == "__main__":
    run_code = 0
