import requests

BASE_URL="http://127.0.0.1:5000"

def test_login_wrong_password():
    resp=requests.post(
        f"{BASE_URL}/login",
        json={"username":"admin","password":"654321"},
    )
    assert resp.status_code==401
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
    assert resp2.json()["email"]=="admin@example.com"
