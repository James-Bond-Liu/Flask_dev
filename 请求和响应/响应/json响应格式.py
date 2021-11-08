import json

from flask import Flask, jsonify
"""
json的响应格式，响应数据的key和value字符串必须用"双引号。
"""
app = Flask(__name__)
# 第一种方式，使用json.dumps()将字典转化为json
@app.route('/index1', methods = ['GET', 'POST'])
def index1():
    data = {"username":"panda"}
    return json.dumps(data), 201, {"content-type":"application/json"}

# 第二中方式，使用jsonify方法
@app.route('/index2', methods = ['GET', 'POST'])
def index2():
    data = {"username":"panda"}
    res = jsonify(data)  # jsonify方法将字典转化为json格式，同时添加"content-type":"application/json"
    res.status = '201'
    # res.status_code=201
    return res
