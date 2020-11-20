from flask import Flask
import os


import urllib.request
app = Flask(__name__,static_url_path='/',static_folder='resource',template_folder='template')
app.config['SECRET_KEY']=os.urandom(24)  #生成随机数种子，用于生成sessionID

#第二种方案，按照标准的函数调用的方式进行
def gettype02():
    type={'1':'PHP开发','2':'java开发'}
    return type
app.jinja_env.globals.update(mytype=gettype02)

#定义404错误页面
@app.errorhandler(404)
def errer(e):
    return "你的页面不存在"

if __name__ == '__main__':
    from controller.myhtml import myhtml
    app.register_blueprint(myhtml)

    from controller.jinja2 import *
    app.register_blueprint(jinja2)
    app.run(debug=True)

