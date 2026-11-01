import logging
import requests

BASE_URL="http://127.0.0.1:5000"
def test_loging():
    resp=requests.get(BASE_URL+"/health")
    assert resp.status_code==200
    logging.info("状态码: %s", resp.status_code)