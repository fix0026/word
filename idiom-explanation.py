import pymysql
import jsonpath
import json
import time
conn = pymysql.connect(host="192.168.1.250", port=3306, user="hz", password="xdkj@2018", database="word", charset="utf8")
print("数据库连接成功")
cursor = conn.cursor()
f = open("idiom.json", encoding='utf-8')
s = f.read()
n = json.loads(s)
x = jsonpath.jsonpath(n, '$..explanation')
i = 0
for y in x:
    i = i+1
    sql2 = 'UPDATE idiom set explanation="%s" where id=%s;' % (pymysql.escape_string(y), i)
    print(sql2)
    #time.sleep(0.5)
    cursor.execute(sql2)
    conn.commit()
cursor.close()
conn.close()
