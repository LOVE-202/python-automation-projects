import requests
import logging



BASE_URL="http://127.0.0.1:5000"
def test_login_and_profile():
    resp=requests.post(
        f"{BASE_URL}/login",
        json={"username":"admin","password":"123456"},
    )
    assert resp.status_code==200
    token=resp.json()["token"]
    logging.info("登陆成功，拿到token：%s",token)



    resp2=requests.get(
        f"{BASE_URL}/profile",
        headers={"Authorization":token},
    )
    assert resp2.status_code==200
    logging.info("profile访问成功，用户名：%s",resp2.json()["username"])
def teest_profile_without_token():
    resp=requests.get(f"{BASE_URL}/profile")
    assert resp.status_code==401
    logging.info("无token访问profile，被拒绝，状态码：%s",resp.status_code)





# def test_profile_without_token():
#     # 不带 token 直接访问 /profile
#     resp = requests.get(f"{BASE_URL}/profile")
#     # 服务器应该拒绝，返回 401
#     assert resp.status_code == 401