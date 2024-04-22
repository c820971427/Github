import pytest


class Test_login:
    # 测试类
    def setup_class(self):
        print("执行测试类之前，进行环境初始化")

    def test_tc01(self):
        print("---test_login01---")
        assert 1 + 1 == 2

    def test_tc02(self):
        print("---test_login02---")
        assert 1 + 1 == 3

    def teardown(self):
        print("-------测试完成，进行环境清理-------")


if __name__ == '__main__':
    pytest.main(["test_func01.py"])
