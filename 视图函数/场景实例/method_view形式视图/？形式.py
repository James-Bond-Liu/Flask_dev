from flask import Flask, request
from flask.views import MethodView

# ?形式，同一个url，参数以？形式传入
app = Flask(__name__)


class UserView(MethodView):
    def get(self):
        project_id = request.args.get('p_id')
        if project_id is None:
            return f'get all projects'
        return f'get {project_id}'

    def post(self):
        return f'post'

    def put(self):
        project_id = request.form.get('p_id')
        return f'put {project_id}'

    def delete(self):
        project_id = request.form.get('p_id')
        return f'delete {project_id}'


# 此种形式下(请求参数都以？后的参数传入)，大家的路由都一致，所以不需要再分开注册了。
f = UserView.as_view('user')

app.add_url_rule('/projects/', view_func=f, methods=['GET', 'POST', 'PUT', 'DELETE'])

app.run(debug=True)
