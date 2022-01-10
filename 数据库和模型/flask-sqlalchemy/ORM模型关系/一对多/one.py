from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 用户表  一个用户有多个地址  一
class User(db.Model):
    __tablename__ = "users"  # 设置表名 表名默认为类名的小写
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # 创建关系属性  relationship("关联的类名", backref="对方表查询关联数据时的属性名")
    addresses = db.relationship("Address", backref="user")


# 地址表   多
class Address(db.Model):
    __tablename__ = "addresses"  # 设置表名 表名默认为类名的小写
    id = db.Column(db.Integer, primary_key=True)
    detail = db.Column(db.String(64), unique=True)
    # 设置外键(一般记录的是另一张表的主键)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))


@app.route('/')
def index():
    # 删除 所有继承自db.Model的表
    db.drop_all()
    # 创建 所有的继承自db.Model的表

    db.create_all()
  
    # # 添加用户
    # user = User(name="zs")
    # db.session.add(user)
    # db.session.commit()  # 必须先提交, 否则没有生成主键, 设置外键无效
    #
    # # 添加地址
    # adr1 = Address(detail="中关村1号", user_id=user.id)
    # adr2 = Address(detail="陆家嘴1号", user_id=user.id)
    # db.session.add_all([adr1, adr2])
    # db.session.commit()
    #
    # # 查询数据  根据用户查询地址
    # adrs = Address.query.filter_by(user_id=user.id).all()
    # for adr in adrs:
    #     print(adr.detail)

    
    user = User(name="zs")
    adr1 = Address(detail="中关村1号", user_id=user.id)
    adr2 = Address(detail="陆家嘴1号", user_id=user.id)
    # 关联数据
    # user.addresses = [adr1, adr2]
    user.addresses.append(adr1)
    user.addresses.append(adr2)
    # 添加到数据库中
    db.session.add_all([user])
    # db.session.add_all([user, adr1, adr2])
    db.session.commit()
    # 使用关系属性来查询数据
    print(user.addresses)
    print(adr1.user)

    return 'index'

if __name__ == '__main__':
    app.run(debug=True)

"""
>>>p1=Parent('p1')

>>>c1=Child('c1')

>>>c2=Child('c2')

>>>p1.children=[c1,c2]

>>>db.session.add(p1)

>>>db.session.commit()

此时，表parent和表child中都插入了数据。"""