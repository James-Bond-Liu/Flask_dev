from flask import Flask, g
import sqlite3

app = Flask(__name__)


@app.before_request
def db():
    c = sqlite3.connect(r'd:\test.db')
    g.db = c
    g.c = c.cursor()


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


# 初始化
@app.route('/', methods=['GET', 'POST'])
def index():
    q = """CREAT TABLE project (ID INT PRIMARY   NOT NULL
                                NAME    CHAR(50)    NOT NULL
                                DESC    CHAR(500);"""
    g.c.execute(q)
    g.db.commit()
    q = f'insert into project (ID,NAME) values (123, "yu");'
    g.c.execute(q)
    g.db.commit()
    return 'hello'


# 查询
@app.route('/s', methods=['GET', 'POST'])
def s():
    g.c.execute('select * from project;')
    print(g.c.fetchall())
    return 's'
