import yaml
import requests
import pytest
from pathlib import Path

SERVER="HTTP://127.0.0.1:5000"
path =Path(__file__).parent.parent/"data"/"search.yaml"
with open(path,encoding="utf-8")as f:
    data=yaml.safe_load(f)
@pytest.mark.parametrize("item",data)
def test_search_user(item):
    resp=requests.get(f"{SERVER}/users/search",
                      params={"name":item["name"]},
                      )
    assert resp.status_code == 200
    assert resp.json()[0]["id"]==item["expected_id"]