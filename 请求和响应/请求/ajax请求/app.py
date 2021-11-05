from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        print(request.json)
        print(request.form)
        print(request.content_type)
        print(request.user_agent)
        print(request.environ)
        print(request.values)
        return '成功'

# 如果是Ajax请求，前端的请求头里会默认添加X-Requested-With: XMLHttpRequest

if __name__ == '__main__':
    app.run(debug=True)