from flask import Flask,abort,render_template,flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'djfks'

@app.route('/')
def index():
    projects = [
        {"name":"项目1", "interface_num":11, "create_time":"2021/1/09"},
        {"name": "项目2", "interface_num": 22, "create_time": "2021/1/10"},
        {"name": "项目3", "interface_num": 33, "create_time": "2021/1/11"}
    ]

    flash('欢迎来到首页')  # 用flash来实现消息闪现，注意必须配置app.config['SECRET_KEY']配置项

    # render_template中的**context，上下文管理器。我们可以在后端render_template处添加关键字参数，然后在前端直接获取。
    # 渲染模版时有两种传递参数的方式：用 var='value' 传递一个参数；使用字典组织多个参数，并且加两个**号转换成关键字参数传入。
    return render_template('index.html', **{"p":projects, "title":'模板渲染'})  # return render_template('index.html', p = projects, title = '模板渲染')


if __name__ == '__main__':
    app.run(debug=True)