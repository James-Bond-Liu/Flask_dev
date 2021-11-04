# -*- coding: utf-8 -*-
# @Time    : 2021/10/26 20:49
# @Author  : Liu Fei
# @File    : 类视图.py
# @Software: PyCharm
from flask.views import View
from flask import Flask,request

app = Flask(__name__)


class UserView(View):
    methods = ['GET', 'POST']  # 类试图中限制前端请求方法的方式二。也可以在add_url_rule中添加请求方式

    def dispatch_request(self):
        return '{}到hello'.format(request.method)


app.add_url_rule('/', view_func=UserView.as_view('user'))  # 实际上将类UserView当作一个视图函数，并起了一个名字。

if __name__ == '__main__':
    app.run()