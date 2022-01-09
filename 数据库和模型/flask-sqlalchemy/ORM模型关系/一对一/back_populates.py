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
    modules = db.relationship('Module', back_populates='project_module', uselist=False)

# 多
class Module(db.Model):
    __tablename__ = 'mode'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    project_module = db.relationship('Project', back_populates='modules', uselist=False)  # 用back_populates来设置映射关系时，一方、多方都需要设置relationship映射

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

@app.route('/select1')
def mode_select_project1():
    mode = Module.query.filter_by(name='ota').first()
    print(mode.project_module)
    print(mode.project_module.name)
    return 'select successful'


@app.route('/select2')
def mode_select_project2():
    project = Project.query.filter_by(name='HXNP').first()  # 先获取project对象
    print(project.modules)  # 由于在定义模型关系时uselist=False，所以此处返回的module对象只有一个，为第一个
    print(project.modules.name)  # 获取项目对应接口的名字
    return 'select successful'


if __name__ == '__main__':
    app.run(debug=True)

