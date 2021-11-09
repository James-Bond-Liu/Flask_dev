import json

from flask import Flask, redirect, request, url_for, render_template, make_response, abort, jsonify

app = Flask(__name__)


class UserError(Exception):  # 自定义一个错误类型，继承错误的基类
    pass


# 当全局出现UserError的错误类型如何处理
@app.errorhandler(UserError)  # 全局处理UserError错误类型
def server_error(error):
    # return render_template('user_error_401.html',error=error), 401
    res = jsonify({"msg": "error:username is None"})
    res.status_code = 401
    return res


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.args.get('username') is None:
        raise UserError()  # 抛出自定义的错误类型和错误内容提示
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
