# -*- coding: utf-8 -*-
# @Time    : 2021/10/20 19:17
# @Author  : Liu Fei
# @File    : 配置项.py
# @Software: PyCharm
from flask import Flask, Config

app = Flask(__name__)

# 设置配置项 
app.config['DEBUG'] = True
app.config['port'] = 5002

@app.route('/')
def index():
    return 'hello'

# 配置项


if __name__ == '__main__':
    app.run(port=app.config['port'], debug=app.config['DEBUG'])