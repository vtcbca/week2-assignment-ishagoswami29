import sqlite3 as sqlite
con=sqlite.connect("c:\\sqlite3\\ems.db")
m="select * from emp_01 order by dept desc"
cur=con.cursor()
cur.execute(m)
r=cur.fetchall()
for i in range(len(r)):
   print("emp id:",(r[i][0]))
   print("emp name:",(r[i][1]))
   print("emp dept:",(r[i][2]))
   print("emp basic:",(r[i][3]))
   print("emp branch:",(r[i][4]))
con.commit()
con.close()
