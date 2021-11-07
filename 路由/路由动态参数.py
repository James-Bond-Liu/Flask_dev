# -*- coding: utf-8 -*-
# @Time    : 2021/10/23 7:10
# @Author  : Liu Fei
# @File    : 路由动态参数.py
# @Software: PyCharm
from flask import Flask, request

app = Flask(__name__)

# 获取测试用例的程序
# 视图函数获取动态参数方式一
@app.route('/cases/<id>')
# <id> 会匹配所有类型的数据
# <id> 会自动匹配url中/cases/后面的内容例如/cases/1;  /cases/djfklasjd。但是不能匹配到后面多个“/”，/cases/1/name是不能匹配的
def getcase1(id):
    return f"{id}"  # 相当于格式化输出return "{}".format(id"

# 视图函数获取动态参数方式二
@app.route('/cases')
def getcase2():
    arg = request.args.get('id')  # 此方式只能匹配?后面的参数名为“id”的参数
    return "{}".format(arg)

if __name__ == '__main__':
    app.run()