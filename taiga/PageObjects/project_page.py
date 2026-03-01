from Common.basepage import BasePage
from taiga.PageLocators.project_page_locators import ProjectPageLocators as loc
import time


class ProjectPage(BasePage):
    """
    项目列表页面元素操作类
    """
    # 把第一个项目名称单独抽出来作为类属性
    first_project_name: str = ""

    def create_project(self) -> str:
        """
        创建公共的SCRUM项目，并返回项目名称
        :return: str-生成的项目名称
        """
        self.action_move_element(loc.project_list_locator, "项目列表入口")
        self.click_element(loc.new_project_button, "新建项目按钮")
        # 当该账号第一次创建项目时，会弹窗，需要快速判断元素存在且可见，然后点击不要再次询问，保存设置
        if self.is_element_visible(loc.ask_question_button):
            self.click_element(loc.ask_question_button, "不要再次询问")
            self.click_element(loc.save_button, "保存设置")
        # 点击SCRUM类型的项目进行创建
        self.click_element(loc.scrum_project_type, "SCRUM项目")
        current_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        project_name = "Test_" + current_time
        self.input_text(loc.project_name_input, "项目名输入框", project_name)
        project_description = "创建" + project_name + "项目"
        self.input_text(loc.project_description_input, "项目描述输入框", project_description)
        self.click_element(loc.project_type_public, "项目类型为公共")
        self.click_element(loc.create_project_button, "创建项目按钮")
        time.sleep(1)
        return project_name

    def get_first_project_name(self) -> str:
        """
        获取第一个项目名，当前项目列表至少有一个项目
        :return: str-第一个项目名
        """
        self.action_move_element(loc.project_list_locator, "项目列表入口")
        self.click_element(loc.view_all_projects_button, "查看所有项目按钮")
        # 定位项目名元素时会定到多个，只取第一个
        first_project_ele = self.get_elements(loc.first_project_locator, "第一个项目名")[0]
        # 这个元素alt属性的值就是项目名
        self.first_project_name = self.get_attribute(first_project_ele, "第一个项目名", "alt")
        return self.first_project_name

    def get_project_number(self):
        """
        获取项目列表中项目数量
        :return: int-项目数量
        """
        self.action_move_element(loc.project_list_locator, "项目列表入口")
        self.click_element(loc.view_all_projects_button, "查看所有项目按钮")
        project_number = len(self.get_elements(loc.first_project_locator, "项目列表数量"))
        return project_number

    def is_project_count_less_or_eq_1(self):
        """
        判断项目列表中项目数量是否小于等于1
        :return: bool-项目数量是否小于等于1
        """
        project_number = self.get_project_number()
        result=project_number <= 1
        self.logger.info(f"项目数量<=1判断结果：{result}，当前项目列表中项目数量为：{project_number}")
        return result

    def enter_first_project(self):
        """
        进入第一个项目
        """
        # 获取第一个项目名
        self.get_first_project_name()
        # 取出模板中的By类型和带占位符的XPATH
        locator_type, xpath_template = loc.project_by_name_locator
        # 替换占位符为实际项目名
        final_xpath = xpath_template.format(project_name=self.first_project_name)
        # 生成最终可用的XPATH
        target_project_locator = [locator_type, final_xpath]
        # 先把鼠标移动到项目入口再点击，否则会点击失败
        self.action_move_element(target_project_locator, "项目入口")
        self.click_element(target_project_locator, "点击第一个项目")

    def enter_test_project(self):
        """
        进入测试专用项目
        """
        # 先进入项目列表
        self.action_move_element(loc.project_list_locator, "项目列表入口")
        self.click_element(loc.view_all_projects_button, "查看所有项目按钮")
        # 先把鼠标移动到项目入口再点击，否则会点击失败
        self.action_move_element(loc.test_project_loctor, "测试专用项目入口")
        self.click_element(loc.test_project_loctor, "点击测试专用项目")

    def enter_project_settings(self):
        """
        进入项目设置
        """
        # 获取项目设置按钮
        setting_ele = self.get_shadow_element(loc.shadow_host, loc.project_setting_button, "项目设置按钮")
        # 点击已定位到的设置按钮
        self.click_existing_element(setting_ele, "项目设置按钮")

    def update_project_name(self):
        """
        更新项目名
        """
        # 这一步已经获取到项目名了
        self.enter_first_project()
        # 先进入项目设置
        self.enter_project_settings()
        new_project_name=self.first_project_name + "_new"
        self.input_text(loc.change_project_name_input, "项目名输入框", new_project_name)
        self.click_element(loc.change_project_save_button, "保存项目名按钮")

    def delete_first_project(self):
        # 这一步已经获取到项目名了
        self.enter_first_project()
        # 先进入项目设置
        self.enter_project_settings()
        self.click_element(loc.delete_project_button, "删除项目按钮")
        self.click_element(loc.delete_project_confirm_button, "确认删除项目按钮")
        time.sleep(0.5) # 删除后数据库响应慢，所以这里休眠0.5秒


if __name__ == "__main__":
    run_code = 0
