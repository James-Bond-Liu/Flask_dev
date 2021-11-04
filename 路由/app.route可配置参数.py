# -*- coding: utf-8 -*-
# @Time    : 2021/10/24 10:33
# @Author  : Liu Fei
# @File    : app.route可配置参数.py
# @Software: PyCharm
from flask import Flask, redirect

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'], endpoint='demo')
# route源码只有两个参数，rule-路由地址，options-关键字参数（methods、endpoint、defaults、redirect_to等）
# methods 只当请求方法
# endpoint 指定端点的名称，默认为视图函数的名称
def index():
    return 'hello, 张景小仙女'
print(app.url_map)
# 集中注册--项目很大时使用
# app.add_url_rule('/', view_func=index, methods=['POST', 'GET'])  # 参数1为配置的路由,参数2为和路由相关联的视图函数名,注意函数不要加()

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

# defaults默认参数
# 指定默认参数值方式一
@app.route('/hi1', defaults={'id':3})  # 指定一个默认参数
def hi1(id):
    return f'hi{id}'
# 指定默认参数值方式二
@app.route('/hi2')
def hi2(id=3):  # 指定一个默认参数
    return f'hi{id}'
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)