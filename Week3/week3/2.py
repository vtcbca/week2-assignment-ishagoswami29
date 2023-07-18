import sqlite3 as sqlite
con=sqlite.connect("c:\\sqlite3\\esm.db")
cur=con.cursor()
q="""insert into emp_01 values(1,'om','IT',5000,'surat'),(2,'sai','HR',7000,'vyara'),(3,'krisha','account',6000,'rajkot'),(4,'dev','Inventory',4000,'ankleshwar'),(5,'aryan','IT',7000,'surat');"""
cur.execute(q)
con.commit()
#insert record using tuple
r=[(6,'khushi','Account',7500,'bardoli'),
   (7,'sana','HR',6000,'surat'),
   (8,'megha','IT',8500,'vyara'),
   (9,'rinkal','Inventory',9500,'navsari'),
   (10,'parth','HR',7400,'bardoli')]
i1="insert into emp_01 values(?,?,?,?,?)"
cur.executemany(i1,r)
con.commit()
# insert record through user input
i2="insert into emp_01 values(?,?,?,?,?)"
l=[]
for a in range(5):
    n=int(input("Enter emp id:"))
    name=input("Enter emp name:")
    dep=input("Enter emp department:")
    basic=int(input("Enter emp basic:"))
    branch=input("Enter emp branch:")
    t=(n,name,dep,basic,branch)
    l.append(t)
cur.executemany(i2,l)
con.commit()
con.close()
