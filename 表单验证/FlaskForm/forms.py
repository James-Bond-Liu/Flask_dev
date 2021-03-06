import re

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import DataRequired, Regexp, Length, EqualTo, ValidationError

"""
自定义validators验证器
"""


# 自定义的手机号码格式验证器（通过模仿其他validators来实现）
class Mobile():
    regex = re.compile(r'^1[3,5,7,8,9]\d{9}$')

    def __init__(self, message=None):
        if message is None:
            self.messsage = '不是手机号码'
        else:
            self.messsage = message

    def __call__(self, form, field):  # form、field 这两个参数是固定的
        match = self.regex.match(field.data)  # field.data是将表单中的数据提取出来，然后进行后续的处理
        if not match:
            message = self.messsage
            raise ValidationError(message)
        return match


"""
专门用于处理前端的表单传至后台后进行数据验证
"""


class RegisterForm(FlaskForm):
    # 字段名最好和表单name属性一致，最好和数据库里面的字段名一致
    # message字段用来编写，当前端返回至后端的表单数据验证失败时，抛出的异常
    phone = StringField(label='手机号码',
                        validators=[Mobile('手机号码格式不正确'),  # 调用自定义的Mobile验证器进行验证
                                    # Regexp(r'1[3,5,8]\d{9}$', message='手机号码格式错误')
                                    DataRequired(message='手机号码不能为空')])  # DataReauired()表明此字段必须存在，不能为空

    pwd = PasswordField(label='密码',
                        validators=[Length(5, 32, message='密码长度不符合要求'), DataRequired(message='密码不能为空')],
                        filters=[lambda x: str(
                            x) + 'l'])  # filters对前端输入的数据按照一定的规则进行过滤，此处，比如前端输入的数据为123456，通过filters后便成为"123456l"，然后拿123456l进行规则的验证

    confirm_pwd = PasswordField(label='确认密码',
                                validators=[EqualTo('pwd', message='两次密码不相同'), DataRequired(message='确认密码不能为空')],
                                render_kw={"class": "form-control"},  # render_kw用来给某个标签增加属性{属性名：属性值}
                                filters=[lambda x: str(x) + 'l'],
                                default=0)  # 此标签不输入数据时，默认为0

    job = SelectField('Job', choices=[
        ('teacher', 'Teacher'),
        ('doctor', 'Doctor'),
        ('engineer', 'Engineer'),
        ('lawyer', 'Lawyer')])

    """
    通过定义一个validate函数来进行验证
    """
    def validate_phone(self):
        # 如果某个数据符合规则，那么我就返回True；否则返回False
        if self.phone.data == 'admin':
            return True
        return False

