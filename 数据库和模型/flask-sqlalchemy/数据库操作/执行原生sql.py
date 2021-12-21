from operator import and_

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



"""
查询数据
"""
@app.route('/select_sql')
def select():
    sql = 'select * from user;'
    res = db.session.execute(sql)
    user = res.fetchone()
    return f'hello, select结果为{user}'





if __name__ == '__main__':
    app.run(debug=True)
