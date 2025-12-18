#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :home_page_locators.py
# @Time      :2025/10/31 10:34
# @Author    :ChenWenGang
from selenium.webdriver.common.by import By


class HomePageLocators:
    # 用户成功登录后登录名框
    username = [By.XPATH, "//i[@class='user-icon']"]
    # 退出按钮
    logout = [By.XPATH, "//li[text()='退出']"]
    # 退出确定按钮
    logout_confirm = [By.XPATH, "//span[text()='确定']/parent::button"]
    # 回到首页按钮
    return_home = [By.XPATH, "//div[@class='title-left']"]
    # 我的待办流程
    my_todo_process = [By.XPATH, "//span[text()='我的待办流程']"]
    # 项目列表
    project_list = [By.XPATH, "//span[text()='项目列表']"]
    # 查看所有
    look_all = [By.XPATH, "//span[text()='查看所有']"]
    # 跳转到我的待办中，并筛选设校审流程
    my_todo_process_filter_prepare = [By.XPATH,
                                      "//p[.//b[text()='设校审流程']]/preceding-sibling::button//i[@class='el-icon']"]
    # 跳转到我的待办中，并筛选项目状态变更流程
    my_todo_process_filter_status = [By.XPATH,
                                     "//p[.//b[text()='项目状态变更流程']]/preceding-sibling::button//i[@class='el-icon']"]
    # 跳转到我的待办中，并筛选资料互提流程流程
    my_todo_process_filter_data = [By.XPATH,
                                   "//p[.//b[text()='资料互提流程流程']]/preceding-sibling::button//i[@class='el-icon']"]
    # 设校审流程的数量
    my_todo_process_filter_prepare_num = [By.XPATH, "//p[.//b[text()='设校审流程']]/following-sibling::span//b"]
    # 项目状态变更流程的数量
    my_todo_process_filter_status_num = [By.XPATH, "//p[.//b[text()='项目状态变更流程']]/following-sibling::span//b"]
    # 资料互提流程的数量
    my_todo_process_filter_data_num = [By.XPATH, "//p[.//b[text()='资料互提流程流程']]/following-sibling::span//b"]
    # 项目概览中的未激活
    project_overview_unactivated = [By.XPATH, "//div[./span[text()='未激活']]/following-sibling::span//b"]
    # 项目概览中的进行中
    project_overview_underway = [By.XPATH, "//div[./span[text()='进行中']]/following-sibling::span//b"]
    # 项目概览中的已暂停
    project_overview_suspended = [By.XPATH, "//div[./span[text()='已暂停']]/following-sibling::span//b"]
    # 项目概览中的已终止
    project_overview_terminated = [By.XPATH, "//div[./span[text()='已终止']]/following-sibling::span//b"]
    # 项目概览中的已完成
    project_overview_completed = [By.XPATH, "//div[./span[text()='已完成']]/following-sibling::span//b"]

    # 工时管理
    work_time_management = [By.XPATH, "//span[text()='工时管理']"]

    # 技术支持
    technical_support = [By.XPATH, "//span[text()='技术支持']"]
    # 培训手册
    training_manual = [By.XPATH, "//li[text()='培训手册']"]
    # 培训视频
    training_video = [By.XPATH, "//li[text()='培训视频']"]
    # 支持人员
    support_staff = [By.XPATH, "//li[text()='支持人员']"]

    # 意见与建议
    suggestion = [By.XPATH, "//span[text()='意见与反馈']"]
    # 意见反馈
    suggestion_feedback = [By.XPATH, "//li[text()='意见反馈']"]
    # 意见清单
    suggestion_list = [By.XPATH, "//li[text()='意见清单']"]
    # 系统评分
    system_score = [By.XPATH, "//li[text()='系统评分']"]
    # 评分结果
    score_result = [By.XPATH, "//li[text()='评分结果']"]

    # 消息中心，还包括了消息的数量
    message = [By.XPATH, "//div//sup"]
    # 消息中设校审流程数量，该数量是一个string类型，类似'(11)'，所以需要做数据处理
    message_my_todo_process_num = [By.XPATH, "//li//span[text()='设校审流程']/following-sibling::span"]
    # 消息中资料互提流程数量
    message_my_todo_data_num = [By.XPATH, "//li//span[text()='资料互提流程']/following-sibling::span"]
    # 消息中项目状态变更流程数量
    message_my_todo_status_num = [By.XPATH, "//li//span[text()='项目状态变更流程']/following-sibling::span"]
    # 消息中文件下载审批流程数量
    message_my_todo_download_num = [By.XPATH, "//li//span[text()='文件下载审批流程']/following-sibling::span"]
    # 消息中文件下载数量审批流程数量
    message_my_todo_file_num = [By.XPATH, "//li//span[text()='文件下载数量审批流程']/following-sibling::span"]
    # 消息中经验教训流程数量
    message_my_todo_lesson_num = [By.XPATH, "//li//span[text()='经验教训流程']/following-sibling::span"]
    # 消息中专家意见流程数量
    message_my_todo_expert_num = [By.XPATH, "//li//span[text()='专家意见流程']/following-sibling::span"]
    # 消息中文件状态待升版的数量
    message_my_todo_file_upgrade_num = [By.XPATH, "//li//span[text()='文件状态待升版']/following-sibling::span"]

    # 中英文切换键
    language_switch = [By.XPATH, "//div//span[contains(@class,'el-dropdown-lang')]"]
    # 中文选项
    language_chinese = [By.XPATH, "//li[text()='中文']"]
    # 英文选项
    language_english = [By.XPATH, "//li[text()='英文']"]


if __name__ == "__main__":
    run_code = 0
