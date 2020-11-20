from flask import Blueprint
myhtml=Blueprint('myhtml',__name__)
@myhtml.route('/template01/')
def template01():
    username="蜗牛学院"
    resp="""
        <div>
            <ul>
                <li>这是一</li>
                <li>这是二</li>
                <li>这是三</li>
            </ul>
            <p>欢迎%s登录</p>
        </div>
    """%username
    return resp

@myhtml.route('/template02/<username>')
def template02(username):
    resp="""
        <div>
            <ul>
                <li>这是一</li>
                <li>这是二</li>
                <li>这是三</li>
            </ul>
            <p>欢迎%s登录</p>
        </div>
    """%username
    return resp

@myhtml.route('/template03')
def template03():
    with open('template/myhtml.html',encoding='utf-8') as file:
        html=file.read()

    return html
