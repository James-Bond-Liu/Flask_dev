import json

from flask import Flask, request, make_response, render_template

app = Flask(__name__)
# 第一种方式，直接return
@app.route('/index1', methods = ['GET', 'POST'])
def index1():
    # 直接利用return，返回响应。
    # 响应信息是必填的。响应状态码（默认200）和响应头相关信息可填可不填。（默认html）
    data = {"username":"panda"}
    return json.dumps(data), 201, {"content-type":"application/json"}

# 利用make_response方法直接构造。
@app.route('/index2', methods = ['GET', 'POST'])
def index2():
    data = {"username": "dog"}
    res = make_response(json.dumps(data), 201, {"content-type":"application/json"})
    return res

# 利用make_response方法先定义再初始化。
@app.route('/index3', methods = ['GET', 'POST'])
def index3():
    res = make_response()
    res.data = render_template('index.html')  # 返回一个html页面
    # res.status = '203'  # 字符串格式
    res.status_code = 203  # int类型

    # res.headers = {"content-type":"text/html"}
    res.content_type = {"content-type":"text/html"}
    return res



if __name__ == '__main__':
    app.run(debug=True)