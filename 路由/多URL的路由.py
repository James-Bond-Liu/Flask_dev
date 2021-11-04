# -*- coding: utf-8 -*-
# @Time    : 2021/10/20 19:02
# @Author  : Liu Fei
# @File    : 多URL的路由.py
# @Software: PyCharm
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
@app.route('/hello/<name>')
def index(name=None):
    if name == None:
        return 'hello python'
    else:
        h = 'weclome to my world'
        return h


if __name__ == '__main__':
    app.run(debug=True)