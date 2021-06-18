#imports
import requests
##import website components
from flask import render_template, session, jsonify, request
##import config from __init__
from bulkofproject import app
#import models
from bulkofproject.models import rating
##import blueprints
from bulkofproject.account import account
from bulkofproject.reviews import reviews_bp
from bulkofproject.kira import kiradirectory
from bulkofproject.roop import roopdirectory
from bulkofproject.dylan import dylandirectory
from bulkofproject.lucas import lucasdirectory
from bulkofproject.jacob import jacobdirectory

#register blueprints

app.register_blueprint(reviews_bp, url_prefix='/reviews')
app.register_blueprint(account, url_prefix='/account')
app.register_blueprint(kiradirectory, url_prefix='/kira')
app.register_blueprint(roopdirectory, url_prefix='/roop')
app.register_blueprint(dylandirectory, url_prefix='/dylan')
app.register_blueprint(lucasdirectory, url_prefix='/lucas')
app.register_blueprint(jacobdirectory, url_prefix='/jacob')



# app routes
@app.route('/')
def home() :
    #in session (logged in)
    if 'user' in session:
        user = session['user']
        return render_template('home.html', user = user)
    #not in session (logged out)
    return render_template('home.html')

@app.route('/easter', methods = ["GET", "POST"])
def easter() :
    weatherresponse = requests.request("GET", "https://fish.nighthawkcodingsociety.com/all_ideal_weathers")
    weatherdump = weatherresponse.json()
    weatherresults = weatherdump["all_ideal_weathers"]

    return render_template('easteregg.html', weatherresults = weatherresults)

@app.route('/ratingAPI', methods = ['GET', 'POST'])
def accessratings():
    ratings = rating.query.all()
    ratinglist = []

    for item in ratings:
        ratinglist.append({'id':item.id, 'game':item.game, 'stars':item.stars, 'review': item.review, 'user': item.user})

    response = jsonify({"ratings": ratinglist})
    return response