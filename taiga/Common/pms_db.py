# @Create Date: 2025/6/18
# @Author: ganlu
from Common.db import HandelDb
from Common.config import conf
from pms.Common.pms_log import logger

db = HandelDb(conf.get("pms", "host"),
              conf.getint("pms", "port"),
              conf.get("pms", "user"),
              conf.get("pms", "password"),
              logger)

if __name__ == '__main__':
    sql = "select * from wp_user_service.sys_role"
    print(db.get_count(sql))
