# -*- coding: utf-8 -*-
# @Time    : 2021/10/24 13:20
# @Author  : Liu Fei
# @File    : run.py
# @Software: PyCharm
from flask import Flask
# from 路由.视图函数的分离 import urls  urls和app两个模块相互导入，会导致循环导入bug

app = Flask(__name__)
# 当可能出现循环导入的情况时，可以将导入代码放在中间。什么时候需要导入再导入，每必要将所有的导入全放在开始行
# from 路由.视图函数的分离 import urls
from 路由.视图函数的分离.urls import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)