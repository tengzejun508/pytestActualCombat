import pytest


@pytest.fixture()
def myfixture():
    print("我的第一个fixture")


class Test_fixture():
    def test_one(self):
        print("test_one")

    def test_two(self, myfixture):
        print("test_two")

    def test_three(self):
        print("test_three")
