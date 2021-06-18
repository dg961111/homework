import pytest
from pytest0617.calculate import Calculate
from util.read_data import ReadData
from decimal import *

r = ReadData()
data = r.get_yaml_data("calculate.yml")


class TestCalculate:

    def setup_class(self):
        self.cal = Calculate()
        print("计算开始")

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.add
    @pytest.mark.parametrize(data.get("args"), data.get("add_success").get("data"),
                             ids=data.get("add_success").get("ids"))
    def test_add_success(self, a, b, expect):
        if isinstance(a, float) or isinstance(b, float):
            a = Decimal(str(a))
            b = Decimal(str(b))
            expect = Decimal(str(expect))
        assert self.cal.add(a, b) == expect

    @pytest.mark.add
    @pytest.mark.xfail
    @pytest.mark.parametrize(data.get("args"), data.get("add_fail").get("data"), ids=data.get("add_fail").get("ids"))
    def test_add_fail(self, a, b, expect):
        assert self.cal.add(a, b) == expect

    @pytest.mark.div
    @pytest.mark.parametrize(data.get("args"), data.get("div_success").get("data"), ids=data.get("div_success").get("ids"))
    def test_div_success(self, a, b, expect):
        if isinstance(a, float) or isinstance(b, float):
            a = Decimal(str(a))
            b = Decimal(str(b))
            expect = Decimal(str(expect))
        assert self.cal.div(a, b) == expect

    @pytest.mark.div
    @pytest.mark.xfail
    @pytest.mark.parametrize(data.get("args"), data.get("div_fail").get("data"), ids=data.get("div_fail").get("ids"))
    def test_div_fail(self, a, b, expect):
        assert self.cal.div(a, b) == expect
