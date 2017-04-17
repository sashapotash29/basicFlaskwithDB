from flask_sqlalchemy import SQLAlchemy 
from flask import Flask 
from app import db






class Friend(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(30))

	def __init__(self, name):
		self.name = name





def grab_all_friends():
	list_of_friends = Friend.query.all()
	return list_of_friends


def add_a_friend(name):
	new_friend = Friend(str(name))
	db.session.add(new_friend)
	db.session.commit()
	return










