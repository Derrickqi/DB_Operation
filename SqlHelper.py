#!/usr/bin/python3
import pymysql.cursors
import traceback


class DbInfo(object):
    def __init__(self, host, username, password, database, port):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.port = port
        self.db = pymysql.connect(host=self.host, user=self.username, password=self.password, database=self.database,
                                  port=self.port, charset='utf8')

    def SelectAllDB(self, sql, args):
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql, args)
            data = self.cursor.fetchall()
            self.db.close()
            print(data)
            return data
        except Exception as e:
            traceback.print_exc()
        finally:
            self.cursor.close()

    def SelectOneDB(self, sql, args):
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql, args)
            data = self.cursor.fetchone()
            self.db.close()
            print(data)
            return data
        except Exception as e:
            traceback.print_exc()
        finally:
            self.cursor.close()

    def InsertDB(self, sql, args):
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql, args)
            self.db.commit()
            self.db.close()
        except Exception as e:
            traceback.print_exc()
            self.db.rollback()
        finally:
            self.cursor.close()

    def UpdateDB(self, sql, args):
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql, args)
            self.db.commit()
            self.db.close()
        except Exception as e:
            traceback.print_exc()
            self.db.rollback()
        finally:
            self.cursor.close()

    def DeleteDB(self, sql, args):
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql, args)
            self.db.commit()
            self.db.close()
        except Exception as e:
            traceback.print_exc()
            self.db.rollback()
        finally:
            self.cursor.close()


DbInfo = DbInfo("192.168.1.156", "root", "123qqq...A", "schoolInfo", 3306)
# DbInfo.SelectAllDB("select name from student where age=%s", 22)
# DbInfo.SelectOneDB("select name from student where age=%s", 22)
# DbInfo.InsertDB("insert into student(name,age) values(%s,%s)", ['qihao', 27])
# DbInfo.UpdateDB("update student set name=%s where name=%s", ['DerrickQi', 'qihao'])
# DbInfo.DeleteDB(("delete from student where name=%s"), ['DerrickQi'])