# -*- coding: utf-8 -*-
# @Time    : 2021/10/23 7:57
# @Author  : Liu Fei
# @File    : 路由重定向.py
# @Software: PyCharm

"""
路由后多一个斜杠/和少一个斜杠/的区别
"""
from flask import Flask, request

app = Flask(__name__)

# flask哲学，/cases/和/cases/ 是两个不同的URL

@app.route('/cases')  # 只能通过“/cases”去访问
def getcase1():
    return 'hello'

@app.route('/cases/')  # 可以给通过”/cases“和”/cases/“两个路径访问
# 当用/cases访问时，响应状态码为308 PERMANENT REDIRECT 永久重定向，同时会相应一个location
# 浏览器收到308，会重新访问location
def getcase2():
    return 'hi'

if __name__ == '__main__':
    app.run()