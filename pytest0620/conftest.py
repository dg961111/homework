# 获取计算器实例
import logging
import pytest
from testedcode.calculate import Calculate
from util.read_data import ReadData

r = ReadData()
data = r.get_yaml_data("calculate.yml")


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
