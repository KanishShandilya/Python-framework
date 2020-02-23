from flask import render_template,request,jsonify,Flask

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/posts",methods=["POST"])
def post():
    start=int(request.form.get("start")) or 0
    end=int(request.form.get("end")) or start+9

    data=[]

    for i in range(start,end+1):
        data.append(f"Post {i}")
    
    return jsonify(data)