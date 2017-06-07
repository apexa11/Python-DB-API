import datetime
import psycopg2, bleach

DBNAME = 'forum'

POSTS =[("This is the first post", datetime.datetime.now())]

def get_posts():
    "return all post from database the most recent first"
    conn = psycopg2.connect(database=DBNAME)
    c= conn.cursor()
    c.execute("select content , time from posts order by time desc")

    posts = c.fetchall()
    c.close()
    conn.close()
    return posts


def add_post():
    "add post to database with current time stamp"
    conn = psycopg2.connect(database=DBNAME)
    c = conn.cursor()
    c.execute("insert into posts values %s" , (bleach.clean(content),))
    c.execute("update posts set content = 'cheese' where content like 'spam%'")
    c.execute("delete from posts where content = 'cheese'")
    POST.append((content,datetime.datetime.now()))
    conn.commit()
    conn.close()

