#imports
##import flask and database
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#configure flask app
app = Flask(__name__, static_url_path= '', static_folder = 'static')
app.config['SECRET_KEY'] = 'ineedsleep'
app.config['SQLALCHEMY_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

#import routes
from bulkofproject import routes