import pytest
from selenium.webdriver.chrome.service import Service
from Common.data import clear_img, clear_root
from selenium import webdriver
from Common.agent import options, driver_version
from taiga.Common.taiga_log import logger
from taiga.Common.taiga_path import logs_dir, screenshot_dir
from taiga.TestDatas import login_datas as gd
from taiga.PageObjects.login_page import LoginPage


@pytest.fixture(scope="session")
def init_taiga():
    clear_root(logs_dir)
    clear_img(screenshot_dir)
    servers = Service(executable_path=driver_version())
    driver = webdriver.Chrome(options=options(), service=servers)
    driver.maximize_window()
    driver.get(gd.login_url)
    logger.info(f"浏览器地址：{gd.login_url}")
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def login_page(init_taiga, user=gd.login_admin_success["username"], password=gd.login_admin_success["password"]):
    """
    复杂化init_taiga，多一个登录操作
    :param: user，要登录账号的用户名，默认使用admin账号
    :param: password，要登录账号的密码，默认使用admin账号
    """
    LoginPage(logger, screenshot_dir, init_taiga).login(user, password)
    yield init_taiga

@pytest.fixture(scope="session")
def logout_page(init_taiga):
    """
    登出操作
    """
    yield init_taiga
    LoginPage(logger, screenshot_dir, init_taiga).logout()
