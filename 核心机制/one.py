from 核心机制.demo import app
from flask import current_app
from flask import g

ctx=app.app_context()
ctx.push()
print(app.name)
print(app.config.get('DEBUG'))
app.run()
