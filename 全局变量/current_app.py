from flask import Flask, current_app

app = Flask(__name__)

"""
g   session     reqeust     current_app 这四个为全局代理设置的

current_app，主要使用场景：在项目的其他文件中访问app程序的本身资源时，直接导入app实例对象容易出现循环导入的问题。
可在其他文件中直接通过Flask导入current_app，然后通过current_app直接访问app的属性
"""
