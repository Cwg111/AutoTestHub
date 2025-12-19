from Common.db import HandelDb
from Common.config import conf
from taiga.Common.taiga_log import logger

db = HandelDb(conf.get("taiga", "host"),
              conf.getint("taiga", "port"),
              conf.get("taiga", "user"),
              conf.get("taiga", "password"),
              conf.get("taiga", "database"),
              logger)

if __name__ == '__main__':
    pass
