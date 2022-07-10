from flask import Flask, redirect, request, url_for, make_response, jsonify

app = Flask(__name__)

# url 和 视图函数  之间有一个绑定关系，叫端点endpoint

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.args.get('username') is None:
        # 直接在redirect中传入url进行重定向
        return redirect('/login', 303)  # 重定向一定要进行返回return 。redirect方法有三个参数（重定向路由，重定向状态码，响应response）
        # redirect 中使用url_for(endpoint名) 进行重定向
        # return redirect(url_for('hhh'))

    # return 'hello'

@app.route('/login', methods = ['GET', 'POST'], endpoint='hhh')
def login():
    return 'login'




if __name__ == '__main__':
    app.run(debug=True)