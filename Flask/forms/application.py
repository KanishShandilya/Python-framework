from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/Hello", methods=["POST", "GET"])
def hello():
    if request.method == "POST":
        name=request.form.get("name")
        return render_template("hello.html",name=name)
    else:
        return "Please Submit The Form Instead"