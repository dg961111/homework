import logging
import allure
import pytest

from settings import DATA_DIR
from util.read_data import ReadData
from decimal import *

r = ReadData()
data = r.get_yaml_data("calculate.yml")


@allure.feature("计算器测试")
class TestCalculate:

    @pytest.mark.add
    @allure.story("加法测试")
    @allure.title("成功: {add_success_data[0]} + {add_success_data[1]} == {add_success_data[2]} ")
    def test_add_success(self, add_success_data, setup_calc):
        a, b, expect = add_success_data
        message = f"断言正确的相加: {a}-{b}-{expect}"
        # 附加一张图片
        with open(DATA_DIR+"test.png", "rb") as f:
            content = f.read()
            allure.attach(content, "测试图片", attachment_type=allure.attachment_type.PNG)
        with allure.step(message):
            logging.info(message)
            assert setup_calc.add(a, b) == expect

    @allure.story("加法测试")
    @pytest.mark.add
    @pytest.mark.xfail
    @allure.title("失败: {add_fail_data[0]} + {add_fail_data[1]} != {add_fail_data[2]} ")
    def test_add_fail(self, add_fail_data, setup_calc):
        a, b, expect = add_fail_data
        message = f"断言错误的相加: {a}-{b}-{expect}"
        with allure.step(message):
            logging.info(message)
            assert setup_calc.add(a, b) == expect

    @pytest.mark.div
    @allure.story("除法测试")
    @allure.title("成功: {div_int_data[0]} / {div_int_data[1]} == {div_int_data[2]} ")
    def test_div_int(self, div_int_data, setup_calc):
        a, b, expect = div_int_data
        message = f"断言整数的除法: {a}-{b}-{expect}"
        with allure.step(message):
            logging.info(message)
            assert setup_calc.div(a, b) == expect

    @pytest.mark.div
    @allure.story("除法测试")
    @allure.title("成功: {div_float_data[0]} / {div_float_data[1]} == {div_float_data[2]} ")
    def test_div_float(self, div_float_data, setup_calc):
        a, b, expect = div_float_data
        message = f"断言小数相除: {a}-{b}-{expect}"
        with allure.step(f"将数据处理为Decimal: {a}-{b}-{expect}"):
            logging.info(f"将数据处理为Decimal: {a}-{b}-{expect}")
            a = Decimal(str(a))
            b = Decimal(str(b))
            expect = Decimal(str(expect))
        with allure.step(message):
            logging.info(message)
            assert setup_calc.div(a, b) == expect

    @pytest.mark.div
    @allure.story("除法测试")
    @allure.title("失败: {div_raise_data[0]} / {div_raise_data[1]}, 报错:{div_raise_data[2]}")
    def test_div_raise(self, div_raise_data, setup_calc):
        a, b, errType = div_raise_data
        message = f"预期相除抛出异常: {a}-{b}-{errType}"
        with allure.step(message):
            logging.info(message)
            with pytest.raises(eval(errType)):
                setup_calc.div(a, b)

