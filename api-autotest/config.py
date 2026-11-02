# 不同环境的服务地址，key 是环境名，value 是地址
ENVIRONMENTS = {
    "dev": "http://127.0.0.1:5000",
    "test": "http://127.0.0.1:5001",
}

# 当前使用哪个环境，改这里就能切换环境
CURRENT_ENV = "dev"

# 根据 CURRENT_ENV 从 ENVIRONMENTS 里取出对应地址
BASE_URL = ENVIRONMENTS[CURRENT_ENV]

