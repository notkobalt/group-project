#imports
##import config from __init__
from bulkofproject import db
from datetime import datetime

#database tables (models)
##login db
class User(db.Model):
    #table columns
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(15), unique = True, nullable = False)
    password = db.Column(db.String(), nullable = False)

    #callable attributes
    def __repr__(self):
        return f"user('{self.username}', '{self.password}')"

##rating db
class rating(db.Model):
    #table columns
    id = db.Column(db.Integer, primary_key = True)
    game = db.Column(db.Text, nullable = False)
    stars = db.Column(db.Integer, nullable = False)
    review = db.Column(db.Text, nullable = False)
    user = db.Column(db.Text, nullable = False)

    def __repr__(self):
        return f"user('{self.game}', {self.stars}', '{self.review}', '{self.user}')"