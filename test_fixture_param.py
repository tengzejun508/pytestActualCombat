import pytest





class Test_fixture_param():
    def test_demo(self, myfixture1):
        print(f"参数值：{myfixture1}")
