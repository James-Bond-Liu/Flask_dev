import json

from flask import Flask, redirect, request, url_for, render_template, make_response, abort

app = Flask(__name__)

class UserError(Exception):  # 自定义一个错误类型，继承错误的基类
    pass

# 当全局出现UserError的错误类型如何处理
@app.errorhandler(UserError)  # 全局处理UserError错误类型
def api_401_error(error):
    return render_template('user_error_401.html',error=error), 401

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.args.get('username') is None:
        raise UserError()  #  抛出自定义的错误类型
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)