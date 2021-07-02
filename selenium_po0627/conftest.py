from datetime import datetime

import pytest
from selenium_po0627.Pages.base_page import BasePage


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
