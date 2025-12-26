from selenium.webdriver.common.by import By


class HomePageLocators:
    project_list_locator = [By.XPATH, "//span[text()='Projects']"]
    new_project_button = [By.XPATH, "//span[text()='New project']"]
    # 不要再次询问，只有第一次创建项目时才会出现此按钮
    ask_question_button = [By.XPATH, "//label[@class='ask-label']"]
    # 保存设置，第一次创建项目时才会出现此按钮
    save_button = [By.XPATH, "//span[text()='SAVE PREFERENCES']"]
    # 查看所有项目按钮，注意只有至少有一个项目时才会出现此按钮
    view_all_projects_button = [By.XPATH, "//a[@title='View all projects']"]
    # 创建项目时，选择类型为Scrum的项目
    scrum_project_type = [By.XPATH, "//p[text()='Scrum']"]
    # 输入项目名称
    project_name_input = [By.XPATH, "//input[@name='project-name']"]
    # 输入项目描述
    project_description_input = [
        By.XPATH,
        "//textarea[contains(@placeholder,'Description')]",
    ]
    # 项目类型为公共
    project_type_public = [By.XPATH, "//label[@for='template-public']"]
    # 项目类型为私有
    project_type_private = [By.XPATH, "//label[@for='template-private']"]
    # 创建项目按钮
    create_project_button = [By.XPATH, "//button[text()='Create Project']"]
    # 点击新建一个项目后项目列表中第一个项目（是根据创建时间从晚到早排序的，最新创建的在第一个），会定位到多个元素，只取第一个
    first_project_locator = [By.XPATH, "//a[@class='list-itemtype-project-image']//img"]
    # 项目中的设置按钮
    project_setting_button = [By.XPATH, "//span[text()='Settings']"]


if __name__ == "__main__":
    run_code = 0
