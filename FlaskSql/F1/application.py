from flask import request,render_template,Flask

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

engine=create_engine('postgres://postgres:mkempire081@localhost:5432/Kanish')

db=scoped_session(sessionmaker(bind=engine))

app=Flask(__name__)

@app.route("/")
def index():
    flights=db.execute('SELECT * FROM flights').fetchall()
    return render_template("index.html",flights=flights)

@app.route('/Book',methods=["POST"])
def book():
    name=request.form.get("name")
    #Making sure flight_i is an integer
    try:
        flight_id=int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html",message="Invalid Flight Number")
    #Making sure there is a flight with that flight_id
    if db.execute('SELECT * FROM flights WHERE id=:f_id',{'f_id':flight_id}).rowcount==0:
        return render_template('error.html',message='No such flights with that id')
    db.execute('INSERT INTO passengers (name,flight_id) VALUES(:n,:f)',{'n':name,'f':flight_id})
    db.commit()
    return render_template("success.html")

@app.route('/flights')
def flights():
    flights=db.execute('SELECT * FROM flights').fetchall()
    return render_template('flights.html',flights=flights)

#:flight_id is a placeholder
@app.route('/flights/<int:flight_id>')
def flig(flight_id):
    fli=db.execute("SELECT * FROM flights WHERE id=:f",{'f':flight_id}).fetchone()
    if fli is None:
        return render_template('error.html',message="No such flights")
    passengers=db.execute('SELECT name FROM passengers WHERE flight_id=:i',{'i':flight_id}).fetchall()
    return render_template('flight.html',flight=fli,passengers=passengers)
