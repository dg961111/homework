import time
from datetime import datetime
import pytest
from selenium_po0627.Pages.base_page import BasePage
from settings import LOG_DIR


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.fixture(scope="session", autouse=True)
def manage_logs(request):
    """Set log file name same as test name"""
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    log_name = LOG_DIR + now + '.log'

    request.config.pluginmanager.get_plugin("logging-plugin").set_log_path(log_name)


@pytest.fixture()
def mainPage():
    global base
    base = BasePage()
    yield base
    base.quit()


# 用例失败后自动截图
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    获取用例执行结果的钩子函数
    :param item:
    :param call:
    :return:
    """
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        base.fail_picture(item.location[2] + datetime.now().strftime('%H%M%S%f'))
