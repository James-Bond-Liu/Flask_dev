from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////test.db'
app.config['SQLALCHEMKY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# 创建数据模型
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 数据类型及列属性直接从db导入
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

def create_all():
    return db.create_all()

@app.route('/')
def index():
    return 'hello'

if __name__ == '__main__':
    app.run(debug=True)