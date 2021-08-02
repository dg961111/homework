import datetime
import logging
import os


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


class Logger:

    def __init__(self):
        # 设置文件名字
        self.filename = "result" + str(datetime.date.today()) + ".log"
        self.logger = logging.getLogger(__name__)
        # 设置日志级别
        self.logger.setLevel(logging.DEBUG)
        # 设置日志format
        self.formatter = logging.Formatter("%(asctime)s|%(levelname)-6s|%(filename)s:%(lineno)-3s|%(message)s",
                                           "%Y-%m-%d-%H:%M")

    def get_logger(self):
        # 判断目录是否存在
        if not os.path.exists("./logs"):
            os.makedirs("./logs")
        log_path = './logs/' + self.filename
        # 添加文件控制器
        file_handler = logging.FileHandler(log_path, encoding="utf-8")
        file_handler.setFormatter(self.formatter)
        self.logger.addHandler(file_handler)
        # 添加流控制器
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(self.formatter)
        self.logger.addHandler(console_handler)

        return self.logger


# 生成实例
log = Logger().get_logger()
