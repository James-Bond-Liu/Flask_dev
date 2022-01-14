from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):  # 继承db的模型类
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(20), nullable=False)  # 是否可以不存在
    author = db.Column(db.String(20), default="吕星辰")  # 默认是··· ···
    phone = db.Column(db.String(20), nullable=False)

    """遍历获取到的数据，为数据库模型动态赋值"""
    def set_attr(self, get_data):
        if isinstance(get_data, dict):
            for item in get_data.items():  # item 最后遍历出来的是 ('key','value') ··· ···
                if hasattr(self, item[0]) and item[0] != 'id':  # id不被赋值，因为它是主键
                    setattr(self, item[0], item[1])
        else:
            raise Exception('{0} MUST BE DICT'.format(get_data))


db.drop_all()
db.create_all(app=app)
"""每次只能添加一行数据"""
data1 = {'title': '生死河', 'author': '吕小辰', 'phone': '13181706133'}
book = Book()
book.set_attr(data1)

db.session.add_all([book])
db.session.commit()

"""一次添加多行数据"""
data2 = [{'title': '背影', 'author': 'panda', 'phone': '123467484'}, {'title': '百年孤独', 'author': 'tiger', 'phone': '126574467484'}]
book = Book()
for i in data2:
    book = Book()
    book.set_attr(i)
    db.session.add(book)
    db.session.commit()