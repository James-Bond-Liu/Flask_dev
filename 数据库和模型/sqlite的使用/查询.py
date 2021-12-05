#导入SQLite驱动：
import sqlite3
#连接到SQlite数据库
#数据库文件是test.db，不存在，则自动创建
conn = sqlite3.connect('test.db')
#创建一个cursor：
cursor = conn.cursor()
#执行查询语句：
# cursor.execute('select *from user where id=?', ('1',))
cursor.execute('select *from user where id=1')
#使用featchall获得结果集（list）
values = cursor.fetchall()
print(values) #result:[('1', 'Michael')]
#关闭cursor
#关闭conn
cursor.close()
conn.close()