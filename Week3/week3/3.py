import sqlite3 as sqlite
con=sqlite.connect("c:\\sqlite3\\ems.db")
i="update emp_01 set basic=basic+(basic*10)/100 where branch='surat'"
cur=con.cursor()
cur.execute(i)
con.commit()
con.close()
	
