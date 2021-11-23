import re

from flask import Flask, request, render_template, abort, Response

app = Flask(__name__)

# 可以将视图函数中的验证提取出来，减少题图函数的代码，提高验证函数的代码复用性
# def test(form):
#     if not form.get('phone'):
#         # 提示手机号码不能为空
#         abort(412, description='phone is empty')
#     if not re.match(r'^1[0-9]{10}$', form.get('phone')):
#         # 提示手机号码不符合格式
#         abort(412, description='phone is error')
#     if not form.get('pwd'):
#         # 提示密码为空
#         abort(412, description='pwd is empty')
#     if form.get('pwd') != form.get('confirm_pwd'):
#         # 提示两次密码不相同
#         abort(412, description='pwd is not correct')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register1.html')
    else:
        # test(request.form)
        phone = request.form.get('phone')
        pwd = request.form.get('pwd')
        confirm_pwd = request.form.get('confirm_pwd')
        # 校验
        if not phone:
            # 提示手机号码不能为空。
            abort(412, description='phone is empty')  # 通过abort中的description参数直接返回给前端报错信息
        if not re.match(r'^1[0-9]{10}$', phone):
            # 提示手机号码不符合格式。
            """
            # abort(412, description='电话号码格式不正确')  # description以中文返回，会出现乱码
            解决方法一，直接return返回消息，同时content-type设置为'text/html;charset=utf-8'
            return '电话号码格式不正确', 412, {'content_type':'text/html;charset=utf-8'}
            
            解决方法二，利用abort抛出异常-Reponse()响应对象
            """
            # 可以通过abort直接返回Response()对象同时设置content-type为UTF-8
            resp = Response(response='电话号码格式不正确', status=412, content_type='text/html;charset=utf-8')
            abort(resp)

        if not pwd:
            # 提示密码为空，后端提供变量对前端进行渲染
            resp = Response(response=render_template('register1.html', msg='密码不能为空'), status=412, content_type='text/html;charset=utf-8')
            abort(resp)
        if pwd != confirm_pwd:
            # 提示两次密码不相同
            abort(412, description='pwd is not correct')
        return 'hello'

if __name__ == '__main__':
    app.run(debug=True)