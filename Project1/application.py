
from flask import Flask, session ,render_template,request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import requests
app = Flask(__name__)


# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine("postgres://dtnlizirzinqoh:628f13a9c751b1baa2373bf575b9539b431302ddbf9607114eb818ad15943aa1@ec2-174-129-41-127.compute-1.amazonaws.com:5432/d8hi5sbk9i7kli")
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    return render_template('index.html')
@app.route("/login",methods=['POST'])
def login():
    name=request.form.get('name')
    password=request.form.get('passwd')
    user=db.execute("SELECT * FROM users WHERE username=:name",{'name':name}).fetchone()
    if user is None:
        return render_template('error.html',message='Incorrect username or password')
    if password==user.password:
        
        return render_template('search.html',user=user)
    else:
        return render_template('error.html',message='Incorrect username or password')
@app.route('/sign',methods=['POST'])
def sign():
    name=request.form.get('username')
    user=db.execute('SELECT * FROM users WHERE username=:name',{'name':name}).fetchone()
    if user is None:
        password=request.form.get('passwd')
        db.execute('INSERT INTO users (username,password) VALUES (:name,:passwd)',{'name':name,'passwd':password})
        db.commit()
        return render_template('log.html')
    else:
        return render_template('error.html',message='USERNAME TAKEN')

@app.route('/processing',methods=['POST'])
def login1():
    return render_template('log.html')
@app.route('/process',methods=['POST'])
def signin1():
    return render_template('sign.html')

@app.route('/BOOKINFO',methods=['POST'])
def search():
    val=int(request.form.get('value'))
    s="%"+request.form.get('searchname')+"%"
    s=s.title()
    if val==1:
        li=db.execute("SELECT * FROM books WHERE isbn LIKE :s",{'s':s}).fetchall()
    elif val==2:
        li=db.execute("SELECT * FROM books WHERE author LIKE :s",{'s':s}).fetchall()
    elif val==3:
        li=db.execute("SELECT * FROM books WHERE title LIKE :s",{'s':s}).fetchall()
    return render_template('lis.html',lis=li)

   
@app.route('/BOOKINFO/<isbn>')
def info(isbn):
    res=requests.get('https://www.goodreads.com/book/review_counts.json', params={"key": "5NN4kXAIDTjkjjIXWUCBA", "isbns": isbn})
    data=res.json()
    d=data['books'][0]
    return render_template('info.html',data=d)