from flask import Flask, redirect, request, url_for
from werkzeug.routing import Rule

app = Flask(__name__)

@app.route('/', methods=['GET', 'PSOT'])
def index():
    if request.args.get('username') is None:
        # redirect 中使用url_for(endpoint名, **values) 进行重定向，values参数是路由规则(Rule类from werkzeug.routing import Rule)中的参数
        # return redirect(url_for('hhh'))
        return redirect(url_for('hhh', username='panda', pwd='dog'))
        # url_for在重定向时可以添加关键字参数，添加的关键字参数是重定向至新URL的参数，和原路由没有关系。
        # 此重定向后，前端访问“127.0.0.1:5000/”，则会重定向至“http://127.0.0.1:5000/login?username=panda&pwd=dog”
    return 'hello'

@app.route('/login', methods = ['GET'], endpoint='hhh')
def login():
    return 'login'



if __name__ == '__main__':
    app.run(debug=True)
