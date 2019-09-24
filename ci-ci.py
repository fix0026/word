import pymysql
import jsonpath
import json

conn = pymysql.connect(host="192.168.1.250", port=3306, user="hz", password="xdkj@2018", database="word", charset="utf8")
print("数据库连接成功")
cursor = conn.cursor()
f = open("ci.json", encoding='utf-8')
s = f.read()
n = json.loads(s)
x = jsonpath.jsonpath(n, '$..ci')
for y in x:
    sql1 = 'insert into ci(ci) values ("%s")' % pymysql.escape_string(y)
    print(sql1)
    cursor.execute(sql1)
    conn.commit()
cursor.close()
conn.close()
