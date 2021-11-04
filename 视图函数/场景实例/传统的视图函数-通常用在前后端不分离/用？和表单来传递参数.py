# 通过？号和表单来传递参数

from flask import Flask, request

app = Flask(__name__)

@app.route('/projects/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def projects1():
    methods = request.method
    project_id = request.form.get('p_id')
    if methods in ['POST', 'PUT', 'DELETE'] and project_id is None:
        return 'not allowed'
    if methods == 'GET':
        project_id = request.args.get('p_id')
        if project_id is None:
            return 'get all projects'
        else:
            return f'get {project_id}'

    elif methods == 'POST':
        return f'POST {project_id}'
    return 'hello everyone'

#
# @app.route('/projects/', methods=['GET'])
# def projects2():
#     return 'get all projects'

app.run(debug=True)