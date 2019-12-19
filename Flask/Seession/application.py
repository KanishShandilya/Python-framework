#Note taking application
from flask import Flask,render_template,request,session
#giving access to session variable which keeps data user specific
from flask_session import Session
#More control over session
#Storing session to server side
app=Flask(__name__)

app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]="filesystem"

Session(app)

@app.route("/",methods=["GET","POST"])
def index():
    #if session["notes"] doesn't exist create session["notes"] as empty list
    if session.get("notes") is None:
        session["notes"]=[]
    #Each Particular session have empty list of notes
    if request.method== "POST":
        note=request.form.get("note")
        session["notes"].append(note)
    return render_template('index.html',notes=session["notes"])
