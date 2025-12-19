import datetime
import os
import pywinauto
from Common.config import conf
from Common.path import export_dir
from pywinauto.keyboard import send_keys

"""
日志图片输出限制
"""


def clear_root(logs_dir):
    """
    输出日志数量个数
    总个数放在web.ini配置文件
    :param logs_dir: 日志保存路径
    :return:
    """
    count = len(os.listdir(logs_dir))
    while count > int(conf.get("log", "num")):
        os.remove(os.path.join(logs_dir, os.listdir(logs_dir)[0]))
        count -= 1


def clear_img(screenshot_dir, is_all=None):
    """
    清除图片
    :param screenshot_dir: 截图保存路径
    :param is_all: 默认为不清除全部，即is_all未赋值，还是None时
    :return:
    """
    times = datetime.datetime.today()
    now_time = times.strftime("%Y-%m-%d")
    if is_all:
        for file in os.listdir(screenshot_dir):
            file_path = os.path.join(screenshot_dir, file)
            os.remove(file_path)
    else:
        for file in os.listdir(screenshot_dir):
            if now_time not in file:
                os.remove(os.path.join(screenshot_dir, os.listdir(screenshot_dir)[0]))


def check_download_file(file_name):
    """
    下载文件校验，跟存放下载文件夹中的第一个文件
    :param file_name: 文件名称
    :return:
    """
    print(f"已下载的文件名称：{os.listdir(export_dir)}")
    try:
        print(f"校验的文件名称：{file_name}")
        assert file_name in os.listdir(export_dir)[0]
    except:
        return False
    else:
        return True
    finally:
        clear_download_file()


def clear_download_file():
    """
    清空已下载的所有文件
    :return:
    """
    for file in os.listdir(export_dir):
        if len(file) > 0:
            os.remove(os.path.join(export_dir, file))


def get_num(data):
    """
    获得页面左下角显示总数的数字
    :param data: 字符串
    :return:
    """
    if isinstance(data, str):
        datas = data.split()
        return datas[1]
    else:
        raise


def get_process_num(data):
    """
    获取消息中不同流程的数量，格式为'(11)'
    """
    if isinstance(data, str):
        num = int(data.replace('(', '').replace(')', ''))
        return num
    else:
        raise


def file_upload(file_path, file_name):
    """
    浏览器应用窗口文件上传
    使用pywinauto库，只能在windows平台使用
    :param file_name: 上传文件名
    :param file_path: 上传文件路径
    :return:
    """
    app = pywinauto.Desktop()
    # 选择上传文件窗口
    dlg = app["打开"]
    # 选择文件地址输入框，点击
    dlg["Toolbar3"].click()
    # 键盘输入上传文件的路径
    send_keys(file_path)
    # 键盘输入回车，打开该路径
    send_keys("{VK_RETURN}")
    # 选中文件名输入框，输入文件名
    dlg["文件名(&N):Edit"].type_keys(file_name)
    # 点击文件上传框打开按钮
    dlg["打开(&O)"].click_input()
