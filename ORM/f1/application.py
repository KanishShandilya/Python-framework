from flask import Flask,render_template,request,jsonify
from models import *

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='postgres://postgres:mkempire081@localhost:5432/Kanish'
app.config["SQLALCHEMY_TRACK_MODIFICATION"]=False

db.init_app(app)

@app.route("/")
def index():
    flights=Flight.query.all()
    return render_template("index.html",flights=flights)

@app.route('/book',methods=["POST"])
def book():
    nam=request.form.get("na")
    
    try:
        flight_id=int(request.form.get("fli"))
    except ValueError:
        return render_template("error.html",message="Invalid Flight id")
    flight=Flight.query.get(flight_id)
    if flight is None:
        return render_template('error.html',message="No such flights with that Id")
    #Adding Passenger
    # passenger=Passengers(name=nam,flight_id=flight_id)
    # db.session.add(passenger)
    # db.session.commit()
    flight.add_passenger(nam)
    return render_template('success.html',message="Your Booking Is Successful")

@app.route('/flights')
def flight():
    flight=Flight.query.all()
    return render_template('flights.html',flights=flight)
    
@app.route('/flights/<int:flight_id>')
def flig(flight_id):
    fli=Flight.query.get(flight_id)
    if fli is None:
        return render_template('error.html',message="Not available")
    passengers=Passengers.query.filter_by(flight_id=flight_id).all()
    return render_template('flight.html',flight=fli,passengers=passengers)

#Building our api
@app.route("/api/flights/<int:flight_id>")
def flights_api(flight_id):
    flight=Flight.query.get(flight_id)
    if flight is None:
        return jsonify({"error":"Invalid Flight_id"}),422
    #Get all passengers
    passengers=flight.passengers
    names=[]
    for passenger in passengers:
        names.append(passenger.name)
    return jsonify({
        "origin":flight.origin,
        "destination":flight.destination,
        "duration":flight.duration,
        "passengers":names
    })