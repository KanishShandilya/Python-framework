import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
engine=create_engine("postgres://dtnlizirzinqoh:628f13a9c751b1baa2373bf575b9539b431302ddbf9607114eb818ad15943aa1@ec2-174-129-41-127.compute-1.amazonaws.com:5432/d8hi5sbk9i7kli")
db=scoped_session(sessionmaker(bind=engine))

def main():
    f=open('books.csv')
    reader=csv.reader(f)

    for isbn,title,author,year in reader:
        db.execute('INSERT INTO books (isbn,title,author,year) VALUES (:in,:ti,:as,:ya)',
                    {'in':isbn,'ti':title,'as':author,'ya':year})
    db.commit()
    print("SAVED")
    
if __name__=="__main__":
        main()