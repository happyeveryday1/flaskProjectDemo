import pymysql
from pymysql.cursors import DictCursor

class Mysql:
    # 实例化即创建与数据库的连接
    def __init__(self):
        conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='861128',charset='utf8',database='woniunote',autocommit='True')
        self.cursor=conn.cursor(DictCursor)

    #封装基础查询语句
    def querry(self,sql):
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        return result

    #执行修改操作
    def execute(self,sql):
        try:
            self.cursor.execute(sql)
            return 'ok'
        except:
            return 'fail'


#封装成标准的模型类，供子类继承
#增加field（）方法来指定查询哪些列，*代表所有列
class Model:
    def __init__(self,**kwargs):
        for k,v in kwargs.items():
            self.__setattr__(k,v)
        print(self.__dict__)

    #通过链式操作指定查询哪些列
    def filed(self,columns):
        self.columns=columns  #动态增加类实例属性
        return self

    #带列名的查询条件
    def select(self,**where):
        table=self.__class__.__getattribute__(self,'table_name')
        sql='select * from %s'%table
        if where is not None:
            sql+=" where "
            for k,v in where.items():
                sql+="%s='%s' and "%(k,v)
            sql+='1=1'
        print(sql)
        result = Mysql().querry(sql)
        return result

