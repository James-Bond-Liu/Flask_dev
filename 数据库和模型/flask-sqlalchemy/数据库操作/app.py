from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/test1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):  # 创建一个表模型，数据模型继承的类时db.Model
    __tablename__ = 'user'  # 指定表名
    id = db.Column(db.Integer, primary_key=True)  # 数据类型及列属性直接从db导入
    username = db.Column(db.String(80), unique=False)
    email = db.Column(db.String(120), unique=True)

# db.create_all()
# 在视图函数访问并操作数据库表前，将其创建出来

"""
插入数据
"""
@app.route('/insert1')
def index1():
    new_user = User(username='liufei', email='779542742@qq.com')
    db.session.add(new_user)  # 添加一条数据
    db.session.commit()
    return 'hello, insert1'

@app.route('/insert2')
def index2():
    new_user1 = User(username='刘菲', email='779542742@qq.com')
    new_user2 = User(username='小姨')
    db.session.add_all([new_user1, new_user2])  # 添加多条数据
    db.session.commit()
    return 'hello, insert2'

"""
查询数据
"""
@app.route('/select')
def select():
    users = User.query.all()
    return f'hello, select结果为{users}'

if __name__ == '__main__':
    app.run(debug=True)
