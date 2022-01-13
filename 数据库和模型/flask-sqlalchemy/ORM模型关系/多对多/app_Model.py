from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost:3306/test"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = False
db = SQLAlchemy(app)

# 创建关系表  多对多关系必须创建单独的表来记录关联数据
class Xuanke(db.Model):
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), primary_key=True)
    score = db.Column(db.Integer)

# 学生表  多  一个学生可以选多门课, 一门课也可以被多个学生选
class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    subjects = db.relationship("Xuanke", backref='students')

# 课程表   多
class Subject(db.Model):
    __tablename__ = "subject"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    students = db.relationship("Xuanke", backref='subjects')

@app.route('/')
def index():
    db.drop_all()  # 删除 所有继承自db.Model的表
    db.create_all()  # 创建 所有的继承自db.Model的表

    stu1 = Student(name="panda")
    stu2 = Student(name="tiger")
    cur1 = Subject(name="python")
    cur2 = Subject(name="c")
    cur3 = Subject(name="java")

    # 关联数据
    stu1.subjects.append(cur1)
    stu1.subjects.append(cur2)
    stu2.subjects.append(cur2)
    stu2.subjects.append(cur3)

    # 添加到数据库
    db.session.add_all([stu1, stu2])
    db.session.commit()

    print(stu1.courses)
    print(cur2.students)
    return 'index'

@app.route('/select')
def select():
    student = Student.query.filter_by(name='panda').first()
    print(student.courses)

    print(student.courses.filter(Subject.name=='python').all())
    return 'select successful'

if __name__ == '__main__':

    app.run(debug=True)