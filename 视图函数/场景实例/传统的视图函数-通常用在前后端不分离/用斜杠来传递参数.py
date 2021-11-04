# 通过斜杠来传递参数

from flask import Flask, request

app = Flask(__name__)

@app.route('/projects/<project_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def projects1(project_id=None):
    methods = request.method
    if methods == 'GET':
        return f'get {project_id}'
    elif methods == 'POST':
        return f'post {project_id}'

    return 'hello everyone'


@app.route('/projects/', methods=['GET'])
def projects2():
    return 'get all projects'

app.run(debug=True)	