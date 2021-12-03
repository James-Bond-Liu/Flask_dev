import pymysql
from flask import Flask, g, request, abort

app = Flask(__name__)

@app.before_request
def get_user():
    sign = request.args.get('user')
    if sign != 'liufei':
        abort(401)
    else:
        a = sign+'md5'  # 相当于用户的token
        g.user = a  # 存储一个key='user',value='a'到全局变量g中

@app.route('/', methods=['GET', 'POST'])
def index():
    print(g.user)  # 调用g全局变量中的值
    return 'Hello world'


if __name__ == '__main__':
    app.run(debug=True)
