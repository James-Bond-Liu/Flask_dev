from flask import Flask,request
from flask.views import View, MethodView

# methodView也是类视图的一种
app = Flask(__name__)

class UserView(MethodView):
    # methods = request.method  不需要像可插拔视图中再去调用前端的请求方法来分配不同的请求了。使用method_view后，会自动获取请求方法，然后进行分发请求。
    # methodView也不需要重写dispatch_request方法。父类MethodView中已经封装重写了。

    def get(self):
        return 'get'
    def post(self):
        return 'post'
    def put(self):
        return 'put'

app.add_url_rule('/', view_func=UserView.as_view('userview'))  # 使用method_view视图时,路由默认支持所有的常见请求方式。当然也可以特殊指定某种请求方式。


if __name__ == '__main__':
    app.run(debug=True)