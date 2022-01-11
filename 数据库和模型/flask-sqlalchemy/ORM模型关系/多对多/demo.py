from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 设置数据库连接地址
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost:3306/test1"
# 是否追踪数据库修改  很消耗性能, 不建议使用
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# 设置在控制台显示底层执行的SQL语句
app.config["SQLALCHEMY_ECHO"] = False

# 创建数据库连接
db = SQLAlchemy(app)

xuanke = db.Table('xuanke', db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                            db.Column('subject_id', db.Integer, db.ForeignKey('subject.id')))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    # subjects = db.relationship('Subject', backref='users', lazy='dynamic', secondary=xuanke)
    # subjects = db.relationship('Subject', secondary=xuanke, bakcref=db.backref('users'), lazy='dynamic')
    # user = User.query.get(1)
    # user.subjects lazy：select >> 直接获得最终结果，[Subject(), Subject()]
    # user.subjects lazy：dynamic >> 得到一个query对象，需要进行后续操作才能获取到最终结果。user.subjects.filter().all() >> [Subject(), Subject()]

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    users = db.relationship('User', backref='subjects', lazy='dynamic', secondary=xuanke)

@app.route('/insert')
def insert():
    db.drop_all()
    db.create_all()
    user1 = User(name='buyu')
    user2 = User(name='muzi')
    user3 = User(name='sun')

    subject1 = Subject(name='自动化')
    subject2 = Subject(name='侧开')
    subject3 = Subject(name='全程')

    user1.subjects.append(subject2)
    user2.subjects.append(subject2)
    user1.subjects.append(subject3)

    db.session.add_all([user1, user2, user3, subject3, subject2, subject1])
    db.session.commit()

    return 'insert successful'

@app.route('/select')
def select():
    # user = User.query.get(1)
    # s = user.subjects.all()[1]
    # print(s)
    # return 'select success'
    subject = Subject.query.get(1)
    s = subject.users
    print(s)
    return 'select success'

if __name__ == '__main__':

    app.run(debug=True)