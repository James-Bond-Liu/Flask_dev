# -*- coding: utf-8 -*-
# @Time    : 2021/10/11 19:30
# @Author  : Liu Fei
# @File    : 初始flask.py
# @Software: PyCharm

from flask import Flask  # Flask是核心类
from flask import request  # request存储了请求参数、地址等环境信息相当于simple_server中的env环境变量
from flask import render_template  # 返回某个静态文件模板时导入
# 初始化app即application
# Flask类只有一个必须指定的参数，即程序主模块或者包的名字，__name__是系统变量，该变量指的是本python文件的文件名
app = Flask(__name__,  # __name__：导入路径（寻找静态目录与模板目录位置的参数）
            template_folder='templates',  # template_folder参数用于指定模板在哪个目录下，默认templates
            static_folder='static',  # 用于告诉后端程序，程序的静态文件保存目录
            static_url_path='/static'  # 参数值必须以“/”开头，访问静态资源的url前缀，默认值是/static，用于区分用户访问内容是静态资源还是动态路由
            )

# 添加路由（以装饰器的方式添加）
@app.route('/')
# 定义视图函数，view function
def index():
    # 工作流程：1、接收参数 2、调用model层里对应的函数去处理数据 3、构建响应结果
    args = request.args  # 获取请求参数，以字典的形式返回。可以获取表单、file、json数据
    name = args.get('name')
    print(name)

    # return 'hello'  # 返回字符串格式的响应体
    # return '<p style="color:red">hello</p>'  # 返回html内容
    return render_template('index.html')  # 直接将html文件返回

if __name__ == '__main__':
    #运行web服务器
    # app.run()web服务器只是用来调试、测试、开发使用的服务器，是flask自带的服务器。不能用于生产环境中充当服务器，生产环境中应当用nginx、uwsgi服务器
    app.run(debug=True)

