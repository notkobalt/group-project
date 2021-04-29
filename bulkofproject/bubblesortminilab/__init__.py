#import flask and blueprints
from flask import Blueprint, render_template, __name__, request

#create blueprint
bubblesortminilab = Blueprint('bubble_sort', __name__)

@bubblesortminilab.route('/dylan', methods = ['GET', 'POST'])
def dylan():
    return render_template('bubblesortminilab/dylan.html')