import sqlite3

conn = sqlite3.connect('customer.db')
c = conn.cursor()

def table_create():
    c.execute("CREATE TABLE IF NOT EXISTS customer(id REAL,name TEXT,company TEXT)")

def data_entry():
    c.execute("INSERT INTO customer VALUES(01,'apexa','oracle')")
    c.execute("INSERT INTO customer VALUES(02,'kashu','booz')")
    c.execute("INSERT INTO customer VALUES(03,'ronak','L&T')")
    c.execute("INSERT INTO customer VALUES(04,'bhumi','OTP')")
    c.execute("INSERT INTO customer VALUES(05,'nishu','percolate')")
    c.execute("INSERT INTO customer VALUES(05,'nishu','percolate')")

    conn.rollback()
    c.close()
    conn.close()

table_create()
data_entry()

    
    
    
    
