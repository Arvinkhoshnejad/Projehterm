import sqlite3
cnt=sqlite3.connect("mystore.db")

def getAllProducts():
    sql='''SELECT * FROM products'''
    result=cnt.execute(sql)
    row=result.fetchall()
    return row



def getAllProduct(pid):
    sql='''SELECT * FROM products WHERE id=?'''
    result=cnt.execute(sql,(pid,))
    row=result.fetchone()
    return row

def getAllCarts(uid):
    sql='''SELECT * FROM cart WHERE uid=?'''
    result=cnt.execute(sql, (uid,))
    row=result.fetchall()
    return row

def Add_Product(pname, price, qnt):
    sql='''INSERT INTO products (pname,price,qnt) VALUES(?,?,?)'''
    cnt.execute(sql,(pname,price,qnt))
    cnt.commit()

def buyValidate(pid,qnt):
    if pid=="" or qnt=="":
        return False,"please fill the inputs"
    
    sql='''SELECT * FROM products WHERE id=?'''
    result=cnt.execute(sql,(pid,))
    row=result.fetchone()
    if not row:
        return False,"wrong product id"
    
    sql='''SELECT * FROM products WHERE id=? AND qnt>=?'''
    result=cnt.execute(sql,(pid,qnt))
    row=result.fetchone()
    if not row:
        return False,"not enough products!"
    
    return True,""

def savetocart(uid,pid,qnt):
    sql='''INSERT INTO cart (uid,pid,qnt) VALUES(?,?,?)'''
    cnt.execute(sql,(uid,pid,qnt))
    cnt.commit()

def updateqnt(pid,qnt):
    sql='''UPDATE products SET qnt=(qnt)-? WHERE id=?'''
    cnt.execute(sql,(qnt,pid))
    cnt.commit()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
