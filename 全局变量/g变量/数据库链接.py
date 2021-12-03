import pymysql
from flask import Flask, g, request, abort

app = Flask(__name__)


def connect_to_database():
    conn = pymysql.connect(host='localhost', user='root', password='', db='hess', charset='utf8mb4')
    return conn.cursor()


@app.before_request
def get_db():
    if 'db' not in g:
        g.db = connect_to_database()  # 将函数connect_to_database返回的游标存储到全局变量g中


@app.teardown_request
def teardown_db(exception):
    db = g.pop('db', None)  # 先将g变量中的db游标删除，如果g中没有db则给变量赋一个默认值None，并返回给变量db。此处是为了删除g变量中的游标
    if db is not None:  # 当db不为空时，关闭游标链接。此处是为了将游标关闭。
        db.close()


@app.route('/register', methods=['GET', 'POST'])
def register():
    g.db.execute('SELECT * FROM user_info;')
    a = g.db.fetchall()
    print(a)
