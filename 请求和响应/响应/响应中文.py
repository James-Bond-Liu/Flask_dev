import json

from flask import Flask, jsonify, make_response

app = Flask(__name__)

# flask中JSON_AS_ASCII默认开启的，当是关闭状态时就可以友好的显示中文
app.config["JSON_AS_ASCII"] = False

# 方式一
@app.route('/index1', methods = ['GET', 'POST'])
def index1():
    data = {"username":"大熊猫"}
    return json.dumps(data, ensure_ascii=False), 201, {"content-type":"application/json"}  # 响应数据以json.dumps更改，想显示中文，需增加参数ensure_ascii=False

# 方式二
@app.route('/index2', methods = ['GET', 'POST'])
def index2():
    data = {"username":"丹顶鹤"}
    return make_response(data), 201, {"content-type":"application/json"}  # 响应数据以make_response构造，想显示中文，需要更改配置项中的"JSON_AS_ASCII"为False

if __name__ == '__main__':

    app.run(debug=True)