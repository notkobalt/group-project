#imports
##import website components
from flask import render_template, request, session, redirect, url_for, jsonify, flash
##import config from __init__
from bulkofproject import app, db
#import models
from bulkofproject.models import User, rating
##import blueprints
from bulkofproject.classesminilab import classesminilab
from bulkofproject.bubblesortminilab import bubblesortminilab
from bulkofproject.classesminilab.jacobminilab import jacobblueprint
from bulkofproject.classesminilab.jacobbubblelab import jacobbubblesort
from bulkofproject.reviews import reviews_bp

#register blueprints
app.register_blueprint(classesminilab, url_prefix='/classes')
app.register_blueprint(bubblesortminilab, url_prefix='/bubble_sort')
app.register_blueprint(jacobblueprint, url_prefix='/jacobblueprint')
app.register_blueprint(jacobbubblesort, url_prefix='/jacobbubblesort')
app.register_blueprint(reviews_bp, url_prefix='/reviews')



# app routes
@app.route('/')
def home() :
    #in session (logged in)
    if 'user' in session:
        user = session['user']
        return render_template('home.html', user = user)
    #not in session (logged out)
    return render_template('home.html')

@app.route('/login', methods = ['GET', 'POST'])
def login() :
    if request.method == 'POST':
        #set up future session data
        session.pop('user', None)
        session.permanent = True

        #get elements from front end
        username = request.form['username']
        password = request.form['password']

        #query database
        users = User.query.all()

        #check username/password match
        try:
            user = [user for user in users if user.username == username][0]
            #password match
            if user and user.password == password:
                #enter user into session
                session['user'] = user.username
                return redirect(url_for('home'))
            #no match
            else:
                #flash("Incorrect Username or Password")
                return redirect(url_for('login'))
        except:
            #flash("Incorrect Username or Password")
            return redirect(url_for('login'))
    else:
        if 'user' in session:
            #flash ("User Already Logged In")
            return redirect(url_for('home'))
        else:
            return render_template('login.html')


@app.route('/signup', methods = ['GET', 'POST'])
def signup() :
    if 'user' in session:
        #flash ("User Already Logged In")
        return redirect(url_for('home'))
    elif request.method == 'POST':
        #get elements from front end
        username = request.form['username']
        password = request.form['password']
        confirmpassword = request.form['confirmPassword']

        #check to see if passwords match
        if password == confirmpassword:
            commit = User(username = username, password = password)
            db.session.add(commit)
            db.session.commit()
        return render_template('signup.html')
    else:
        return render_template('signup.html')

@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user', None)
        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))

@app.route('/api')
def websiteapi():
    reviewsquery = rating.query.all()
    reviewslist = []

    for review in reviewsquery:
        reviewslist.append({'game':review.game, 'stars':review.stars, 'review':review.review, 'user':review.user})

    gamejson = jsonify({'reviewslist':reviewslist})
    return gamejson