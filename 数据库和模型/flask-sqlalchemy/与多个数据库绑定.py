from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/test1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 配置多个数据库连接
SQLALCHEMY_BINDS = {
    'panda': 'mysql+pymysql://root:123456@localhost:3306/test2',
    'cat': 'mysql+pymysql://root:123456@localhost:3306/test3'
}
app.config['SQLALCHEMY_BINDS'] = SQLALCHEMY_BINDS

db = SQLAlchemy(app)


class User(db.Model):  # 创建一个表模型，数据模型继承的类db.Model
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)  # 数据类型及列属性直接从db导入
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)


class News(db.Model):
    __tablename__ = 'news'
    __bind_key__ = 'panda'

    id = db.Column(db.Integer, primary_key=True)
    news_title = db.Column(db.String(80), unique=True)
    news_content = db.Column(db.String(120), unique=True)


class Profile(db.Model):
    __tablename__ = 'profile'
    __bind_key__ = 'cat'

    id = db.Column(db.Integer, primary_key=True)
    news_title = db.Column(db.String(80), unique=True)
    news_content = db.Column(db.String(120), unique=True)


"""
上面是三个数据模型User,News,Profile
    User没有指定bind_key，默认制定了bind_key为URI的地址，则在创建表初始化数据库时使用默认的URI的数据库链接地址
    News在模型类中指定了bind_key为SQLALCHEMY_BINDS中配置的panda，所以在创建表时，只能用配置项中配置好的panda数据库地址
"""

db.create_all()  # 调用此方法初始化数据库，将数据模型类创建到数据库中
"""
db.creat_all()方法中没有传入参数bind，默认创建所有的数据库模型，模型创建到bind指定的相应的库中。

db.creat_all()方法中没有传入参数bind，则在创建数据库时默认使用URI中配置的数据库链接，而创建的数据模型表也只能是模型类中没有指定bind_key的模型
此app中调用此方法，只能创建user表，
profile和news表不能创建，因为这两个数据模型类中已经指定了其自身的数据库链接，而不能使用其他的数据库链接bind
"""
# db.create_all(bind='panda')
"""
指定bind=panda，在创建数据库表时只会去寻找和panda数据链接绑定的数据模型类然后创建到数据库中
"""
# db.create_all(bind=['panda', 'cat'])
"""
指定多个bind，初始化到数据库中
"""
