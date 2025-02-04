from flask import Flask, render_template
app=Flask(__name__)

@app.route("/lie")
def lie():
    return render_template("lie.html")

@app.route("/head")
def head():
    return render_template("head.html")