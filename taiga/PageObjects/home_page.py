#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :home_page.py
# @Time      :2025/11/20 17:10
# @Author    :ChenWenGang
from Common.basepage import BasePage
from pms.PageLocators.home_page_locators import HomePageLocators as loc
from pms.TestDatas import home_datas as hd


class HomePage(BasePage):
    """
    首页元素操作类
    """
    def return_home(self):
        """
        从项目列表页面返回到首页
        :return:
        """
        self.click_element(loc.return_home, "点击回到首页")
        self.wait_page_url_change(hd.project_list_url)

    def go_my_todo_process(self):
        """
        跳转到我的待办
        :return:
        """
        self.click_element(loc.my_todo_process, "点击首页中我的待办")

    def go_project_list(self):
        """
        跳转到项目列表
        :return:
        """
        self.click_element(loc.project_list, "点击首页中项目列表")
        self.wait_page_url_change(hd.home_url)

    def click_look_all(self):
        """
        点击查看所有
        :return:
        """
        self.click_element(loc.look_all, "点击查看所有")


if __name__ == "__main__":
    run_code = 0
