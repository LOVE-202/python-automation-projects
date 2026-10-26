import pytest
import requests

# 测试端统一使用的服务地址
BASE_URL = "http://127.0.0.1:5000"


@pytest.fixture(autouse=True)
def reset_data():
    # 每个测试开始前，调用 /reset 接口，把服务端数据恢复成初始状态
    requests.post(f"{BASE_URL}/reset")
    # yield 之前是“测试前做的事”；这里没有“测试后要做的事”，直接结束
    yield
