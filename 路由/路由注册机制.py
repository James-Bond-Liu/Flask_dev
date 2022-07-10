# -*- coding: utf-8 -*-
# @Time    : 2021/10/23 8:49
# @Author  : Liu Fei
# @File    : 路由注册机制.py
# @Software: PyCharm
from flask import Flask, request

"""
路由注册方式：
1、利用装饰器注册@app.route()
2、集中注册机制
"""

app = Flask(__name__)

print(app.url_map)  # Map([<Rule '/static/<filename>' (GET, OPTIONS, HEAD) -> static>])  未注册路由之前只有一个绑定关系，静态文件。URL即/static/<filename>，端点名即static

@app.route('/cases')  # 装饰器注册,小项目使用
def getcase1():
    return 'hello'

print(app.url_map)  # Map([<Rule '/static/<filename>' (GET, OPTIONS, HEAD) -> static>])
# Map([<Rule '/cases' (GET, OPTIONS, HEAD) -> getcase1>, <Rule '/static/<filename>' (GET, OPTIONS, HEAD) -> static>]) 注册路由后增加一条绑定关系。URL即/cases，端点名即getcase1，(GET, OPTIONS, HEAD)为注册时添加的参数

# 集中注册--项目很大时使用
#app.add_url_rule(rule = '/', view_func=getcase2)
# app.add_url_rule(rule = '/cases/', view_func=getcase1)  # 参数1为配置的路由,参数2为和路由相关联的视图函数名,注意函数不要加()

if __name__ == '__main__':
    app.run(debug=True)