#imports
##import flask components
from flask import render_template
##import config from __init__
import requests, json
from flask import request
from bulkofproject import app, db
from bulkofproject.classesminilab import classesminilab
from bulkofproject.bubblesortminilab import bubblesortminilab
from bulkofproject.classesminilab.jacobminilab import jacobblueprint
from bulkofproject.classesminilab.jacobbubblelab import jacobbubblesort
from bulkofproject.reviews import reviews_bp

# register blueprints
app.register_blueprint(classesminilab, url_prefix='/classes')
app.register_blueprint(bubblesortminilab, url_prefix='/bubble_sort')
app.register_blueprint(jacobblueprint, url_prefix='/jacobblueprint')
app.register_blueprint(jacobbubblesort, url_prefix='/jacobbubblesort')
app.register_blueprint(reviews_bp, url_prefix='/reviews')



# app routes
@app.route('/')
def home() :
    return render_template('home.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        #request
        titleslist = []
        displaylinks = ''
        searchurl = "https://api.rawg.io/api/games?key=91edf65dde2d49c7a6519987ed7c1769&search="
        searchentry = request.form['search']
        searchlink = searchurl + searchentry

        searchresponse = requests.request("GET", searchlink)
        searchdump = searchresponse.json()
        searchresults = searchdump['results']

        #for display on front end
        for item in searchresults:
            titleslist.append(item['name'])

        for index in titleslist:
            displaylinks = displaylinks +  "<a href=#>" + index + "</a></br> "

        return render_template(('search.html'), displaylinks = displaylinks)
    return render_template('search.html')

@app.route('/login')
def login() :
    return render_template('login.html')

@app.route('/signup')
def signup() :
    return render_template('signup.html')