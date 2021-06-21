import time
import pytest
import logging
from other.calculate import Calculate
from settings import LOG_DIR
from util.read_data import ReadData

r = ReadData()
data = r.get_yaml_data("calculate.yml")


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        print(item.nodeid)
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.fixture(scope="session", autouse=True)
def manage_logs(request):
    """Set log file name same as test name"""
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    log_name = LOG_DIR + now + '.log'

    request.config.pluginmanager.get_plugin("logging-plugin").set_log_path(log_name)


# 获取计算器实例
@pytest.fixture(scope="module")
def setup_calc():
    cal = Calculate()
    logging.info("=====开始计算====")
    yield cal
    logging.info("=====结束计算====")


# 获取正确相加的参数
@pytest.fixture(params=data.get("add").get("success").get("data"), ids=data.get("add").get("success").get("ids"))
def add_success_data(request):
    return request.param


# 获取错误相加的参数
@pytest.fixture(params=data.get("add").get("fail").get("data"), ids=data.get("add").get("fail").get("ids"))
def add_fail_data(request):
    return request.param


# 获取整数相除的参数
@pytest.fixture(params=data.get("div").get("success").get("int").get("data"),
                ids=data.get("div").get("success").get("int").get("ids"))
def div_int_data(request):
    return request.param


# 获取小数相除的参数
@pytest.fixture(params=data.get("div").get("success").get("float").get("data"),
                ids=data.get("div").get("success").get("float").get("ids"))
def div_float_data(request):
    return request.param


# 获取除法报错的参数
@pytest.fixture(params=data.get("div").get("fail").get("data"),
                ids=data.get("div").get("fail").get("ids"))
def div_raise_data(request):
    return request.param

