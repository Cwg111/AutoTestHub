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


def get_latest_project_name():
    """
    在数据库中查询最新创建的项目的名称
    """
    sql = "select p.name from projects_project p  order by created_date desc limit 1;"
    logger.info(f"sql语句：{sql}")
    return db.select_one_data(sql)[0]


if __name__ == '__main__':
    test_sql = "select id,username,is_active from users_user where username='test_userA';"
    logger.info(f"sql语句：{test_sql}")
    logger.info(f"查询结果：{db.select_one_data(test_sql)}")
    print(f"当前最新创建的项目名称是：{get_latest_project_name()}，类型为：{type(get_latest_project_name())}")
