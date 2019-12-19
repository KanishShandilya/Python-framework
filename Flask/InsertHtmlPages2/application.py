from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():
    head="This is HeadLine"
    return render_template("prac12.html",headline=head)
@app.route("/bye")
def bye():
    headline="Thank You"
    ert="Pass"
    return render_template("prac12.html",headline=headline,ert=ert)