import pytest
from selenium.webdriver.chrome.service import Service
from Common.data import clear_img, clear_root, read_json_data
from selenium import webdriver
from Common.agent import options, driver_version
from taiga.Common.taiga_log import logger
from taiga.Common.taiga_path import *
from taiga.PageObjects.login_page import LoginPage

login_data = read_json_data(login_data_dir)
default_username = login_data["login_admin_success"]["username"]
default_password = login_data["login_admin_success"]["password"]


@pytest.fixture(scope="session")
def init_taiga():
    clear_root(logs_dir)
    clear_img(screenshot_dir)
    servers = Service(executable_path=driver_version())
    driver = webdriver.Chrome(options=options(), service=servers)
    driver.maximize_window()
    driver.get(login_url)
    logger.info(f"浏览器地址：{login_url}")
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def login_page(init_taiga):
    """
    复杂化init_taiga，多一个登录操作
    """
    LoginPage(logger, screenshot_dir, init_taiga).login(default_username, default_password)
    yield init_taiga


@pytest.fixture(scope="session")
def logout_page(init_taiga):
    """
    登出操作
    """
    yield init_taiga
    LoginPage(logger, screenshot_dir, init_taiga).logout()
