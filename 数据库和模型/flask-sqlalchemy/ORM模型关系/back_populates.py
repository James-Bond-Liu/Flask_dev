from operator import and_

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/test1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 一
class Project(db.Model):  # 创建一个表模型，数据模型继承的类时db.Model
    __tablename__ = 'project'  # 指定表名， 如果不指定表名则默认将类名【User】小写之后为表名
    id = db.Column(db.Integer, primary_key=True)  # 数据类型及列属性直接从db导入
    name = db.Column(db.String(80))

    # modules和数据库中的表没有关系，不会在表中存在字段modules
    # db.relationship建立一个映射关系（声明本模型Project和哪个数据库模型建立映射关系，多对一调用时的查询对象）
    modules = db.relationship('Module', back_populates='project_module')  # modules，一对多调用时的查询对象

    # 当查询项目得到一个project。然后调用project.modules就会返回该项目下的module列表




# 多
class Module(db.Model):
    __tablename__ = 'mode'
    id = db.Column(db.Integer, primary_key=True)  # 数据类型及列属性直接从db导入
    name = db.Column(db.String(80))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))  # 定义一个外键，db.ForeignKey参数为另一个表中的字段。project为表名，不是模型类名。id为另一张表某个字段名
    project_module = db.relationship('Project', back_populates='modules ')

    # 当查询得到一个module的时候，想要获取module对应的项目信息直接module.project_module。这样就不用写多表关联查询语句了。即反向引用。



if __name__ == '__main__':
    app.run(debug=True)
