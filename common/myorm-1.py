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

class User:
    table_name='user'

    #构造方法，
    def __init__(self,**kwargs):
        for k,v in kwargs.items():
            self.__setattr__(k,v)
        print(self.__dict__)

    #def select(self):
        # sql='select * from %s'%self.table_name
        # result=Mysql().querry(sql)
        # return result
    def select(self,**where):
        sql='select * from %s'%self.table_name
        if where is not None:
            sql+=" where "
            for k,v in where.items():
                sql+="%s='%s' and "%(k,v)
            sql+='1=1'
        print(sql)
        result = Mysql().querry(sql)
        return result

    #新增
    def insert(self):
        #insert into table(col1,col2,col3) value(v1,v2,v3)
        keys=[]
        values=[]
        for k,v in self.__dict__.items():
            keys.append(k)
            values.append(v)
        print(keys)
        print(values)
        print(",".join(keys))
        sql="insert into %s(%s) values('%s')"%(self.table_name,','.join(keys),"','".join(values))
        print(sql)
        result=Mysql().execute(sql)
        print(result)
if __name__ == '__main__':
    # db=Mysql()
    # result=db.querry('select * from user')
    # print(result)

    user=User(username='hym',password='123456',nickname='傻大个儿',role='manager',credit='3')
    # result=user.insert()
    # print(result)
    user.insert()
