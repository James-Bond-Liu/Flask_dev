from flask import Flask, redirect, request, url_for
app = Flask(__name__)

def server_error(error):
    return '当前系统正在维护，请稍后重试'
# 类似于路由的集中注册
app.register_error_handler(ZeroDivisionError, server_error)

@app.route('/', methods=['GET', 'PSOT'])
def index():
    1/0  # 会报错500，错误描述为ZeroDivisionError
    return 'hello'

if __name__ == '__main__':
    app.run(debug=True)