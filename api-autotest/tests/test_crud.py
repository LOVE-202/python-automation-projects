import requests

# 测试端统一的服务地址
BASE_URL = "http://127.0.0.1:5000"


def test_create_user():
    # 新增一个用户，期望返回 201 表示创建成功
    resp = requests.post(
        f"{BASE_URL}/users",
        json={"name": "Bob", "age": 25},
    )
    assert resp.status_code == 201
    assert resp.json()["name"] == "Bob"


def test_update_user():
    # 修改 2 号用户的年龄为 18
    resp = requests.put(
        f"{BASE_URL}/users/2",
        json={"age": 18},
    )
    assert resp.status_code == 200
    assert resp.json()["age"] == 18


def test_delete_user():
    # 删除 1 号用户
    resp = requests.delete(f"{BASE_URL}/users/1")
    assert resp.status_code == 200
    # 删除后再查列表，应该只剩 1 个用户
    resp2 = requests.get(f"{BASE_URL}/users")
    assert len(resp2.json()) == 1
