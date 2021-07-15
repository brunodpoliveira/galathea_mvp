from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from typing import Callable
from chatbot import bot
from thumbs import *
import os


# --------------------------------------
# this block solves the unresolved attribute column problem
class MySQLAlchemy(SQLAlchemy):
    Column: Callable  # Use the typing to tell the IDE what the type is.
    String: Callable
    Integer: Callable
    Text: Callable


# --------------------------------------

# GUI + website
app = Flask(__name__)
# switches from deployment to development sever
ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    # database config is 'postgresql://username:password@serveradress/servername
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'postgresql://postgres:postgres@localhost/gala_feedback'

else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'postgres://zgxkmcyqmtbatf:e673ec62df8cc8da9fc437c335c0d7a185ebb89943435e0c33c0a2d52457dc35@ec2-54-91-188-254.compute-1.amazonaws.com:5432/d3s3flqffn3aj3'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = MySQLAlchemy(app)


# --------------------------------------

# TODO refactor feedback to thumbs up/down system
class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), unique=True)
    text_bot = db.Column(db.String(200))
    thumbs_up = db.Column(db.String(200))
    thumbs_down = db.Column(db.String(200))

    def __init__(self, customer, text_bot, thumbs_up, thumbs_down):
        self.customer = customer
        self.text_bot = text_bot
        self.thumbs_up = thumbs_up
        self.thumbs_down = thumbs_down


# --------------------------------------

@app.route("/")
def home():
    return render_template("index.html")


# --------------------------------------

@app.route("/get")
def get_bot_response():
    usertext = request.args.get('msg')
    return str(bot.get_response(usertext))


# --------------------------------------

@app.route('/submit', methods=['POST'])
def thumbs():
    if request.method == 'POST':
        pass

        # if the customer's name is not on database, it will add its feedback to it
        """
        if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
            data = Feedback(customer, text_bot, thumbs_up, thumbs_down)
            db.session.add(data)
            db.session.commit()
            send_mail(customer, text_bot, thumbs_up, thumbs_down)
            return render_template('success.html')
        """


if __name__ == "__main__":
    app.run()
# --------------------------------------
