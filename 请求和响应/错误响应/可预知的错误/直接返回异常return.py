# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/7 14:23
@Auth ： Liu Fei
@File ：直接返回异常return.py
@IDE ：PyCharm
"""
from flask import Flask, redirect, request, url_for, render_template

app = Flask(__name__)


def server_error(error):
    return '当前系统正在维护，请稍后重试'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.args.get('username') is None:
        return render_template('user_error_404.html'), 404  # 可预知的错误第一种处理方式，直接return返回响应
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)