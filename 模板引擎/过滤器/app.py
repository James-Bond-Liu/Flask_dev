from flask import Flask, abort, render_template, flash, session, redirect, url_for
import time
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'djfks'

"""自定义过滤器"""
@app.template_filter('s_time')  # 此过滤器的参数为自定义的过滤器的名字。默认为自定义函数名称。
def strf_time(timestamp):
    return datetime.fromtimestamp(timestamp)
# 集中注册过滤器,位置参数1-被装饰的函数，位置参数2-定义过滤器名称
# app.add_template_filter(strf_time, 's_time')

@app.route('/')
def index():
    projects = [
        {"name": "project", "interface_num": 11, "create_time": time.time()},
        {"name": "project", "interface_num": 22, "create_time": time.time()},
        {"name": "project", "interface_num": 33, "create_time": time.time()}
    ]

    flash('欢迎来到首页')  # 用flash来实现消息闪现，注意必须配置app.config['SECRET_KEY']配置项

    # render_template中的**context，上下文管理器。我们可以在后端render_template处添加关键字参数，然后在前端直接获取。
    # 渲染模版时有两种传递参数的方式：用 var='value' 传递一个参数；使用字典组织多个参数，并且加两个**号转换成关键字参数传入。
    return render_template('index.html', **{"p": projects,
                                            "title": '模板渲染',
                                            })  # return render_template('index.html', p = projects, title = '模板渲染')

@app.route('/login/<username>')
def login(username):
    session['user'] = username  # 使用flask中的session来保存前端传入服务器的数据
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
