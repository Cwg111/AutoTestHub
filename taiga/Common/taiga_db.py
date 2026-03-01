from Common.db import HandelDb
from Common.config import conf
from taiga.Common.taiga_log import logger

db = HandelDb(
    conf.get("taiga", "host"),
    conf.getint("taiga", "port"),
    conf.get("taiga", "user"),
    conf.get("taiga", "password"),
    logger,
    conf.get("taiga", "database"),
    "pg",
)


def get_latest_project_name() -> str:
    """
    在数据库中查询最新创建的项目的名称
    """
    # 数据库已经指定为taiga，但数据库还有一层public，需要指定public.projects_project，这个是模式，相当于一个文件夹，下面是具体的表
    sql = "select p.name from public.projects_project p  order by created_date desc limit 1;"
    logger.info(f"sql语句：{sql}")
    return db.select_one_data(sql)[0]  # type: ignore


def get_project_member_count(project_name: str) -> int:
    """
    在数据库中查询指定项目的成员数量
    :param project_name: 项目名称
    :return: 成员数量
    """
    sql = f"SELECT user_id FROM public.projects_membership WHERE project_id = (SELECT id from public.projects_project where name='{project_name}')  AND user_id IS NOT NULL;"
    return db.get_count(sql)

def get_all_member_count(project_name: str) -> int:
    """
    在数据库中查询指定项目的所有成员数量，包括邀请失败的成员
    :param project_name: 项目名称
    :return: 所有成员数量
    """
    sql = f"SELECT user_id FROM public.projects_membership WHERE project_id = (SELECT id from public.projects_project where name='{project_name}');"
    return db.get_count(sql)


if __name__ == "__main__":
    test_sql = "select id,username,is_active from public.users_user where username='test_userA';"
    logger.info(f"sql语句：{test_sql}")
    logger.info(f"查询结果：{db.select_one_data(test_sql)}")
    print(
        f"当前最新创建的项目名称是：{get_latest_project_name()}，类型为：{type(get_latest_project_name())}"
    )
    print(
        f"项目测试专用项目的成员数量是：{get_project_member_count('测试专用项目')}，类型为：{type(get_project_member_count('测试专用项目'))}"
    )
