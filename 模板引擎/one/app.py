from flask import Flask,abort,render_template,flash

app = Flask(__name__)

@app.route('/')
def index():
    projects = [
        {"name":"项目1", "interface_num":11, "create_time":"2021/1/09"},
        {"name": "项目2", "interface_num": 22, "create_time": "2021/1/10"},
        {"name": "项目3", "interface_num": 33, "create_time": "2021/1/11"}
    ]

    # render_template中的**context，上下文管理器。我们可以在后端render_template处添加关键字参数，然后在前端直接获取。
    return render_template('index.html', p = projects, title = '模板渲染')

if __name__ == '__main__':
    app.run(debug=True)