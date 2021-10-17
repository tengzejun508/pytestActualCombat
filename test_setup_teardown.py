# -- coding: utf-8 --
# setup和teardown的使用
import pytest


def setup_module():
    print("整个test_setup_tesrdown模块开始执行一次")


def teardown_module():
    print("整个test_setup_tesrdown模块结束执行一次")


def setup_function():
    print("执行类外面的方法之前执行")


def teardown_function():
    print("执行类外边方法执行结束之后执行")


def test_three():
    print("test_three")


def test_four():
    print("test_four")


class Test_setup_tesrdown():

    def setup_class(self):
        print("在执行类里面所有用例之前执行")

    def teardown_class(self):
        print("在执行类里面所有测试用例之后")

    def setup_method(self):
        print("在执行每个测试用例之前执行")

    def teardown_method(self):
        print("在执行每个测试用例之后执行")

    def test_one(self):
        print("test_one")

    def test_two(self):
        print("test_two")
