# -*- coding: utf-8 -*-
# @Time    : 2021/10/20 19:10
# @Author  : Liu Fei
# @File    : 其他装饰器装饰视图函数.py
# @Software: PyCharm
from flask import Flask

app = Flask(__name__)

# 其他装饰器
def one(func):
    def two(*args, **kwargs):
        print('**'*30)
        return func(*args, **kwargs)  # 其他装饰器不要return其他值，只能return回视图函数的返回值。否则return的其他值会被包装正响应对象返回给前端。
        # return 'djf;laksjdfoisadj'
    return two

@app.route('/')  # 视图函数装饰器
@one  # 其他装饰器放在视图装饰器最里面，否则其他装饰器不会生效。
def index():
    return 'hello world!'


if __name__ == '__main__':
    app.run(debug=True)