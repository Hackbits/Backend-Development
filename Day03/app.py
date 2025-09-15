from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html",message = "Hello from flask templates,Today is Day 3.")

@app.route("/base")
def base():
    return render_template("base.html")

@app.route("/about")
def about():
    return render_template("about.html")
