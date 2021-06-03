#import flask and blueprints
from flask import Blueprint, render_template, __name__, request

reviews_bp = Blueprint('reviews', __name__)

#game = game
game = 'test'
@reviews_bp.route('/<link>')
#parameters in "reviews" make the link adaptable, will have a for loop once query system is set up changein the 'test' text to the corresponding games (2 week ticket difficult to convey in 1 ticket a week system)

#for game in gamelist:
def reviews(link = game):

    return render_template('reviews/reviews.html', #game = test
    )



