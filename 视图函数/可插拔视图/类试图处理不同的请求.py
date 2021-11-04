# -*- coding: utf-8 -*-
# @Time    : 2021/10/26 20:45
# @Author  : Liu Fei
# @File    : 类试图处理不同的请求.py
# @Software: PyCharm

"""
通过类视图处理不同的请求
"""

from flask import Flask, request
from flask.views import View

app = Flask(__name__)


class ProjecView(View):

    # methods = ['GET', 'POST']  # 限制请求方式的第二种方式

    def get(self):
        return 'get'

    def post(self):
        return 'post'

    # 分配请求， 将不同的请求方式分开处理，不在同一个视图中处理
    def dispatch_request(self):  # 视图类中固定的方法，专用于处理请求。
        dispatch_pattern = {'GET': self.get, 'POST': self.post}
        method = request.method
        return dispatch_pattern.get(method)()


f = ProjecView.as_view('project')
app.add_url_rule('/project', view_func=f, methods=['GET', 'POST'])  # 将类ProjectView通过as_view方法当作视图函数来使用。as_view需要一个参数，即这个视图的名称。

"""
处理不同请求的方式二
from flask import Flask, request
from flask.views import View

app = Flask(__name__)


class ProjecView(View):
    def get(self):
        return 'get'
        
    def post(self):
        return 'post'

    def dispatch_request(self):
        method = request.method
        if method == 'GET'：
        	return self.get()
        elif method == 'POST':
        	return self.post()

f = ProjecView.as_view('project')
app.add_url_rule('/project', view_func=f, methods=['GET', 'POST']) 

if __name__ == '__main__':
    app.run(debug=True)

"""

if __name__ == '__main__':
    app.run(debug=True)
