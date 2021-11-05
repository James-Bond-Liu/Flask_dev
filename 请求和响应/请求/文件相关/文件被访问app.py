from flask import Flask, send_from_directory
app = Flask(__name__)

@app.route('/load/<file_name>')
def load(file_name):
    return send_from_directory(directory='static', path=r'G:\python_files\请求和响应\请求\文件相关', filename=file_name)  # 将文件返回给前端浏览

if __name__ == '__main__':
    app.run(debug=True)