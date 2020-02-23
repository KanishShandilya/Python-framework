from flask import Flask,render_template,request,jsonify
import time
app=Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/posts',methods=['POST'])
def posts():
    start=int(request.form.get('start') or 0)
    end=int(request.form.get('end') or (start+9))

    #Generate list of post
    data=[]

    for i in range(start,end+1):
        data.append(f"POST {i}")
    time.sleep(1)
    return jsonify(data)