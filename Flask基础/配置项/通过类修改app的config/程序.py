from flask import Flask, request, render_template
import 配置类

app = Flask(__name__)
app.config.from_object(配置类.BaseConfig)


@app.route('/')
def hello():
    return 'hello, welcome to my python world'

if __name__ == '__main__':
    app.run()