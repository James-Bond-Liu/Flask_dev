import os
from flask import Flask, request, render_template, abort, Response
from forms import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(10)  # 利用urandom方法生成10位的随机字符，用来充当密钥

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(formdata=request.form,
        data=None)
    """
    RegisterForm类继承FlaskForm类，初始化参数formdata,obj,data
    当前端通过form表单提交数据时，服务端通过formdata参数来接收数据。
    当前端发送Ajax请求或者以json格式发送数据时，服务端通过data参数来接收数据。
    formdata用来接收前端以form表单提交至后台的数据，优先级最高
    data：用来接收前端以json格式将数据提交至后台的数据，当formdata、obj为空时，使用
    """

    if request.method == 'GET':
        return render_template('register2.html', form = form)
    else:
        phone = request.form.get('phone')
        pwd = request.form.get('pwd')
        confirm_pwd = request.form.get('confirm_pwd')
        # 校验
        # form = RegisterForm(request.form)  # RegisterForm根本上继承自Form类，在初始化参数formdata

        # if form.validate() and form.validate_phone():  调用自定义的validate函数进行表单验证
        if form.validate():  # 对表单中的数据按照RegisterForm中定义的规则进行验证
            print(form.data)
            return 'successful'
        else:
            return f'ERROR:{form.errors}'  # form.errors为RegisterForm中validators中定义的message错误提示
            # ERROR:{'phone': ['This field is required.'], 'pwd': ['This field is required.'], 'confirm_pwd': ['This field is required.'], 'csrf_token': ['The CSRF token is missing.']}

if __name__ == '__main__':
    app.run(debug=True)