import os
import env
import csv
import datetime
from db import db
from twitter import twitter_api
from flask import Flask, render_template, jsonify, redirect
from flask_bootstrap import Bootstrap
import pandas as pd

from models.localities import LocalitiesModel

# APP SETTINGS

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['DEBUG'] = True

Bootstrap(app)


## Main View
@app.route('/')
def dashboard():
    dataset = LocalitiesModel.get_all()
    return render_template('dashboard.html', dataset=dataset)


@app.route('/upload')
def upload():
    # create context
    with open('geo1.csv', encoding="utf8") as f:
        # read csv
        reader = csv.reader(f)
        # omit header by skipping first row in iterator
        headers = next(reader)
        for row in reader:
            try:
                new_locality = LocalitiesModel(locality=row[0], area=row[1], country=row[2], woeid=row[3])
                new_locality.save_to_db()
            except Exception as e:
                pass
    return redirect('/')


@app.errorhandler(404)
def error404(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def error500(error):
    return render_template('500.html'), 500


## DB INIT
db.init_app(app)

if __name__ == '__main__':

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run()

# Heroku
#     port = int(os.environ.get('PORT', 5000))
#     app.run(host='0.0.0.0', port=port)
