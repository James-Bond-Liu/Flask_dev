import re

from flask import Flask, request, render_template, abort
app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        phone = request.form.get('phone')
        pwd = request.form.get('pwd')
        confirm_pwd = request.form.get('confirm_pwd')
        # 校验
        if not phone:
            # 提示手机号码不能为空
            abort(412, description='phone is empty')
        if not re.match(r'^1[0-9]{10}$', phone):
            # 提示手机号码不符合格式
            abort(412, description='phone is error')
        if not pwd:
            # 提示密码为空
            abort(412, description='pwd is empty')
        if pwd != confirm_pwd:
            # 提示两次密码不相同
            abort(412, description='pwd is not correct')
        return 'hello'

if __name__ == '__main__':
    app.run(debug=True)