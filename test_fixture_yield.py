import pytest

class Test_yield():
    def test_yield(self,myfixture2):
        print(f"参数传值：{myfixture2}")

    def test_demo(self):
        print("demo1")