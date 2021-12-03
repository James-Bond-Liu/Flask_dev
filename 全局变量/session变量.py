import os

from flask import Flask, request, session, abort

app = Flask(__name__)
# 必须要设置secret_key
app.config['SECRET_KEY']=os.urandom(24)

@app.route('/', methods=['GET', 'POST'])
def home():
    if not session.get('user'):
        abort(401)
    print(session.get('user'))  # 提取session中的值
    return 'hello world'

@app.route('/login', methods=['GET', 'POST'])
def login():
    username=request.args.get("username")
    pwd = request.args.get('pwd')
    if username and pwd:
        session['user'] = username  # 设置session中的键值对
        return '登录成功'
    return '没有登录'

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if session.get('user'):
        session.pop('user', None)  # 删除session，或者session['user']=False
    return '退出'

# 清除session中所有数据
@app.route('/clear')
def clear():
    print (session.get('username'))
    session.clear()   # 清除session中所有数据
    print (session.get('username'))
    return 'success'


if __name__ == '__main__':
    app.run(debug=True)