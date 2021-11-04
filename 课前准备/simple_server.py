# -*- coding: utf-8 -*-
# @Time    : 2021/10/9 5:30
# @Author  : Liu Fei
# @File    : simple_server.py
# @Software: PyCharm

"""
搭建服务
监听动作，while 0，1
处理程序
返回数据到套接字，生成一个响应对象
"""
from wsgiref.simple_server import make_server

def app(env, start_reponse):  # application，处理程序
    # env 获取请求相关数据
    # 状态码，header
    start_reponse('200 ok', [('content-type', 'text/application')])

    return [b'hello']  # 页面的返回内容必须一bytes格式返回

server = make_server("", 6001, app)  # 创建一个web服务器
server.serve_forever()  # 启动这个web服务器

