from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/test1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# 一
class Project(db.Model):
    __tablename__ = 'project'  # 指定表名， 如果不指定表名则默认将类名【User】小写之后为表名
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    # modules和数据库中的表没有关系，不会在表中创建字段modules
    # db.relationship建立一个映射关系（声明本模型Project和哪个数据库模型建立映射关系）
    modules = db.relationship('Module', backref='project_module')  # modules，一对多调用时的查询对象

    # 当查询项目得到一个project。然后调用project.modules就会返回该项目下的module对象列表

# 多
class Module(db.Model):
    __tablename__ = 'mode'
    id = db.Column(db.Integer, primary_key=True)  # 数据类型及列属性直接从db导入
    name = db.Column(db.String(80))
    project_id = db.Column(db.Integer, db.ForeignKey(
        'project.id'))  # 定义一个外键，db.ForeignKey参数为另一个表中的字段。project为表名，不是模型类名。id为另一张表某个字段名

    # 当查询得到一个module的时候，想要获取module对应的项目信息直接module.project_module。即反向引用。


@app.route('/insert_project')
def insert_project():
    project1 = Project(name='HESS')
    project2 = Project(name='HXNP')
    db.session.add_all([project1, project2])
    db.session.commit()
    return 'insert_project successful'


@app.route('/insert_mode')
def insert_mode():
    mode1 = Module(name='ota', project_id=2)
    mode2 = Module(name='ctrller-manager', project_id=2)
    db.session.add_all([mode1, mode2])
    db.session.commit()
    return 'insert_mode successful'


@app.route('/select1')  # 多对一进行查询
def mode_select_project1():
    mode = Module.query.filter_by(name='ota').first()  # 先获取mode对象，
    print(mode.project_module)  # 想要获取module对应的项目信息直接module.project_module
    print(mode.project_module.name)  # 获取mode对应项目的项目名称
    return 'select successful'


@app.route('/select2')  # 一对多进行查询
def mode_select_project2():
    project = Project.query.filter_by(name='HXNP').first()  # 先获取project对象
    print(project.modules)  # 想要获取project对应的接口module信息直接project.modules，返回相关的对象列表
    print(project.modules[1].name)  # 获取项目对应接口的名字
    return 'select successful'


if __name__ == '__main__':
    app.run(debug=True)
