import sqlite3 as sqlite
con=sqlite.connect("c:\\sqlite3\\esm.db")
c="create table emp_01(eid int primary key,ename text,dept text,basic int,branch text)"
cur=con.cursor()
cur.execute(c)
con.commit()
con.close
