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
from bulkofproject.gameapi import randomGame

# register blueprints
app.register_blueprint(classesminilab, url_prefix='/classes')
app.register_blueprint(bubblesortminilab, url_prefix='/bubble_sort')
app.register_blueprint(jacobblueprint, url_prefix='/jacobblueprint')
app.register_blueprint(jacobbubblesort, url_prefix='/jacobbubblesort')



# app routes
@app.route('/')
def home() :
    return render_template('home.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        titlesdictionary = {}
        titleslist =[]
        searchurl = "https://api.rawg.io/api/games?key=91edf65dde2d49c7a6519987ed7c1769&search="

        #get entry from POST form
        searchentry = request.form['search']
        searchlink = searchurl + searchentry

        #send request to RAWG API game database
        searchresponse = requests.request("GET", searchlink)
        searchdump = searchresponse.json()
        searchresults = searchdump['results']

        for item in searchresults:
            titleslist.append(item['name'])

        #append all titles to a dictionary
        for item in searchresults:
            titlesdictionary[item['name']] = item['background_image']

        #format for HTML
        displaylinks = ""
        for x, y in titlesdictionary.items():
            if y == None:
                displaylinks = displaylinks + "<a href=#><div class='container'> <img class='icon' src='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.tlDKZhACEaIkaATgSSsXygAAAA%26pid%3DApi&f=1'><div class='title'>" + x + "</div></div></a>"
            else:
                displaylinks = displaylinks + "<a href=#><div class='container'> <img class='icon' src='" + y + "'><div class='title'>" + x + "</div></div></a>"
        print(displaylinks)

        return render_template(('search.html'), displaylinks = displaylinks, displayMessage = randomGame(titleslist))
    return render_template('search.html')

@app.route('/login')
def login() :
    return render_template('login.html')

@app.route('/signup')
def signup() :
    return render_template('signup.html')

@app.route('/easter')
def easter() :
    return render_template('easteregg.html')

@app.route('/profile')
def profile() :
    return render_template('profile.html')