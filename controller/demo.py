from flask import Blueprint, request

demo=Blueprint('demo',__name__)
@demo.route('/demo1')
def mydemo1():#函数名称不能与全局变量名称一样
    return "hhh"

@demo.route('/demo2')
def mydemo2():#函数名称不能与全局变量名称一样
    return "jjj"
#定义模块拦截器
@demo.before_request
def bero():
    url=request.path
    if url=='/demo1':
        return "禁止访问"
    else:
        pass

