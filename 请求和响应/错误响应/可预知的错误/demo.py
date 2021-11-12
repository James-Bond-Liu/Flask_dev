# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/9 19:53
@Auth ： Liu Fei
@File ：set_for_if_flash.py
@IDE ：PyCharm
"""
from flask import Flask, request, abort

# 实例化app
app = Flask(import_name=__name__)

@app.route('/login', methods=["GET","POST"])
def login():

    if request.args.get('user_name') != 'libai' and request.args.get('user_pwd') != '123':
        abort(404)

    return "login sucess"

# 定义错误处理的方法
@app.errorhandler(404)
def handle_404_error(err):
    """自定义的处理错误方法"""
    # 这个函数的返回值会是前端用户看到的最终结果
    return "出现了404错误， 错误信息：%s" % err

if __name__ == '__main__':
    app.run(debug=True)
