#imports
##import website components
from flask import render_template, request, session, redirect, url_for, jsonify, flash
##import config from __init__
from bulkofproject import app
#import models
from bulkofproject.models import User, rating
##import blueprints
from bulkofproject.classesminilab import classesminilab
from bulkofproject.bubblesortminilab import bubblesortminilab
from bulkofproject.classesminilab.jacobminilab import jacobblueprint
from bulkofproject.classesminilab.jacobbubblelab import jacobbubblesort
from bulkofproject.account import account
from bulkofproject.reviews import reviews_bp

#register blueprints
app.register_blueprint(classesminilab, url_prefix='/classes')
app.register_blueprint(bubblesortminilab, url_prefix='/bubble_sort')
app.register_blueprint(jacobblueprint, url_prefix='/jacobblueprint')
app.register_blueprint(jacobbubblesort, url_prefix='/jacobbubblesort')
app.register_blueprint(reviews_bp, url_prefix='/reviews')
app.register_blueprint(account, url_prefix='/account')



# app routes
@app.route('/')
def home() :
    #in session (logged in)
    if 'user' in session:
        user = session['user']
        return render_template('home.html', user = user)
    #not in session (logged out)
    return render_template('home.html')

@app.route('/easter')
def easter() :
    return render_template('easteregg.html')

@app.route('/ratingAPI', methods = ['GET', 'POST'])
def accessratings():
    ratings = rating.query.all()
    ratinglist = []

    for item in ratings:
        ratinglist.append({'id':item.id, 'game':item.game, 'stars':item.stars, 'review': item.review, 'user': item.user})

    response = jsonify({"ratings": ratinglist})
    return response