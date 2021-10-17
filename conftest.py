import pytest


@pytest.fixture(params=[1, 2, {"a": 1, "b": 2}, (1, 2, 3)])
def myfixture1(request):
    return request.param
