# -*- coding: utf-8 -*-
# @Time    : 2021/10/9 17:17
# @Author  : Liu Fei
# @File    : web服务器作业.py
# @Software: PyCharm

"""
利用simple_server服务器，具备以下功能：
1、定义3个url，‘/’首页，‘/login’登录，‘/projects'项目
2、对三个url做出对应的响应
3、如果访问不在指定的3个url，报404错误
"""

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
        start_reponse('404 not found', [('content-type', 'text/plain')])
        return [b'page not found']

    resp = patterns.get(url)
    if resp is None:
        start_reponse('404 not found', [('content-type', 'text/plain')])
        return [b'page not found']
    start_reponse('200 ok', [('content-type', 'text/plain')])
    return [resp(params).encode()]


server = make_server("", 6001, app)  # 创建一个web服务器
server.serve_forever()  # 启动这个web服务器
