import requests



BASE_URL="http://127.0.0.1:5000"
def test_login_and_profile():
    resp=requests.post(
        f"{BASE_URL}/login",
        json={"username":"admin","password":"123456"},
    )
    assert resp.status_code==200
    token=resp.json()["token"]
    resp2=requests.get(
        f"{BASE_URL}/profile",
        headers={"Authorization":token},
    )
    assert resp2.status_code==200
    assert resp2.json()["username"]=="admin"

# def test_profile_without_token():
#     # 不带 token 直接访问 /profile
#     resp = requests.get(f"{BASE_URL}/profile")
#     # 服务器应该拒绝，返回 401
#     assert resp.status_code == 401