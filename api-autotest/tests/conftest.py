import sys
import logging
from pathlib import Path

import pytest
import requests

# 把 api-autotest 目录加入 sys.path，这样下面才能 import 到 config 和 client
sys.path.insert(0, str(Path(__file__).parent.parent))

from client import ApiClient

# 配置日志：最低显示 INFO 级别，并带上时间和级别
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

# 测试端统一使用的服务地址
BASE_URL = "http://127.0.0.1:5000"


@pytest.fixture(autouse=True)
def reset_data():
    # 每个测试开始前，调用 /reset 接口，把服务端数据恢复成初始状态
    try:
        requests.post(f"{BASE_URL}/reset")
    except requests.exceptions.ConnectionError:
        # 服务没启动时跳过重置，让纯本地练习（fixture、parametrize）也能运行
        pass
    # yield 之前是“测试前做的事”；这里没有“测试后要做的事”，直接结束
    yield


@pytest.fixture
def client():
    # 返回一个统一客户端，测试里用 client.get("/users") 这种写法
    return ApiClient()
