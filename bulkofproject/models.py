#imports
##import config from __init__
from bulkofproject import db

#database tables (models)
##login
class login(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(15), unique = True, nullable = False)
    password = db.Column(db.String(), nullable = False)