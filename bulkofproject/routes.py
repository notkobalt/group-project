#imports
##import flask components
from flask import render_template
##import config from __init__
from bulkofproject import app, db

#app routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search')
def search():
    return render_template('search.html')