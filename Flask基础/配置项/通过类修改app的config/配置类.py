class BaseConfig(object):  # 基础配置
    DEBUG = True
    PORT = 11

class TestConfig(BaseConfig):
    DEBUG = True
    port = 22

class DevConfig(BaseConfig):
    DEBUG = True
    port = 33

class ProConfig(BaseConfig):
    DEBUG = False
    port = 8081
