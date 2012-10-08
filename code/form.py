from flask import Flask, render_template, request
app = Flask(__name__)
app.debug = True


@app.route("/loop", methods=["POST", "GET"])
def looper():
    if request.method == "POST":
        i = int(request.form['endpoint'])
    else:
        i = 10
    a = [x**2 for x in range(i)]
    return render_template('loop.html', values=a)

@app.route("/form")
def form():
    return render_template('form.html')

if __name__ == "__main__":
    app.run()
