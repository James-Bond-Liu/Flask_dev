from flask import Flask,request
from flask.views import View, MethodView

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    a = request
    # get请求的请求数据
    get_data = request.args

    # 表单数据
    form_data = request.form

    # json数据，请求头 application/json
    json_data = request.json

    #file文件数据
    file_data = request.files

    #
    return 'index '

if __name__ == '__main__':
    app.run(debug=True)
