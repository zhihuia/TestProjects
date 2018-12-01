import pymysql.cursors

class MySql_Operator:

    def __init__(self,host,db,user,passwd,port=3306):
        try:
            self.conn = pymysql.Connect(host=host, user=user,password=passwd,db=db,
                    port=port,charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
            self.cur = self.conn.cursor()
            self.connect_flag = 0
        except Exception as e:
            print(e)
            self.connect_flag = 1

    #查找
    def sleect_all_datas(self,select_sql):
        #查询数据-execute函数
        self.cur.execute(select_sql)
        data_all = self.cur.fetchall()
        return data_all

    #增加、修改、删除
    def updata_datas(self,updata_sql):
        try:
            self.cur.execute(updata_sql)
            self.conn.commit()
        except:
            self.conn.rollback()

    #关闭数据库连接
    def close_db(self):
        self.cursor.close()
        self.conn.close()

