from flask import Flask, session, request, redirect, url_for, render_template
app = Flask(__name__)
app.debug = True
app.secret_key = 'badger'

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session['username'] = request.form['user']
        session['logged_in'] = True
        return redirect(url_for('home'))
    else:
        return render_template('login.html')

@app.route("/")
def home():
    if session.get('logged_in'):
        return "You are logged in as %s" % session.get('username')
    else:
        return "You are not logged in"

if __name__ == "__main__":
    app.run()
