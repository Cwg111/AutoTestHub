from Common.db import HandelDb
from Common.config import conf
from taiga.Common.taiga_log import logger

db = HandelDb(conf.get("taiga", "host"),
              conf.getint("taiga", "port"),
              conf.get("taiga", "user"),
              conf.get("taiga", "password"),
              logger,
              conf.get("taiga", "database"),
              "pg"
              )

if __name__ == '__main__':
    test_sql="select id,username,is_active from users_user where username='test_userA';"
    print(db.select_one_data(test_sql))
