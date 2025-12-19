import os
from configparser import ConfigParser
from Common.path import conf_dir


class HandleConfig(ConfigParser):
    """
    封装日志配置参数
    """

    def __init__(self, file_path):
        """
        :param file_path: 日志配置文件路径
        """
        super().__init__()
        self.read(file_path, encoding="utf-8")


# 当前项目的配置文件操作读取
dir_con = os.path.join(conf_dir, "web.ini")
conf = HandleConfig(dir_con)

if __name__ == '__main__':
    print(conf.get("log", "name_pms"))
    print(conf.get("taiga", "host"))
