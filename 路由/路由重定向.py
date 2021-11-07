# -*- coding: utf-8 -*-
# @Time    : 2021/10/23 7:57
# @Author  : Liu Fei
# @File    : 路由重定向.py
# @Software: PyCharm

"""
路由后多一个斜杠/和少一个斜杠/的区别
"""
from flask import Flask, request, redirect

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



@app.route('/', methods=['POST', 'GET'], endpoint='demo')
def index():
    return 'hello, 张景小仙女'
print(app.url_map)

# redirect指定重定向
# 重定向方式一
@app.route('/hello1',redirect_to='/' )  # 此种方式不会执行下面视图函数的代码
def hello1():
    print('****')
    return 'This is hello1'
# 重定向方式二
@app.route('/hello2')
def hello2():
    print('****')  # 此种方式会执行视图函数中的代码
    return redirect('/hello1')  # 此种方式需要导入flask中的redirect方法。




if __name__ == '__main__':
    app.run()