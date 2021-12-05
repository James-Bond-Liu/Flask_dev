from flask import Flask
import pymysql

app = Flask(__name__)


def connect_to_database():
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='123456',
                           db='lemon_tester',
                           charset='utf8mb4')
    return conn.cursor()

@app.route('/')
def index():
    db = connect_to_database()
    db.execute('SELECT * FROM project_info;')
    res = db.fetchall()
    print(res)
    return 'hello'
