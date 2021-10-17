import pytest
import yaml


def get_datas():
    with open("./datas.yml") as f:
        dataAll = yaml.safe_load(f)
        print(dataAll)
        datas = dataAll["datas"]
        myid = dataAll["myid"]
        print(f"datas获取数据“{datas}")
        return [datas, myid]
def addFunction(a, b):
    return a + b

class Test_add():
    @pytest.mark.parametrize("a,b,expect",get_datas()[0],ids=get_datas()[1])
    def testAdd(self,a,b,expect):
        assert  expect == addFunction(a,b)