import sqlite3

#connecting database to table
conn = sqlite3.connect('Students.db')
#creating cursor for database
#cursor runs query and fetch data fom database
c = conn.cursor()

#creating table if not exists in db.
def table_create():
    c.execute("CREATE TABLE IF NOT EXISTS Students(name TEXT,id REAL)")

#insert data into table
def table_entry():
    c.execute("INSERT INTO Students VALUES('apexa',01)")
    c.execute("INSERT INTO Students VALUES('kashu',02)")
    c.execute("INSERT INTO Students VALUES('ronak',03)")
    c.execute("INSERT INTO Students VALUES('anjana',04)")
    c.execute("INSERT INTO Students VALUES('piyush',05)")

def query():
    db=c.execute("select name from Students order by name asc")
    result=db.fetchall()
    return result
print query()
    
table_create()
table_entry()    
conn.commit()
c.close()
conn.close()


              
              

