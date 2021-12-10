#!/usr/bin/env python
#-*- coding: utf-8 -*-


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 配置多个数据库连接
SQLALCHEMY_BINDS = {
    'users': 'sqlite:///users.db',
    'appmeta': 'sqlite:///appmeta.db'
}

app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///test.db' # 默认数据库引擎
app.config['SQLALCHEMY_BINDS'] = SQLALCHEMY_BINDS
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class News(db.Model):
    __tablename__ = 'news' # 未设置__bind_key__,则采用默认的数据库引擎

    id = db.Column(db.Integer, primary_key=True)
    news_title = db.Column(db.String(80), unique=True)
    news_content = db.Column(db.String(120), unique=True)

    def __init__(self, news_title, news_content):
        self.news_title = news_title
        self.news_content = news_content

    def __repr__(self):
        return '<news_title %r>' % self.news_title

class User(db.Model):
    __bind_key__ = 'users' # 已设置__bind_key__,则采用设置的数据库引擎
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

class Article(db.Model):
    __bind_key__ = 'appmeta'
    __tablename__ = 'article'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    content = db.Column(db.String(120), unique=True)

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return '<Title %r>' % self.title


# db.create_all() # 未指定bind,则使用默认的数据库引擎
# db.create_all(bind='users') # 指定bind,则使用指定的数据库引擎
# db.create_all(bind='appmeta')
#
# news = News('ha','hahahhahaha') # 自动关联到相对应的ORM模型,进而使用相关联的数据库引擎
# db.session.add(news) # 插入一条数据
# db.session.commit()
#
# admin = User('admin', 'admin@example.com')
# guest = User('guest', 'guest@example.com')
# db.session.add_all([admin,guest]) # 插入多条数据
# db.session.commit()
#
# title = Article('title1', 'content1')
# db.session.add(title)
# db.session.commit()

"""
执行该文件,会自动生成三个数据库文件:appmeta.db,users.db,test.db
每个数据库中插叙的有相对应的数据
"""
if __name__ == '__main__':
    app.run(debug=True)