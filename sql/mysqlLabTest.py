#coding=utf-8

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost",'springmvc','root','123456')

# 使用cursor（）方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("select version()")

# 使用fetchone方法获取一条数据库
data = cursor.fetchone()

print 'Database versuib: %s' % data

# 关闭数据库连接
db.close()