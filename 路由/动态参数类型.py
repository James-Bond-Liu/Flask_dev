# -*- coding: utf-8 -*-
# @Time    : 2021/10/23 7:29
# @Author  : Liu Fei
# @File    : 动态参数类型.py
# @Software: PyCharm
from flask import Flask, request

app = Flask(__name__)

@app.route('/cases1/<int:id>')  # 只能匹配/cases/整型数据类型的参数
def getcase1(id):
    return f"{id}"

@app.route('/cases2/<float:id>')  # 只能匹配/cases/浮点型数据类型的参数
def getcase2(id):
    return f"{id}"

@app.route('/cases3/<string:id>')
# 只能匹配/cases/字符串型数据类型的参数。
# 注意url/cases3/name后面不能再加“/”，如/cases3/name/dasdf/djfdk，这是不匹配的
def getcase3(id):
    return f"{id}"

@app.route('/cases4/<path:id>')  # 支持匹配/cases/带有“/”的参数，如/cases4/name/hello/index
def getcase4(id):
    return f"{id}"

if __name__ == '__main__':
    app.run()