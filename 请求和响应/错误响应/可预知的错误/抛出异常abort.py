# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/7 14:59
@Auth ： Liu Fei
@File ：抛出异常abort.py
@IDE ：PyCharm
"""
from flask import Flask, redirect, request, url_for, render_template, make_response, abort

app = Flask(__name__)

# 将404的报错处理单独写出来，用app.errorhandler来处理
@app.errorhandler(404)
def server_error(error):
    return render_template('user_error_404.html'), 404

@app.route('/index1', methods=['GET', 'POST'])
def index1():
    if request.args.get('username') is None:
        abort(make_response(render_template('user_error_404.html'), 404))
        return render_template('index.html')


@app.route('/index2', methods=['GET', 'POST'])
def index2():
    if request.args.get('username') is None:
        abort(404)  # 此处抛出异常404，然后errorhandler会全局处理404的异常
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
