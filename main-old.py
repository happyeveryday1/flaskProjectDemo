from flask import Flask, render_template, session, make_response, request
import os


import urllib.request
app = Flask(__name__,static_url_path='/',static_folder='resource',template_folder='template')
app.config['SECRET_KEY']=os.urandom(24)  #生成随机数种子，用于生成sessionID
#定义文章首页
@app.route('/')
def index():
    #return render_template('article-1.html')
    return render_template("index-list.html")
    #return render_template("boot3.html")
    #return render_template("post-3.html")
#定义文章列表页
@app.route('/article')
def article():
    return render_template("article-user.html")

#定义用户注册
@app.route("/user/reg",methods=['POST',])
def register():
    return "good"

@app.route("/sess")
def sess():
    session['username']='woniu'
    session['nickname']="mm",
    session['role']='管理员',
    session['logina']='true',
    return session.get('username')

@app.route('/sc/read')
def scread():
    return "你当前的昵称为%s"%session.get('username')
    session.clear

#利用自定义响应的方式来往浏览器设置cookie
@app.route('/cookie')
def cookie():
    #无法在同一个接口中既设置cookie又获取cookie
    response=make_response()
    response.set_cookie('username','xiaohong',max_age=30)
    response.set_cookie('password', '123456', max_age=30)
    return response
@app.route('/co/read')
def coread():
    return "你当前的昵称为%s"%request.cookies.get('username')
    session.clear

#定义全局拦截器
#@app.before_request
def before():
    url=request.path  #读取到当前接口的地址

    if url=='/sess':
        pass
    elif session.get('username') != 'woniu':
        return "您还未登录"
    else:
        return "jjjj"

from controller.demo import *
app.register_blueprint(demo)  #使用blueprint时，必须将其注册到app中
if __name__ == '__main__':
    app.run(debug=True)