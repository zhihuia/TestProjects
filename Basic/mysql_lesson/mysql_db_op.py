mysql_host = "119.23.241.154"
mysql_port = 3306
mysql_db = "test"
mysql_user = "futurevistor"
mysql_passwd = "123456"


#引入相关的库
import pymysql.cursors

#连接操作--编码格式的指定，默认返回数据类型的指定（字典）
conn = pymysql.Connect(host=mysql_host, user=mysql_user,password=mysql_passwd,db=mysql_db,
                port=mysql_port,charset='utf8mb4',cursorclass  = pymysql.cursors.DictCursor)

#获取游标
cursor = conn.cursor()

#sql语句
sql_insert = 'insert into python6(name,sex) values ("xixi","女")'

#执行sql语句
# try:
#     cursor.execute(sql_insert)
#     conn.commit()
# except:
#     conn.rollback()

#查询
sql_select = "select * from python6"
#执行
cursor.execute(sql_select)
#获取查询结果 --只获取一条数据
data_a = cursor.fetchone()
print(data_a)

#获取查询结果 --获取所有条数据
data_all = cursor.fetchall()
print(data_all)

#关闭连接、关闭游标
cursor.close()
conn.close()