#import flask and blueprints
from flask import Blueprint, render_template, __name__, request

reviews_bp = Blueprint('reviews', __name__)

@reviews_bp.route('/write')
def write():
    if request.method == 'POST':
        return render_template('reviews/write.html')
    else:
        return render_template('reviews/write.html')

@reviews_bp.route('/')
def review():
    if request.method == 'POST':
        return render_template('reviews/review.html')
    else:
        return render_template('reviews/review.html')