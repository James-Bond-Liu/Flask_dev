# -*- coding: utf-8 -*-
# @Time    : 2021/10/24 13:45
# @Author  : Liu Fei
# @File    : urls.py
# @Software: PyCharm

from 路由.视图函数的分离.run import app
from 路由.视图函数的分离 import views

app.add_url_rule('/', view_func=views.index)
app.add_url_rule('/hi', view_func=views.hi)