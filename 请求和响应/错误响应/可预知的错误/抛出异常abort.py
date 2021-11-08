# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/7 14:59
@Auth ： Liu Fei
@File ：抛出异常abort.py
@IDE ：PyCharm
"""
import json

from flask import Flask, redirect, request, url_for, render_template, make_response, abort

app = Flask(__name__)

# 将401的报错处理单独写出来，用app.errorhandler来处理
# @app.errorhandler(401)  # 全局处理401的异常
# def server_error(error):
#     return render_template('user_error_401.html'), 401

@app.route('/index1', methods=['GET', 'POST'])
def index1():
    if request.args.get('username') is None:
        data = {"username": "dog"}
        res = make_response(json.dumps(data), 201, {"content-type": "application/json"})
        abort(make_response(render_template('user_error_401.html'),401))  # 自定义401的响应信息
    return render_template('index.html')


@app.route('/index2', methods=['GET', 'POST'])
def index2():
    if request.args.get('username') is None:
        abort(401)  # 此处抛出异常401，然后errorhandler会全局处理401的异常
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
