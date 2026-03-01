from selenium.webdriver.common.by import By

class MemberPageLocators:
    """
    成员页面元素定位
    """
    member_list_locator = (By.XPATH, "//span[text()='Members']")
    member_add_button = (By.XPATH, "//button[text()='+ New member']")
    member_add_input = (By.XPATH, "//input[contains(@placeholder,'write an email')]")
    # 只有输入了已有用户正确的邮箱，才会有添加按钮出现
    member_add_confirm_button = (By.XPATH, "//button[contains(@class,'add-member')]")
    # 项目角色筛选框，需点击才能选到角色
    member_role_select = (By.XPATH, "//select[contains(@class,'invite')]")
    # 邀请说明输入框
    member_invite_input = (By.XPATH, "//textarea")
    # 邀请按钮
    member_invite_button = (By.XPATH, "//button[text()='Invite']")
    # 删除成员按钮，有多个，只删第二个
    member_delete_button = (By.XPATH, "(//a[@title='Delete member'])[2]")
    # 删除确认按钮
    member_delete_confirm_button = (By.XPATH, "//form[@style]//span[text()='Delete']")
    # 删除成功提示信息，注意这个要是在页面可见才是删除成功
    member_delete_success = (By.XPATH, "//h4[contains(text(),'Everything')]")
    
