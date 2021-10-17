import pytest

# pytest -sv -m "demo" test_mark.py 只执行test_one方法
# pytest -sv -m "demo or smoke" test_mark.py,执行test_one,test_two
# pytest -sv -m "demo and smoke" test_mark.py,只执行test_two
class Test_mark():
    @pytest.mark.demo
    def test_one(self):
        print("testOne")
    @pytest.mark.demo
    @pytest.mark.smoke
    def test_two(self):
        print("testtwo")
