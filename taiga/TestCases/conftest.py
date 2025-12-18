# @Create Date: 2025/6/18
# @Author: ganlu
import time

import pytest
from selenium.webdriver.chrome.service import Service

from Common.data import clear_img, clear_root
from selenium import webdriver
from Common.agent import options, driver_version
from pms.Common.pms_log import logger
from pms.Common.pms_path import logs_dir, screenshot_dir
from pms.TestDatas import login_datas as gd
from pms.PageObjects.login_page import LoginPage


@pytest.fixture(scope="session")
def init_pms():
    clear_root(logs_dir)
    clear_img(screenshot_dir)
    servers = Service(executable_path=driver_version())
    driver = webdriver.Chrome(options=options(), service=servers)
    driver.maximize_window()
    driver.get(gd.login_url)
    logger.info(f"浏览器地址：{gd.login_url}")
    # time.sleep(1)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def login_page(init_pms):
    """
    复杂化初始driver，多一个登录操作
    """
    LoginPage(logger, screenshot_dir, init_pms).login(gd.login_success["username"], gd.login_success["password"])
    yield init_pms

