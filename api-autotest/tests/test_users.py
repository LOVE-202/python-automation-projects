import requests

# 所有测试都访问同一个服务地址，用常量统一管理，以后换环境只改这里
BASE_URL = "http://127.0.0.1:5000"


# 以 test_ 开头的函数，pytest 才会自动执行
def test_health():
    # 发 GET 请求到健康检查接口
    resp = requests.get(f"{BASE_URL}/health")
    # 断言状态码是 200，表示服务正常
    assert resp.status_code == 200
    # 断言返回内容里的 status 字段是 ok
    assert resp.json()["status"] == "ok"


def test_get_users_count():
    # 获取用户列表
    resp = requests.get(f"{BASE_URL}/users")
    # 初始数据只有 Tom 和 Jerry，所以长度应该是 2
    assert resp.status_code == 200
    assert len(resp.json()) == 2


def test_search_user():
    # 按名字搜索 Tom，params 会自动拼成 ?name=Tom
    resp = requests.get(
        f"{BASE_URL}/users/search",
        params={"name": "Tom"},
    )
    # 第一个结果的 name 应该是 Tom
    assert resp.status_code == 200
    assert resp.json()[0]["name"] == "Tom"
