# -*- coding: utf-8 -*-
# @Time    : 2021/10/26 20:55
# @Author  : Liu Fei
# @File    : 装饰器装饰类视图.py
# @Software: PyCharm
from flask import Flask, request
from flask.views import View
from time import time

app = Flask(__name__)

# 注意装饰器不能用@符号来装饰类视图
def log_time(f):
    def one(*args, **kwargs):
        print(f'{time()}')
        return f(*args, **kwargs)
    return one


class ProjecView(View):

    def get(self):
        return 'get'

    def post(self):
        return 'post'

    def dispatch_request(self):
        dispatch_pattern = {'GET': self.get, 'POST': self.post}
        method = request.method
        return dispatch_pattern.get(method)()


f = ProjecView.as_view('project')  # 相当于视图函数
log_time(f)  # 装饰器装饰函数的第二种调用方式。显示调用。装饰器装饰类视图时只需要装饰as_view函数就可以了

app.add_url_rule('/project', view_func=f, methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(debug=True)
