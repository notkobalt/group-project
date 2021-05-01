#import flask and blueprints
from flask import Blueprint, render_template, __name__, request
#import dylan lab
from bulkofproject.bubblesortminilab.dylanlab import listgen, bubblesort

#create blueprint
bubblesortminilab = Blueprint('bubble_sort', __name__)

@bubblesortminilab.route('/dylan', methods = ['GET', 'POST'])
def dylan():
    #list
    initial = listgen(10)
    print(initial)
    final = bubblesort(initial)
    print(final)

    return render_template('bubblesortminilab/dylan.html', initial = initial, final = final)