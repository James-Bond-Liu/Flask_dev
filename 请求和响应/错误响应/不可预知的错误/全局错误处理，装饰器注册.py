from flask import Flask, redirect, request, url_for
app = Flask(__name__)

# errorhandler装饰器，是专门用来注册全局错误处理的
@app.errorhandler(500)  # errorhandler的参数可以是状态码，也可以是错误类型描述@app.errorhanler(ZeroDivisionError)
def server_error(error):
    return '当前系统正在维护，请稍后重试'


@app.route('/', methods=['GET', 'PSOT'])
def index():
    1/0  # 会报错500，错误描述为ZeroDivisionError
    return 'hello'

if __name__ == '__main__':
    app.run(debug=True)