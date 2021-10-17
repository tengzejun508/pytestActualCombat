from pythoncode.calculator import Calculator
import pytest


class Test_calculator():
    def setup_class(self):
        self.calc = Calculator()
        print("计算开始")

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize("a,b",[(1,2),(3,0),(-1,2)])
    def test_divid(self, a, b):
        print(self.calc.divid(a, b))
