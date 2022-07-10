from flask import Flask
app = Flask(__name__)
# 导入配置项
app.config.from_pyfile('setting.py', silent=True)
# silent 默认Flase当配置文件不存在的时候抛出异常，
# 使用silent=True的时候只是会返回False,但是不抛出异常

@app.route('/')
def index():
    return 'hello'

if __name__ == '__main__':
    app.run()