# coding = utf-8

import pymysql

users_db = pymysql.connect(host="localhost", user="root", password="bao929038", db="Wechat_Users")
# print (users_db)
cursor = users_db.cursor()
# create cursor

class Wechat_SQL(object):
    def __init__(self, db, cursor):
        self.cursor = cursor
        self.db = db

    def creat_table(self):
        creat_table = "CREATE TABLE IF NOT EXISTS Foxboro (ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT, " \
                      "SESAID CHAR(6) NOT NULL, PHONE VARCHAR(11) NOT NULL, NAME VARCHAR(20), WECHATID VARCHAR(100) NOT NULL);"
        result =  self.cursor.execute(creat_table)
        self.close()
        return result


    def checkuser(self, WECHATID):
        sql = "select * from Foxboro where WECHATID =%(WECHATID)s"
        result =  (self.cursor.execute(sql,{"WECHATID":WECHATID}))
        self.close()
        return result

    def insert_user(self, SESAID, PHONE, NAME, WECHATID):
        if self.checkuser(WECHATID):
            return 0
        else:
            insert_sql = "INSERT INTO  Foxboro (SESAID,PHONE,NAME,WECHATID) values (\'%s\', \'%s\', \'%s\', \'%s\');" \
                         %(str(SESAID),str(PHONE),str(NAME),str(WECHATID))
            print (insert_sql)
            result =  (self.cursor.execute(insert_sql))
        self.close()
        return result
    def update_wechatid(self, SESAID, WECHATID):
        pass

    def delete_user(self, WECHATID):
        if self.checkuser(WECHATID):
            sql = "delete from Foxboro where WECHATID =%(WECHATID)s"
            result = (self.cursor.execute(sql,{"WECHATID":WECHATID}))
        else:
            result = "No user"
        self.close()
        return result

    def close(self):
        self.db.commit()
        self.cursor.close()
        self.db.close()





