from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Regexp, Length, EqualTo

"""
专门用于处理前端的表单传至后台后进行数据验证
"""

class RegisterForm(FlaskForm):
	# 字段名最好和表单name属性一致，最好和数据库里面的字段名一致
	# message字段用来编写，当前端返回至后端的表单数据验证失败时，抛出的异常
	phone = StringField(label='手机号码',
						validators=[Regexp(r'1[3,5,8]\d{9}$', message='手机号码格式错误'), DataRequired(message='手机号码不能为空')])  # DataReauired()表明此字段必须存在，不能为空

	pwd = PasswordField(label='密码',
						validators=[Length(5,32, message='密码长度不符合要求'), DataRequired(message='密码不能为空')],
						filters=[lambda x:str(x)+'l'])  # filters对前端输入的数据按照一定的规则进行过滤，此处，比如前端输入的数据为123456，通过filters后便成为"123456l"，然后拿123456l进行规则的验证

	confirm_pwd = PasswordField(label='确认密码',
								validators=[EqualTo('pwd', message='两次密码不相同'),DataRequired(message='确认密码不能为空')],
								render_kw={"class":"form-control"},# render_kw用来给某个标签增加属性{属性名：属性值}
								filters=[lambda x: str(x) + 'l'],
								default=0)  # 此标签不输入数据时，默认为0