#imports
##import flask components
from flask import render_template
##import config from __init__
from bulkofproject import app, db
from bulkofproject.classesminilab import classesminilab
from bulkofproject.bubblesortminilab import bubblesortminilab
from bulkofproject.classesminilab.jacobminilab import jacobblueprint

# register blueprints
app.register_blueprint(classesminilab, url_prefix='/classes')
app.register_blueprint(bubblesortminilab, url_prefix='/bubble_sort')
app.register_blueprint(jacobblueprint, url_prefix='/jacobblueprint')



# app routes
@app.route('/')
def home() :
    return render_template('home.html')


@app.route('/search')
def search() :
    return render_template('search.html')