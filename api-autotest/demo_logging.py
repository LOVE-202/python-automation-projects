import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logging.debug("这是一条调试信息")
logging.info("这是一条普通信息")
logging.warning("这是一条警告")
logging.error("这是一条错误")