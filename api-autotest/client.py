import requests
from config import BASE_URL


class ApiClient:
    """统一的接口请求客户端，自动拼上服务地址。"""

    def __init__(self, base_url=BASE_URL):
        # 保存服务地址，供每个请求使用
        self.base_url = base_url

    def get(self, path, **kwargs):
        # 用 self.base_url + path 拼出完整地址，再交给 requests.get
        return requests.get(self.base_url + path, **kwargs)

    def post(self, path, **kwargs):
        return requests.post(self.base_url + path, **kwargs)

    def put(self, path, **kwargs):
        return requests.put(self.base_url + path, **kwargs)

    def delete(self, path, **kwargs):
        return requests.delete(self.base_url + path, **kwargs)
