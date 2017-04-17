from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import models


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bestFriends.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 


db = SQLAlchemy(app)





@app.route("/", methods=['GET'])
def show_homepage():
	list_of_friends = models.grab_all_friends()
	return render_template('home.html',
		list_of_friends=list_of_friends)

@app.route("/addfriend/<new_name>", methods=['GET'])
def add_my_new_friend(new_name):
	models.add_a_friend(new_name)
	print("new name has been added")
	return "ok I'll return something"




if __name__ == "__main__":
	app.run(debug=True, port = 3000)

