#flask is framework of python

from flask import Flask

app = Flask(__name__)

#@ signifies a decorator -wrap a function and modifying its behaviour 
@app.route('/')
def index():
    return 'this is my main page'

@app.route('/about')
def about():
    return "this is my about page"

@app.route('/contact')
def contact():
    return "this is my contact page"

@app.route('/profile/<username>')
def profile(username):
    return "<h1>hey there,%s</h1>" %username
    
if __name__ == '__main__':
    app.run(debug=True)

