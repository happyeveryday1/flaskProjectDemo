from flask import Blueprint, render_template, session

jinja2=Blueprint('jinja2',__name__)

#自定义一个函数,供jinja2调用
#第一种方案，使用上下文处理器来注册自定义函数到jinja2模板引擎中，并且返回一个字典类型的数据
#第二种方案件main.py
@jinja2.context_processor
def gettype01():
    type={'1':'PHP开发','2':'java开发'}
    return dict(gettype=type)



@jinja2.route('/jinja2')
def jinja2_demo():
    session['username']='蜗牛笔记',
    article={'title':'flask实战教程','count':101}
    color="<font color='red'>这是一段红色文字</font>"

    return render_template('jinja2-demo.html',article=article,count=100,color=color)