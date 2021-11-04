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

def home():
    return 'hello'
def login():
    return 'login'
def projects():
    return 'projects'

def app(env, start_reponse):
    # env 获取请求的地址、环境变量
    # 状态码，header
    if env.get('PATH_INFO') == '/':
        start_reponse('200 ok', [('content-type', 'text/plain')])
        res = home()
        return [res.encode()]
    elif env.get('PATH_INFO') == '/login':
        start_reponse('200 ok', [('content-type', 'text/plain')])
        res = login()
        return [res.encode()]
    elif env.get('PATH_INFO') == '/projects':
        start_reponse('200 ok', [('content-type', 'text/plain')])
        res = projects()
        return [res.encode()]
    else:
        start_reponse('404 not found', [('content-type', 'text/plain')])
        return [b'page not found']


server = make_server("", 6001, app)  # 创建一个web服务器
server.serve_forever()  # 启动这个web服务器


""""
如果出现了很多的条件分支都是==，可以利用字典去封装
"""
from wsgiref.simple_server import make_server

def home():
    return 'hello'
def login():
    return 'login'
def projects():
    return 'projects'
patterns = {
    '/':home,
    '/login':login,
    '/projects':projects
}
def app(env, start_reponse):
    url = env.get('PATH_INFO')
    if (url is None) or (url not in patterns.keys()):
        start_reponse('404 not found', [('content-type', 'text/plain')])
        return [b'page not found']

    resp = patterns.get(url)
    if resp is None:
        start_reponse('404 not found', [('content-type', 'text/plain')])
        return [b'page not found']
    start_reponse('200 ok', [('content-type', 'text/plain')])
    return [resp().encode()]  # encode()函数将字符串转换成bytes格式数据


server = make_server("", 6001, app)  # 创建一个web服务器
server.serve_forever()  # 启动这个web服务器
