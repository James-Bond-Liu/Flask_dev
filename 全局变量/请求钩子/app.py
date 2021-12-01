from flask import Flask, abort, request

app = Flask(__name__)

@app.before_request
def get_user():
    user = request.args.get('user')

    if user != 'liufei':
        abort(401)

@app.route('/', methods=['GET', 'POST'])
def index():
    return 'hello'


if __name__ == '__main__':
    app.run(debug=True)