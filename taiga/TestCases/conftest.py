import pytest
from selenium.webdriver.chrome.service import Service
from Common.data import clear_img, clear_root, read_json_data
from selenium import webdriver
from Common.agent import options, driver_version
from taiga.Common.taiga_log import logger
from taiga.Common.taiga_path import logs_dir,login_url,screenshot_dir,login_data_dir,home_url
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
    复杂化init_taiga，多一个登录操作，供其他页面（非登录页）使用
    """
    login_page = LoginPage(logger, screenshot_dir, init_taiga)
    # 执行登录
    login_page.login(default_username, default_password)
    # 简单断言：保证登录成功（前置条件，失败则直接终止）
    login_page.wait_page_url_change(login_url)  # 先等待登录页面加载完成
    assert login_page.get_page_url() == home_url
    logger.info("登录成功")
    yield init_taiga


@pytest.fixture(scope="function")
def clean_login_state(init_taiga):
    """
    登录用例专用，轻量清理状态：清cookie+回登录页
    """
    init_taiga.delete_all_cookies()  # 清cookie
    init_taiga.get(login_url)  # 返回登录页面
    logger.info("清理登录状态成功")
    yield init_taiga
