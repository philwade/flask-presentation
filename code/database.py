from flask import Flask, g
from sqlite3 import dbapi2 as sqlite3
app = Flask(__name__)
app.debug = True

def get_db():
    return sqlite3.connect('test.db')

@app.before_request
def before_request():
    g.db = get_db()

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

@app.route("/")
def home():
    names = g.db.execute("select name from user")
    return "<br>".join([n[0] for n in names])

if __name__ == "__main__":
    app.run()
