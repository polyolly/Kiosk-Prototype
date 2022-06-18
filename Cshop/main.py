from flask import Flask, redirect, url_for, render_template

app= Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html", content="Testing")
@app.route("/base.html")
def base():
    return render_template("base.html", content="Testing")
@app.route("/hot.html")
def hot():
    return render_template("hot.html", content="Testing")
@app.route("/dessert.html")
def dessert():
    return render_template("dessert.html", content="Testing")
@app.route("/modal")
def modal():
    return render_template("modal.html", content="Testing")


if __name__ == "__main__":
    app.run(debug=True, port=7777)