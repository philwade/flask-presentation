from flask import Flask, render_template
app = Flask(__name__)
app.debug = True


@app.route("/loop")
def looper():
    a = [x**2 for x in range(10)]
    return render_template('loop.html', values=a)

if __name__ == "__main__":
    app.run()
