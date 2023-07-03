"""Python的mysql"""

from pymysql import Connect #导入包

conn = Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='password',
    autocommit=True,
)#创建sql连接 autocommit:自动提交，不用调用commit方法手动提交了
print(conn.get_server_info())#返回数据库版本
cursor = conn.cursor()#创建操作数据库的游标对象
conn.select_db("py_project_test01")#选择数据库

# cursor.execute("create table test_pymysql(id int, name varchar(255));") #查询语句
cursor.execute("select * from test_pymysql;")
select = cursor.fetchall()
sql_data = { i+1:select[i] for i in range(len(select))}
print(sql_data) #{1: (1, '小明'), 2: (2, '小刚'), 3: (3, '小李')}

"""更改数据库：插入，删除需要确认"""
cursor.execute("insert into test_pymysql(id,name) values (4,'小光');")



conn.close()#关闭sql









