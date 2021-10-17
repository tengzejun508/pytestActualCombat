import pytest


# 参数化
def function(a, b):
    return a + b


# 第一个参数要与所传参数的个人及名称相同，第二个参数传列表数据
@pytest.mark.parametrize("a, b", [(1, 2), (3, 4)])
def test_demo(a, b):
    assert function(a, b) == a + b


# ids添加别名
@pytest.mark.parametrize("a, b", [(1, 2), (3, 4)], ids=('aa', 'bb'))
def test_demo2(a, b):
    assert function(a, b) == a + b


# 参数分开，执行的次数为笛卡尔积
@pytest.mark.parametrize("a", (1, 2, 3))
@pytest.mark.parametrize("b", (4, 5, 6))
def test_demo3(a, b):
    print(f"测试数据组合a----》{a},b---->{b}")
