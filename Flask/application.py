from flask import Flask

app=Flask(__name__)#Web Aplication is Flask and __name__ -> current File

@app.route("/")#"/" is default route We are saying through decorator
# that if route is default run index
def index():
    return "Hello World!!!!"

@app.route("/Kanish")
def pro():
    return "You Are Pro:)"
@app.route("/Aditya")
def noob():
    return "You are Noob:("
@app.route("/Tripathi")
def motu():
    return "You are Motu :)"
@app.route("/Abhishek")
def smile():
    return "Smile while taking Photos :)"
@app.route("/<string:name>")
def hell(name):
    return f"<h1>Hello {name.capitalize()}</h1>"
#Takes every input string after default and put it as name