from flask import Flask,render_template,request
from models import *

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]='postgres://postgres:mkempire081@localhost:5432/Kanish'
app.config["SQLALCHEMY_TRACK_MODIFICATION"]=False

db.init_app(app)

def main():
    flights=Flight.query.all()
    '''
    SELECT * FROM flights WHERE origin="PARIS" Limit 1;
    Flight.query.filter_by(origin="PARIS").first()=>Returns null if no column is returned
    No of rows returned
    Flight.query.filter_by(origin="PARIS").count()
    id as primary key
    Flight.query.filter_by(id=28).first()
    Flight.query.get(28)


    Updating
    UPDATE flights SET duration=280 WHERE id=6;
    flight=Flight.query.get(6)
    flight.duration=280
    commit changes at the end
    
    
    '''
    for flight in flights:
        print(flight.origin," ",flight.destination," ",flight.duration)
    
if __name__=="__main__":
    with app.app_context():
        main()