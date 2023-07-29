import sqlite3
cnt=sqlite3.connect("mystore.db")
#_____________________CREATE PRODUCTS TABLE____________________________________
##sql='''CREATE TABLE products(
##        id INTEGER PRIMARY KEY,
##        pname CHAR(30) NOT NULL,
##        price INTEGER NOT NULL,
##        qnt INTEGER NOT NULL
##        )'''
##cnt.execute(sql)
#_____________________INSERT DATA INTO PRODUCTS TABLE______________________
##sql=''' INSERT INTO products(pname,price,qnt)
##            VALUES("Tuna",70000,38)'''
##cnt.execute(sql)
##cnt.commit()
#_____________________CREATE CART TABLE__________________________________________
##sql='''CREATE TABLE cart(
##        id INTEGER PRIMARY KEY,
##        uid INTEGER NOT NULL,
##        pid INTEGER NOT NULL,
##        qnt INTEGER NOT NULL
##        )'''
##cnt.execute(sql)
