from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 设置数据库连接地址
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost:3306/test"
# 是否追踪数据库修改  很消耗性能, 不建议使用
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# 设置在控制台显示底层执行的SQL语句
app.config["SQLALCHEMY_ECHO"] = False

# 创建数据库连接
db = SQLAlchemy(app)

"""多对多 通过关系属性来关连/查询数据 操作简单  1> 定义关系表来设置外键 2> 定义关系属性 3> 使用关系属性来关联数据"""

# 创建关系表  多对多关系必须创建单独的表来记录关联数据。
# 注意此表不是ORM模型，不能进行相关的ORM操作
t_stu_cur = db.Table("table_stu_cur",
         db.Column("stu_id", db.Integer, db.ForeignKey("students.id"), primary_key=True),
         db.Column("cur_id", db.Integer, db.ForeignKey("courses.id"), primary_key=True)
         )


# 学生表  多  一个学生可以选多门课, 一门课也可以被多个学生选
class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # 多对多关系属性, 还需要设置参数secondary="关系表名"
    # courses = db.relationship("Course", backref="students", secondary="table_stu_cur")  # lazy参数默认为select
    courses = db.relationship("Course", backref='students', lazy='dynamic', secondary='table_stu_cur')

    # student = Student.query.get(1)
    # student.courses  lazy：select >> 直接获得最终结果，[<Course 1>, <Course 2>]
    # student.courses  lazy：dynamic >> 得到一个query对象，需要进行后续操作才能获取到最终结果。student.courses.filter().all() >> [<Course 1>, <Course 2>]

    # 只有正向映射引用时(student.courses)才会返回一个query对象，反向映射引用（course.students）直接返回最终结果

# 课程表   多
class Course(db.Model):
    __tablename__ = "courses"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)



@app.route('/')
def index():

    # 删除 所有继承自db.Model的表
    # db.drop_all()
    # 创建 所有的继承自db.Model的表
    db.create_all()

    stu1 = Student(name="panda")
    stu2 = Student(name="tiger")
    cur1 = Course(name="python")
    cur2 = Course(name="c")
    cur3 = Course(name="java")

    # 关联数据
    stu1.courses.append(cur1)
    stu1.courses.append(cur2)
    stu2.courses.append(cur2)
    stu2.courses.append(cur3)

    # 添加到数据库
    # db.session.add_all([stu1, stu2, cur1, cur2, cur3])
    db.session.add_all([stu1, stu2])
    db.session.commit()

    print(stu1.courses)  # 正向映射，SELECT courses.id AS courses_id, courses.name AS courses_name FROM courses, table_stu_cur WHERE %(param_1)s = table_stu_cur.stu_id AND courses.id = table_stu_cur.cur_id
    print(cur2.students)  # 反向映射，[<Student 1>, <Student 2>]
    return 'index'
@app.route('/select')
def select():
    student = Student.query.filter_by(name='panda').first()
    print(student.courses)  # Student模型实例调用属性courses后返回一个query对象
    # print(student.courses[1].name)
    print(student.courses.filter(Course.name=='python').all())  # query对象经过后续操作才能返回最终结果
    return 'select successful'

if __name__ == '__main__':
    # db.drop_all()
    app.run(debug=True)