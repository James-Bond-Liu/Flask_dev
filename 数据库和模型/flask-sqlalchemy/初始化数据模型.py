from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/test1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# migrate = Migrate(app, db)


class User(db.Model):  # 创建一个表模型，数据模型继承的类时db.Model
    __tablename__='liufei'  # 指定表名，若没有指定，则以模型类名User的小写user为表名
    id = db.Column(db.Integer, primary_key=True)  # 数据类型及列属性直接从db导入
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)


def create_all():
    return db.create_all()  # 调用此方法初始化模型，将表创建到数据库中

create_all()
