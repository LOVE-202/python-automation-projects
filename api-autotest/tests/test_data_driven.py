import requests
import pytest
import yaml
from pathlib import Path


BASE_URL="http://127.0.0.1:5000"
DATA_FILE=Path(__file__).parent.parent/ "data"/"users.yaml"
with open(DATA_FILE,encoding="utf-8")as f:
    cases=yaml.safe_load(f)
@pytest.mark.parametrize("case",cases)
def test_get_user_by_id(case):
    resp=requests.get(f"{BASE_URL}/users/{case['user_id']}")
    assert resp.status_code==200
    assert resp.json()["name"]==case["expected_name"]