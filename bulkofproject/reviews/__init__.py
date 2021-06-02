#import flask and blueprints
from flask import Blueprint, render_template, __name__, request

reviews_bp = Blueprint('reviews', __name__)

@reviews_bp.route('/<game>')
#parameters in "reviews" make the link adaptable, will have a for loop once query system is set up changein the 'test' text to the corresponding games (2 week ticket difficult to convey in 1 ticket a week system)
def reviews(game = 'test'):
    return render_template('reviews/reviews.html')



