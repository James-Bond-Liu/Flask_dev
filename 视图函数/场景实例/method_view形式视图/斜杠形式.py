from flask import Flask,request
from flask.views import View, MethodView
# 斜杠形式，不同url
app = Flask(__name__)

class UserView(MethodView):
    def get(self, project_id=None):
        if project_id is None:
            return f'get all projects'
        return f'get {project_id}'

    def post(self):
        return f'post'

    def put(self, project_id):
        return f'put {project_id}'

    def delete(self, project_id):
        return f'delete {project_id}'

# 此种形式(参数通过url地址传入)，注意get请求路由分为有参数和无参数的，所以路由要分开注册
f = UserView.as_view('user')
app.add_url_rule('/projects/<project_id>/', strict_slashes=False, view_func=f, methods=['GET', 'POST', 'PUT', 'DELETE'])

# strict_slashes=False  对于post、delete、put请求的url结尾无论是否有/， 都可以正常访问。
# 默认的get请求，strict_slashes值不对get请求产生影响。路由配置时结尾有/，请求url有咩有/都可以访问。路由配置结尾没有/，请求url就不能加/，否则无法访问呢。

app.add_url_rule('/projects/', view_func=f, defaults = {'project_id':None},methods=['GET' ])

app.run(debug=True)