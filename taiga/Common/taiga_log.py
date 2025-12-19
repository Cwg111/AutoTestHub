import os
import datetime
from Common.logger import MyLogger
from Common.config import conf
from taiga.Common.taiga_path import logs_dir

if conf.getboolean("log", "file_ok"):
    file_name = os.path.join(logs_dir, conf.get("log", "file_name_pms"))
    now = str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
    logger = MyLogger(conf, "name_pms", file_name + "-{}.log".format(now))
else:
    file_name = None
    logger = MyLogger(conf, "name_pms", file_name)

if __name__ == '__main__':
    logger.warning("警告警告！！！！！")
