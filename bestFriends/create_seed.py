from app import db
from models import *
from flask_sqlalchemy import SQLAlchemy

db.drop_all()
db.create_all()



friend1 = Friend("Wes")
friend2 = Friend("Me")
friend3 = Friend("Julissa")
friend4 = Friend("Tasfia")


db.session.add(friend1)
db.session.add(friend2)
db.session.add(friend3)
db.session.add(friend4)

db.session.commit()


print("Created and seeded")











