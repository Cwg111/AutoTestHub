# @Create Date: 2023/10/24
# @Author: ganlu
import pymysql
import psycopg2


class HandelDb:
    """
    封装数据库连接
    """
    def __init__(self, host, port, user, pwd, log, database=None, types="mysql"):
        """
        连接数据库，创建游标
        默认为MYSQL数据库
        :param types: 数据库类型
        :param host: 地址
        :param port: 端口
        :param user: 用户
        :param pwd: 密码
        :param log: 日志
        :param database: 库名称
        :return:
        """
        # 连接pg数据库
        if types == "pg":
            self.conn = psycopg2.connect(
                host=host,
                port=port,
                user=user,
                password=pwd,
                database=database
            )
        else:
            self.conn = pymysql.connect(
                host=host,
                port=port,
                user=user,
                password=pwd,
                charset='utf8',
                cursorclass=pymysql.cursors.DictCursor
            )
        self.logger = log
        # 创建游标
        self.cur = self.conn.cursor()

    def select_one_data(self, sql):
        """
        获取一条数据
        :param sql: sql语句
        :return:
        """
        self.conn.commit()  # 同步数据库
        self.cur.execute(sql)
        return self.cur.fetchone()

    def select_some_data(self, sql, num):
        """
        获取几条数据
        :param sql:
        :return:
        """
        self.conn.commit()
        self.cur.execute(sql)
        return self.cur.fetchmany(num)

    def select_all_data(self, sql):
        """
        获取所有的数据
        :param sql:
        :return:
        """
        self.conn.commit()
        self.cur.execute(sql)
        return self.cur.fetchall()

    def get_count(self, sql):
        """
        获取查询结果的条数
        :param sql:
        :return:
        """
        self.logger.info("sql语句：{}".format(sql))
        self.conn.commit()
        self.cur.execute(sql)
        return self.cur.rowcount

    def update(self, sql):
        """
        更新数据
        :param sql:
        :return:
        """
        self.logger.info("sql语句：{}".format(sql))
        self.cur.execute(sql)
        self.conn.commit()

    def close(self):
        """
        关闭连接
        :return:
        """
        self.cur.close()
        self.conn.close()
