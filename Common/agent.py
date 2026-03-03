import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.driver_cache import DriverCacheManager

from Common.path import driver_dir, export_dir

"""
Chrome浏览器驱动配置
"""

def get_chrome_driver():
    """
    自动匹配Chrome版本，下载驱动到指定的 driver_dir（Conf/chromedriver）
    :return: chromedriver 可执行文件的绝对路径
    """
    # 1. 先确保指定的驱动目录存在，不存在就自动创建（避免报错）
    os.makedirs(driver_dir, exist_ok=True)

    # 2. 初始化驱动管理器，【核心】通过 cache_manager 参数指定下载目录
    cache_manager = DriverCacheManager(driver_dir)
    driver_manager = ChromeDriverManager(cache_manager=cache_manager)

    # 3. 自动执行：检测Chrome版本 → 检查目录里是否已有对应驱动 → 没有就下载 → 有就直接用
    driver_path = driver_manager.install()

    print(f"✅ Chrome驱动已匹配/下载到指定目录：{driver_path}")
    return driver_path


def options():
    """
    添加chrome参数
    :return:
    """
    # 启动浏览器添加设置，通过ChromeOptions类
    option = webdriver.ChromeOptions()
    # 取消chrome受自动控制提示
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
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
    # print(driver_version())
    print(get_chrome_driver())
