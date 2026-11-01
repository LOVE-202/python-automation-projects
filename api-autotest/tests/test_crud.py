


def test_create_user(client):
    # 新增一个用户，期望返回 201 表示创建成功
    resp = client.post(
        "/users",
        json={"name": "Bob", "age": 25},
    )
    assert resp.status_code == 201
    assert resp.json()["name"] == "Bob"


def test_update_user(client):
    # 修改 2 号用户的年龄为 18
    resp = client.put(
        "/users/2",
        json={"age": 18},
    )
    assert resp.status_code == 200
    assert resp.json()["age"] == 18


def test_delete_user(client):
    # 删除 1 号用户
    resp = client.delete("/users/1")
    assert resp.status_code == 200
    # 删除后再查列表，应该只剩 1 个用户
    resp2 = client.get("/users")
    assert len(resp2.json()) == 1
