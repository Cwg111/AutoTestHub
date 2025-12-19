import logging


class MyLogger(logging.Logger):
    """
    日志输出封装
    """
    def __init__(self, conf, log_name, file=None):
        """
        设置日志输出级别，日志名称，输出渠道
        :param log_name: 显示日志名称
        :param file: 输出日志名称
        :param conf: 项目配置文件读取操作
        """
        super().__init__(conf.get("log", log_name), conf.get("log", "level"))
        # 设置输出内容格式
        fmt = "%(asctime)s %(name)s %(levelname)s %(filename)s %(lineno)d line:  %(message)s"
        formatter = logging.Formatter(fmt)
        # 日志格式绑定到渠道
        # 设置输出渠道
        handle1 = logging.StreamHandler()  # 输出到控制台
        handle1.setFormatter(formatter)
        self.addHandler(handle1)
        if file:
            handle2 = logging.FileHandler(file, encoding="utf-8", mode='w')
            handle2.setFormatter(formatter)
            self.addHandler(handle2)
