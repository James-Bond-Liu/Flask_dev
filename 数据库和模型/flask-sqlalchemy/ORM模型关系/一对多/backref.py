from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# 一，项目
class Project(db.Model):
    __tablename__ = 'project'  # 指定表名， 如果不指定表名则默认将类名【User】小写之后为表名
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    # modules和数据库中的表没有关系，不会在表中创建字段modules
    # db.relationship建立一个映射关系（声明本模型Project和哪个数据库模型建立映射关系）
    # modules = db.relationship('Module', backref='project_module')  # modules，一对多调用时的查询对象
    modules = db.relationship('Module', backref = 'project_module', lazy='select')


    # 当查询项目得到一个project。然后调用project.modules就会返回该项目下的module对象列表


# 多，接口
class Module(db.Model):
    __tablename__ = 'mode'
    id = db.Column(db.Integer, primary_key=True)  # 数据类型及列属性直接从db导入
    name = db.Column(db.String(80))
    project_id = db.Column(db.Integer, db.ForeignKey(
        'project.id'))  # 定义一个外键，db.ForeignKey参数为另一个表中的字段。project为表名，不是模型类名。id为另一张表某个字段名

    # 当查询得到一个module的时候，想要获取module对应的项目信息直接module.project_module。即反向引用。



# 插入数据方式一
"""
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

"""

# 插入数据方式二
@app.route('/insert')
def insert():
    # 删除 所有继承自db.Model的表
    db.drop_all()

    # 创建 所有的继承自db.Model的表
    db.create_all()

    project1 = Project(name='HESS')
    project2 = Project(name='HXNP')
    mode1 = Module(name='ota')
    mode2 = Module(name='ctrller-manager')

    # 使用关系属性关联数据
    project2.modules.append(mode1)  # mode表中mode1数据行project_id直接等于project2的id不用手动填写。
    project2.modules.append(mode2)

    # 添加到数据库中
    db.session.add_all([project1,
                       project2])  # 可以直接将project1,project2,mode1,mode2四个数据添加到数据库中，替代了db.session.add_all(project1, project2, mode1, mode2)

    db.session.commit()
    return 'insert successful'


@app.route('/select1')  # 多对一进行查询
def mode_select_project1():
    mode = Module.query.filter_by(name='ota').first()  # 先获取mode对象
    print(mode.project_module)  # 想要获取module对应的项目信息直接module.project_module
    print(mode.project_module.name)  # 获取mode对应项目的项目名称
    mode.project_module.name = 'liufei'  # 更改表中某个字段
    db.session.commit()
    return 'select successful'


@app.route('/select2')  # 一对多进行查询
def mode_select_project2():
    project = Project.query.filter_by(name='liufei').first()  # 先获取project对象
    # print(project.name, project.id)
    print(project.modules)  # 想要获取project对应的接口module信息直接project.modules，返回相关的对象列表
    # print(project.modules[1].name)  # 获取项目对应接口的名字
    return 'select successful'


if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True)
