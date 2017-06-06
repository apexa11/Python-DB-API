import datetime

POSTS =[("This is the first post", datetime.datetime.now())]

def get_posts():
    "return all post from database the most recent first"
    return reversed(POST)

def add_post():
    "add post to database with current time stamp"
    POST.append((content,datetime.datetime.now()))

