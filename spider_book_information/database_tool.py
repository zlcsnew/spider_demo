#!-*- coding:utf-8 -*-
import MySQLdb
import config
def init():
    db = MySQLdb.connect("localhost", config.username, config.password, config.database_name, charset='utf8');
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS %s"%(config.table_name));
    sql = """CREATE TABLE %s (
             BookName  CHAR(40) NOT NULL,
             author  CHAR(40),
              price CHAR(12),
              outcomingtime  CHAR(20))"""%(config.table_name)
    cursor.execute(sql)
    db.close()

def insert_item(content_item):
    db = MySQLdb.connect("localhost", config.username, config.password, config.database_name,charset='utf8')
    cursor = db.cursor()
    for item in content_item:
       print item[0]
       sql = """INSERT INTO %s(BookName,author,price,outcomingtime)VALUES ('%s','%s','%s','%s')"""%(config.table_name,item[0].decode(),item[1].decode(),item[2].decode(),item[3].encode())
       cursor.execute(sql)
    db.commit()
    db.close()
