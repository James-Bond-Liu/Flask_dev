from flask import Flask, abort, request

app = Flask(__name__)

@app.before_request
#每次访问接口都会执行这个函数。before_request不要添加return，当before_request添加return后，后面的视图函数就不会再执行了。
def get_user():
    user = request.args.get('user')
    if user != 'liufei':
        abort(401)

@app.after_request  # 常用来接收视图函数响应体response
def make_res(response):
    print(response)
    response.headers['server'] = 'panda'
    return response

@app.teardown_request  # 常用来接收视图函数错误信息error
def tear_make_res(error):
    print(error)
    print('teardown_****')

@app.before_first_request  # 第一次访问整个服务，会调这个函数
def set_server_name():
    print('the first request')

@app.route('/', methods=['GET', 'POST'])
def index():
    # 1/0
    return 'hello welocme to my world'



if __name__ == '__main__':
    app.run(debug=True)