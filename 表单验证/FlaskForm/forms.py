from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Regexp, Length, EqualTo


class ReqisterForm(FlaskForm):
	# 字段名最好和表单name属性一致，最好和数据库里面的字段名一致
	phone = StringField(validators=[Regexp(r'1[3,5,8]\d{9}$'), DataRequired()])  # DataReauired()表明此字段必须存在，不能为空
	pwd = PasswordField(validators=[Length(6,32), DataRequired()])
	confirm_pwd = PasswordField(EqualTo('pwd'))