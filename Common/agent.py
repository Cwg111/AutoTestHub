# @Create Date: 2023/11/6
# @Project: web
# @Author: ganlu

import os
import time

from webdriver_manager.core.utils import get_browser_version_from_os
from selenium import webdriver
from Common.path import driver_dir, export_dir

"""
Chrome浏览器驱动配置
"""


def driver_version():
    """
    匹配当前chrome驱动版本
    :return:
    """
    # 获取本地chrom浏览器版本
    browser_version = get_browser_version_from_os("google-chrome")
    # 通过本地浏览器版本指定浏览器驱动版本
    browser_driver = browser_version.split(".")[0] + "chromedriver.exe"
    if browser_driver in os.listdir(driver_dir):
        driver_path = os.path.join(driver_dir, browser_driver)
        print("当前Chrome浏览器驱动版本：{}".format(driver_path))
        return driver_path
    else:
        raise print("本地chrome驱动版本：{}，未找到指定的驱动版本！！！".format(browser_version))


def options():
    """
    添加chrome参数
    :return:
    """
    # 启动浏览器添加设置，通过ChromeOptions类
    option = webdriver.ChromeOptions()
    # 76以下版本，取消chrome受自动控制提示
    # option.add_argument("--disable-infobars")
    # 76以上版本，取消chrome受自动控制提示
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    # 无痕模式
    # option.add_argument("--incognito")
    # 驱动器下载文件路径配置
    option.add_experimental_option('prefs', {
        'profile.default_content_settings.popups': 0,  # 禁止弹出窗口
        'download.default_directory': export_dir,  # 设置下载路径，路径不存在会自动创建
        'download.prompt_for_download': False,  # 是否弹窗询问
        'safebrowsing.enabled': False,  # 是否提示安全警告
        'download.directory_upgrade': False,  # 记录下载目录是否被更改
        "credentials_enable_service": False,  # 关闭密码保存
        "profile.password_manager_enabled": False  # 关闭密码保存弹窗
    })
    return option


if __name__ == '__main__':
    pass
