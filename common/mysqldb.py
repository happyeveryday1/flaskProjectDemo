import pymysql
#1、连接到MySQL数据库
from pymysql.cursors import DictCursor

conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='861128',charset='utf8',database='woniunote',autocommit='True')
print(conn.get_server_info())
#2、执行sql语句
#2.1、实例化一个游标对象
#cursor=conn.cursor()

#2.2、定义sql语句
sql='select * from user;'
#2.3、通过游标执行
#cursor.execute(sql)
#result=cursor.fetchall()
#2.4、处理执行结果
#一般情况不建议使用下标获取数据，建议使用key==>列名，value==>单元格的值
#print(result[0][1])

sql2="update user set username='jjt@456.com' where userid=1"
cursor=conn.cursor(DictCursor)
cursor.execute(sql2)
#提交修改  update\insert\delete
#conn.commit()
#result=cursor.fetchall()
#print(result[0]['username'])
#3、关闭数据库连接
cursor.close()
conn.close()