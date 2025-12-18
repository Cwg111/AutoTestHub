# @Create Date: 2024/9/3
# @Author: ganlu
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 浏览器驱动路径
driver_dir = os.path.join(base_dir, "Conf", "chromedriver")
# 当前项目配置文件路径
conf_dir = os.path.join(base_dir, "Conf")
# 文件下载路径
export_dir = os.path.join(base_dir, "Conf", "export")