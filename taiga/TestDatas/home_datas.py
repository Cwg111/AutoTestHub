#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :home_datas.py
# @Time      :2025/11/20 17:28
# @Author    :ChenWenGang
import os.path

base_url = "http://cppe-pm/#/"
home_url = os.path.join(base_url, "home")
# 我的待办页面网址
my_todo_process_url = os.path.join(base_url, "myFlow/todoFlow/todoList")
# 项目列表页面网址
project_list_url = os.path.join(base_url, "projectList")
if __name__ == "__main__":
    run_code = 0
