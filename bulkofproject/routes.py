#imports
##import flask components
from flask import render_template
##import config from __init__
from bulkofproject import app, db
from bulkofproject.classesminilab import lab
from bulkofproject.classesminilab.jacobminilab import jacobblueprint

# register blueprints
app.register_blueprint(lab, url_prefix='/lab')
app.register_blueprint(jacobblueprint, url_prefix='/jacobblueprint')


# app routes
@app.route('/')
def home() :
    return render_template('home.html')


@app.route('/search')
def search() :
    return render_template('search.html')