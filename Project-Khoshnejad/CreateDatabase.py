import sqlite3
cnt=sqlite3.connect("mystore.db")
#print("Database has been created successfully!")
#_____________________CREATE TABLE____________________________________
##sql='''CREATE TABLE users(
##        id INTEGER PRIMARY KEY,
##        user CHAR(15) NOT NULL,
##        pass CHAR(30) NOT NULL,
##        addr TEXT,
##        grade INTEGER NOT NULL
##        )'''
##cnt.execute(sql)
#____________________INSERT DATA_______________________________________
##sql=''' INSERT INTO users(user,pass,addr,grade)
##            VALUES("Mitra","123456789","Mashhad",1)'''
##cnt.execute(sql)
##cnt.commit()
