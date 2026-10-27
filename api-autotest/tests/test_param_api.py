import pytest
import requests


BASE_URL="http://127.0.0.1:5000"

@pytest.mark.parametrize("user_id,expected_name",[
    (1,"Tom"),
    (2,"Jerry"),
])
def test_get_user_by_id(user_id,expected_name):
    resp=requests.get(f"{BASE_URL}/users/{user_id}")
    assert resp.status_code==200
    assert resp.json()["name"]==expected_name