"""
drop table user;
create table user(uid,pwd);
insert into user(uid,pwd) values('userid1','password1');
insert into user(uid,pwd) values('userid2','password2');
insert into user(uid,pwd) values('userid3','password3');
"""




import sqlite3
dbname='TestDB.db'
uid="userid1"
pwd="password1"

#データがない
#uid="xxxxx"
#pwd="xxxxx"

conn=sqlite3.connect(dbname)
c = conn.cursor()
select_sql = "select * from user where uid='"+uid+"' and pwd='"+pwd+"'"
print(select_sql)
c.execute(select_sql)
data=c.fetchall()
if len(data)==0:
   print("データがありません")
else:
   print("データがあります")
for row in c.execute(select_sql):
        print(row[0],"-----",row[1])
conn.close()
    