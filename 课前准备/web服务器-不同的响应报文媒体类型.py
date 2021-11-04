# -*- coding: utf-8 -*-
# @Time    : 2021/10/9 17:17
# @Author  : Liu Fei
# @File    : web服务器作业.py
# @Software: PyCharm

"""
content-type:通知客户端，服务端返回的报文格式
    text/plain--字符串格式
    text/html--HTML格式
    application/json--json格式
"""
import json
from wsgiref.simple_server import make_server


def home(request):
    return 'hello'


def login(request):
    return 'login'


def projects(request):
    return 'projects'


patterns = {
    '/': home,
    '/login': login,
    '/projects': projects
}


def app(env, start_reponse):
    url = env.get('PATH_INFO')
    params = env.get('QUERY_STRING')  # 获取env中的url？后面的前端传入的参数
    if (url is None) or (url not in patterns.keys()):
        # 字符串格式
        # start_reponse('404 not found', [('content-type', 'text/plain')])
        # return [b'page not found']

        # html格式
        # start_reponse('404 not found', [('content-type', 'text/html')])
        # return [b'<p style="color:red">page not found</p>']

        # json格式
        start_reponse('404 not found', [('content-type', 'application/json')])
        msg = {'msg':'page not found'}
        return [json.dumps(msg).encode()]


    resp = patterns.get(url)
    if resp is None:
        start_reponse('404 not found', [('content-type', 'text/plain')])
        return [b'page not found']
    start_reponse('200 ok', [('content-type', 'text/plain')])
    return [resp(params).encode()]


server = make_server("", 6001, app)  # 创建一个web服务器
server.serve_forever()  # 启动这个web服务器
