from flask import Flask,render_template,request
import csv
from models import *

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]='postgres://postgres:mkempire081@localhost:5432/Kanish'
app.config["SQLALCHEMY_TRACK_MODIFICATION"]=False

db.init_app(app)

def main():
    f=open("a.csv")
    reader=csv.reader(f)
    for origin,destination,duration in reader:
        flight=Flight(origin=origin,destination=destination,duration=duration)
        db.session.add(flight)#Add flight to database
        '''
    DELETE FROM flights WHERE id=28;
    flight=Flight.query.get(28)
    db.session.delete(flight)
    '''
    db.session.commit()
    

if __name__=="__main__":
    with app.app_context():
        main()