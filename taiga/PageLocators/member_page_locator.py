from selenium.webdriver.common.by import By

class MemberPageLocators:
    """
    成员页面元素定位
    """
    member_list_locator = (By.XPATH, "//span[text()='Members']")
    member_add_button = (By.XPATH, "//button[text()='+ New member']")
    member_add_input = (By.XPATH, "//input[contains(@placeholder,'write an email')]")
    # 只有输入了正确的邮箱格式，才会有添加按钮出现
    member_add_confirm_button = (By.XPATH, "//button[contains(@class,'add-member')]")
    # 取消邀请按钮
    member_invite_cancel_button = (By.XPATH, "//div[@project='project']//a[@class='close']")
    # 项目角色筛选框，需点击才能选到角色
    member_role_select = (By.XPATH, "//select[contains(@class,'invite')]")
    # 邀请说明输入框
    member_invite_input = (By.XPATH, "//textarea")
    # 邀请按钮
    member_invite_button = (By.XPATH, "//button[text()='Invite']")
    # 重新邀请按钮，出现这个按钮就代表了邀请了一个不存在的用户邮箱，可能有多个
    member_invite_resend_button = (By.XPATH, "//a[@title='Resend']")
    # 活跃用户即实际邀请成功的存在的用户
    member_active_user = (By.XPATH, "//div[@class='active']")
    # 删除按钮数，这个按钮数显示了所有成员，包括邀请失败的成员
    member_delete_button_count = (By.XPATH, "//a[@title='Delete member']")
    # 删除成员按钮，有多个，只删第二个
    member_delete_second_button = (By.XPATH, "(//a[@title='Delete member'])[2]")
    # 删除确认按钮
    member_delete_confirm_button = (By.XPATH, "//form[@style]//span[text()='Delete']")
    
