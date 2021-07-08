from datetime import datetime
import pytest
from appium0704.Pages.app import App


@pytest.fixture(scope="class")
def create_app():
    global c_app
    c_app = App()
    yield c_app
    c_app.quit()


@pytest.fixture()
def app(create_app):
    create_app.start()
    yield create_app.switch_to_base()


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
        c_app.fail_picture(item.location[2] + datetime.now().strftime('%H%M%S%f'))
