## App Utilities
import os
import env
import datetime
from twitter import twitter_api
from flask import Flask, render_template, jsonify
from flask_bootstrap import Bootstrap


# APP SETTINGS

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['DEBUG'] = True

Bootstrap(app)


## Main View
@app.route('/')
def dashboard():

    return render_template('dashboard.html')


@app.errorhandler(404)
def error404(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def error500(error):
    return render_template('500.html'), 500


if __name__ == '__main__':


    app.run()

# Heroku
#     port = int(os.environ.get('PORT', 5000))
#     app.run(host='0.0.0.0', port=port)