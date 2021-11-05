import os

from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

# 限制上传文件的最大值
app.config["MAX_CONTENT_LENGTH"] = 1024*1024 # 1M

# 限制上传文件的格式
def allowed_format(filename):
    format_list = ['jpg', 'npg', 'md', 'gif']
    file_format = filename.split('.')[-1]
    if file_format in format_list:
        return True
    return False


@app.route('/upload', methods = ['GET', 'POST'])
def upload():
    file = request.files.get('file_name')  # 获取前端上传的文件
    if file is None:
        return render_template('index.html')
    if allowed_format(file.filename):  # 只有当文件格式符合要求时才能存储
        path = os.getcwd()
        file.save(path+secure_filename(file.filename))  # file.filename用来获取文件名称，file.save用来保存文件
        return 'save successful'
    else:
        return 'error'

"""
后端获取文件名是通过URL来获取的。
但假如我们上传的文件名有空格，当文件上传至后台，通过URL获取时，比如文件名“dmeo one.doc”，在URL中体现为“demo%ud%20one.doc”。
此时后端获取文件名与原文件名发生差异。secure_filename(file.filename),用来获取原始文件名。
"""


if __name__ == '__main__':
    app.run(debug=True)